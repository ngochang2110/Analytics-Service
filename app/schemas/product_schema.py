from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    item_identifier: Optional[str] = None
    item_weight: Optional[float] = None
    item_fat_content: Optional[str] = None
    item_visibility: Optional[float] = None
    item_type: Optional[str] = None
    item_mrp: Optional[float] = None
    outlet_identifier: Optional[str] = None
    outlet_establishment_year: Optional[int] = None
    outlet_size: Optional[str] = None
    outlet_location_type: Optional[str] = None
    outlet_type: Optional[str] = None
    item_outlet_sales: Optional[float] = None


