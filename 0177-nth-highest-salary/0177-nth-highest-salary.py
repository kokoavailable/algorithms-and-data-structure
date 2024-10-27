import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    
    result = employee[employee['rank'] == N][['salary']].drop_duplicates()

    if result.empty:
        result = pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        result.columns = [f'getNthHighestSalary({N})']
    
    
    return result