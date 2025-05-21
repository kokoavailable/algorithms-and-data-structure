import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[orders["order_date"].dt.year == 2019]

    orders_count = orders_2019.groupby("buyer_id").size().reset_index(name="orders_in_2019")

    result = pd.merge(users, orders_count, how="left", left_on="user_id", right_on="buyer_id")

    result["orders_in_2019"] = result["orders_in_2019"].fillna(0).astype(int)

    final_result = result[["user_id", "join_date", "orders_in_2019"]].rename(columns={"user_id": "buyer_id"})

    return final_result