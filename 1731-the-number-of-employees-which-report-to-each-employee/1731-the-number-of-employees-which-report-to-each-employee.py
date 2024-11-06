import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports = employees[~employees['reports_to'].isna()]
    
    result = reports.groupby('reports_to').agg(
        reports_count=('employee_id', 'size'),
        average_age=('age', 'mean')
    ).reset_index()
    
    result['average_age'] = (result['average_age'] + 0.5).astype(int)
    
    result = result.merge(employees[['employee_id', 'name']], left_on='reports_to', right_on='employee_id')
    
    result = result[['employee_id', 'name', 'reports_count', 'average_age']].sort_values('employee_id')
    
    return result