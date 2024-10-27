import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False)
    
    result = employee[employee['rank'] ==2][['salary']].drop_duplicates()
    
    if result.empty:
        result = pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        result.columns = ['SecondHighestSalary']
    
    return result