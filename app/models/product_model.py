from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    item_identifier = Column(String, index=True)
    item_weight = Column(Float)
    item_fat_content = Column(String)
    item_visibility = Column(Float)
    item_type = Column(String)
    item_mrp = Column(Float)
    outlet_identifier = Column(String, index=True)
    outlet_establishment_year = Column(Integer)
    outlet_size = Column(String)
    outlet_location_type = Column(String)
    outlet_type = Column(String)
    item_outlet_sales = Column(Float)
