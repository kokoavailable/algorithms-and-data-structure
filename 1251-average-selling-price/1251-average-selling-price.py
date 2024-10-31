import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    sales = units_sold.merge(
        prices,
        on="product_id",
        how="inner"
    )
    sales = sales[(sales["purchase_date"] >= sales["start_date"]) & (sales["purchase_date"] <= sales["end_date"])]

    # Step 2: Revenue 테이블 생성
    # product_id를 기준으로 총 매출과 총 판매 단위를 집계
    revenue = sales.groupby("product_id").agg(
        total_revenue=pd.NamedAgg(column="price", aggfunc=lambda x: (x * sales.loc[x.index, "units"]).sum()),
        total_units=pd.NamedAgg(column="units", aggfunc="sum")
    ).reset_index()

    # Step 3: 모든 Products에 대해 LEFT JOIN 수행
    # Prices에 존재하는 모든 product_id를 기준으로 revenue를 조인하고 평균 가격 계산
    distinct_products = prices[["product_id"]].drop_duplicates()
    result = distinct_products.merge(
        revenue,
        on="product_id",
        how="left"
    )

    # 평균 가격 계산 및 NaN 처리
    result["average_price"] = (result["total_revenue"] / result["total_units"]).round(2).fillna(0)

    # 필요한 열만 선택하여 반환
    return result[["product_id", "average_price"]]