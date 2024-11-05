import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_user_count = users['user_id'].nunique()
    
    contest_user_counts = (
        register.groupby('contest_id')['user_id']
        .nunique()
        .reset_index())
    
    contest_user_counts.rename(columns={'user_id': 'registered_user_count'}, inplace=True)

    
    contest_user_counts['percentage'] = (contest_user_counts['registered_user_count'] * 100.0 / total_user_count).round(2)

    contest_user_counts = (
        contest_user_counts
        .sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
        .reset_index(drop=True)
        .drop(columns=['registered_user_count'])
    )
    
    return contest_user_counts