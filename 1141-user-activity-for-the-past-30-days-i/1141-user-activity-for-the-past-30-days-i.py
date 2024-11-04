import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filtered_activity = activity[
        (activity['activity_date'] >= '2019-06-28') &
        (activity['activity_date'] <= '2019-07-27')
    ]
    
    result = (
        filtered_activity.groupby('activity_date')['user_id']
        .nunique()
        .reset_index(name='active_users')
        .rename(columns={'activity_date': 'day'})
    )
    
    return result