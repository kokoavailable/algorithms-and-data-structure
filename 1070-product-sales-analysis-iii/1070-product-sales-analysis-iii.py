import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    first_year = sales.groupby('product_id')['year'].min().reset_index()
    first_year.rename(columns={'year':'first_year'}, inplace=True)
    
    merged = first_year.merge(sales, on='product_id')
    
    filtered = merged[merged['year'] == merged['first_year']]
    
    result = filtered[['product_id', 'first_year', 'quantity', 'price']]
    
    return result