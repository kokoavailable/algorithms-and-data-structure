import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports = employees[~employees['reports_to'].isna()]
    
    # 상사별로 그룹화하고 직원 수와 평균 나이를 계산
    result = reports.groupby('reports_to').agg(
        reports_count=('employee_id', 'size'),
        average_age=('age', 'mean')
    ).reset_index()
    
    # 평균 나이를 정수로 반올림하여 변경
    result['average_age'] = (result['average_age'] + 0.5).astype(int)
    
    print(result)
    
    # 상사 이름과 employee_id를 원래 테이블에서 가져옴
    result = result.merge(employees[['employee_id', 'name']], left_on='reports_to', right_on='employee_id')
    
    # 컬럼 이름 재정의 및 정렬
    result = result[['employee_id', 'name', 'reports_count', 'average_age']].sort_values('employee_id')
    
    return result