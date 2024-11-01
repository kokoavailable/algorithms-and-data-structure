import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(project, employee, on="employee_id")
    
    result = (
        merged_df.groupby("project_id")["experience_years"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"experience_years": "average_years"})
    )

    return result