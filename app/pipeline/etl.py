import pandas as pd

from app.database.connection import get_db
from app.models import Product


class Processing:

    def __init__(self):
        self.db = get_db()

    def replace_nan_with_unknown(sefl, value):
        if pd.isna(value):
            return "unknown"
        else:
            return value

    def extract(self, file_path: str) -> pd.DataFrame:
        """Extract data from a CSV file."""

        # Create a mapping dictionary
        fat_content_map = {
            "Low Fat": "Low Fat",
            "low fat": "Low Fat",
            "LF": "Low Fat",
            "Regular": "Regular",
            "reg": "Regular"
        }

        data = pd.read_csv(file_path)

        # Apply the mapping to standardize the "Item_Fat_Content" column
        data["Item_Fat_Content"] = data["Item_Fat_Content"].map(fat_content_map)

        numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
        data[numeric_columns] = data[numeric_columns].fillna(0)

        object_columns = data.select_dtypes(include=["object"]).columns
        data[object_columns] = data[object_columns].fillna("unknown")

        return data

    def transform(selt, data: pd.DataFrame) -> pd.DataFrame:
        """Transform data to match the Product schema, handle nulls."""
        # Convert NaN to None, as NaN is not supported by SQLAlchemy for non-float columns
        return data.where(pd.notnull(data), None)

    def load(self, data: pd.DataFrame):
        """Load data into the PostgreSQL database."""
        # Convert DataFrame to a list of dictionaries for bulk insert
        data_records = data.to_dict(orient="records")

        try:
            for row in data_records:
                self.db.add(Product(
                    item_identifier=row["Item_Identifier"],
                    item_weight=row["Item_Weight"],
                    item_fat_content=row["Item_Fat_Content"],
                    item_visibility=row["Item_Visibility"],
                    item_type=row["Item_Type"],
                    item_mrp=row["Item_MRP"],
                    outlet_identifier=row["Outlet_Identifier"],
                    outlet_establishment_year=row["Outlet_Establishment_Year"],
                    outlet_size=row["Outlet_Size"],
                    outlet_location_type=row["Outlet_Location_Type"],
                    outlet_type=row["Outlet_Type"],
                    item_outlet_sales=row["Item_Outlet_Sales"]
                ))
            self.db.commit()
            print(f"{len(data_records)} records successfully loaded into the database.")
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
        finally:
            self.db.close()

    def run_pipeline(self):
        csv_file_path = "data/data_raw.csv"
        data = self.extract(csv_file_path)
        data = self.transform(data)
        self.load(data)
