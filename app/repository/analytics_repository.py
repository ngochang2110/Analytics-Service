import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from app.repository.product_repository import ProductRepository


class AnalyticsReport:
    def __init__(self):
        self.product_repository = ProductRepository()

    def sales_performance_report(self):
        result = self.product_repository.get_sales_performance()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

    def average_item_visibility_report(self):
        result = self.product_repository.get_average_item()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

    def display_average_item_visibility_report(self):
        df = self.average_item_visibility_report()
        # Bar Chart for Average Visibility and Sales
        fig, ax = plt.subplots()
        df.plot(x="outlet_type", y=["avg_visibility", "avg_sales"], kind="bar", ax=ax)
        st.pyplot(fig)

    def display_trend_year_report(self):
        result = self.product_repository.get_sales_trend_year()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        fig = px.line(df, x="outlet_establishment_year", y="total_sales",
                      title="Sales Trends Over the Years", markers=True)
        st.header("Sales Trends Over the Years")
        st.plotly_chart(fig)

    def display_price_range_report(self):
        result = self.product_repository.get_price_range()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # Create traces for Min, Max, and Avg Prices
        trace_min = go.Bar(x=df["outlet_location_type"], y=df["min_price"], name="Min Price")
        trace_max = go.Bar(x=df["outlet_location_type"], y=df["max_price"], name="Max Price")
        trace_avg = go.Bar(x=df["outlet_location_type"], y=df["avg_price"], name="Avg Price")
        data = [trace_min, trace_max, trace_avg]
        layout = go.Layout(
            title="Price Range by Outlet Location Type",
            xaxis=dict(title="Outlet Location Type"),
            yaxis=dict(title="Price"),
            barmode="group"
        )
        fig = go.Figure(data=data, layout=layout)
        st.header("Price Range Analysis in Different Locations")
        st.plotly_chart(fig)

    def display_stock_level_report(self):
        result = self.product_repository.get_stock_level()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        fig = px.bar(df, x="outlet_size", y="item_count", color="item_type",
                     title="Stock Levels by Item Type in Different Outlet Sizes",
                     barmode="stack")
        st.header("Stock Levels by Item Type in Different Outlet Sizes")
        st.plotly_chart(fig)

    def display_sales_performance_report(self):
        result = self.product_repository.get_sales_performance()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        fig = px.pie(df, values="total_sales", names="item_type",
                     title="Sales Distribution by Item Type")
        st.header("Sales Distribution by Item Type")
        st.plotly_chart(fig)

    def display_dashboard_item_report(self):
        result = self.product_repository.get_sale_dashboard()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        st.header("Product Sales and Outlet Analysis")
        st.write("Overview of sales performance, item weight, and visibility by various dimensions.")
        st.table(df)


class ReportDisplay:
    def __init__(self):
        self._report = AnalyticsReport()

    def display(self):
        st.title("E-Commerce Sales and Stock Analytics")
        report_type = st.selectbox("Select Report Type",
                                   ["SalesPerformance", "AverageItemVisibility",
                                    "PricesRange", "SalesTrendsYears", "StockLevelsItems",
                                    "ReportDashboard"
                                    ])

        if report_type == "SalesPerformance":
            self._report.display_sales_performance_report()

        if report_type == "AverageItemVisibility":
            self._report.display_average_item_visibility_report()

        if report_type == "PricesRange":
            self._report.display_price_range_report()

        if report_type == "SalesTrendsYears":
            self._report.display_trend_year_report()

        if report_type == "StockLevelsItems":
            self._report.display_stock_level_report()

        if report_type == "ReportDashboard":
            self._report.display_dashboard_item_report()
