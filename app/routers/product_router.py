from fastapi import APIRouter
from app.pipeline.etl import Processing
from app.services.product_service import ProductService

product_router = APIRouter(prefix="/product", tags=["Product"])

@product_router.post("/upload_csv")
def upload_csv():
    etl = Processing()
    etl.run_pipeline()
    return {"message": "Import data successful"}


@product_router.get("/price-range")
def get_price_range():
    product_service = ProductService()
    data = product_service.get_price_range_service()
    return {
        "status": 200,
        "data": data
    }

@product_router.get("/stock-level")
def get_stock_level():
    product_service = ProductService()
    data = product_service.get_stock_level_service()
    return {
        "status": 200,
        "data": data
    }


@product_router.get("/average-item")
def get_average_item():
    product_service = ProductService()
    data = product_service.get_average_item_service()
    return {
        "status": 200,
        "data": data
    }


@product_router.get("/sales-trend-year")
def get_sales_trend_year():
    product_service = ProductService()
    data = product_service.get_sales_trend_year_service()
    return {
        "status": 200,
        "data": data
    }


@product_router.get("/sale-dashboard")
def get_sale_dashboard():
    product_service = ProductService()
    data = product_service.get_sale_dashboard_service()
    return {
        "status": 200,
        "data": data
    }


@product_router.get("/sales-performance")
def get_sales_performance():
    product_service = ProductService()
    data = product_service.get_sales_performance_service()
    return {
        "status": 200,
        "data": data
    }