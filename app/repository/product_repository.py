import logging
from sqlalchemy import text
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import get_db
from app.models import Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProductRepository:

    def __init__(self):
        self.db = get_db()

    def get_products(self):
        try:
            sql = text("SELECT * FROM products")
            result = self.db.execute(sql)

            products = [Product(**row) for row in result.mappings().all()]
            return products

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_sales_performance(self):
        """Sales Performance by Item Type and Fat Content"""
        try:
            sql = text(f"""
                        SELECT item_type, item_fat_content, SUM(item_outlet_sales) AS total_sales
                        FROM products
                        GROUP BY item_type, item_fat_content
                        ORDER BY total_sales DESC;""")

            result = self.db.execute(sql)

            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_average_item(self):
        """Average Item Visibility and Sales by Outlet Type"""
        try:
            sql = text(f"""
                        SELECT outlet_type, AVG(item_visibility) AS avg_visibility, AVG(item_outlet_sales) AS avg_sales
                        FROM products
                        GROUP BY outlet_type;""")

            result = self.db.execute(sql)
            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_sales_trend_year(self):
        """Sales Trends Over Years"""
        try:
            sql = text(f"""
                        SELECT outlet_establishment_year, SUM(item_outlet_sales) AS total_sales
                        FROM products
                        GROUP BY outlet_establishment_year
                        ORDER BY outlet_establishment_year;
                        """)

            result = self.db.execute(sql)
            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_stock_level(self):
        """Stock Levels by Item Type in Different Outlet Sizes"""
        try:
            sql = text(f"""
                        SELECT item_type, outlet_size, COUNT(*) AS item_count
                        FROM products
                        GROUP BY item_type, outlet_size;
                        """)

            result = self.db.execute(sql)
            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_price_range(self):
        """Price Range Analysis in Different Locations"""
        try:
            sql = text(f"""
                        SELECT outlet_location_type, MIN(item_mrp) AS min_price, 
                        MAX(item_mrp) AS max_price, AVG(item_mrp) AS avg_price
                        FROM products
                        GROUP BY outlet_location_type;
                        """)

            result = self.db.execute(sql)
            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")

    def get_sale_dashboard(self):
        """Product Sales and Outlet Analysis Group by: item_fat_content,
            item_type,
            outlet_size,
            outlet_location_type,
            outlet_type
        """
        try:
            sql = text(f"""
                        SELECT 
                            item_fat_content, 
                            item_type,
                            outlet_size,
                            outlet_location_type,
                            outlet_type,
                            SUM(item_outlet_sales) AS total_sales,
                            AVG(item_weight) AS avg_item_weight,
                            MAX(item_fat_content) AS max_item_fat_content, 
                            MAX(item_type) AS max_item_type,                
                            AVG(item_visibility) AS max_avg_item_visibility,
                            MAX(outlet_establishment_year) AS max_year      
                        FROM 
                            products
                        GROUP BY 
                            item_fat_content, 
                            item_type,
                            outlet_size,
                            outlet_location_type,
                            outlet_type
                        ORDER BY 
                            item_fat_content, 
                            item_type,
                            outlet_size,
                            outlet_location_type,
                            outlet_type
                        """)

            result = self.db.execute(sql)
            return result

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching products")
