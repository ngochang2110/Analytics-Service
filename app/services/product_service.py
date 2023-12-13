from app.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self._product_repository = ProductRepository()

    def get_sale_dashboard_service(self):
        results = self._product_repository.get_sale_dashboard()
        return [row for row in results.mappings().all()]

    def get_stock_level_service(self):
        results = self._product_repository.get_stock_level()
        return [row for row in results.mappings().all()]

    def get_sales_performance_service(self):
        results = self._product_repository.get_sales_performance()
        return [row for row in results.mappings().all()]

    def get_average_item_service(self):
        results = self._product_repository.get_average_item()
        return [row for row in results.mappings().all()]

    def get_price_range_service(self):
        results = self._product_repository.get_price_range()
        return [row for row in results.mappings().all()]

    def get_sales_trend_year_service(self):
        results = self._product_repository.get_sales_trend_year()
        return [row for row in results.mappings().all()]
