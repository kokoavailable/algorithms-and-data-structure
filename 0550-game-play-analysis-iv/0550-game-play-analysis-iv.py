import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    a2 = activity.groupby('player_id')['event_date'].min().reset_index()
    a2.rename(columns={'event_date': 'min_date'}, inplace=True)
    
    activity['previous_date'] = activity['event_date'] - pd.Timedelta(days=1)
    merged = activity.merge(a2, on='player_id')
    filtered = merged[merged['min_date'] == merged['previous_date']]
    
    fraction = round(filtered['player_id'].nunique() / a2['player_id'].nunique(), 2)
    
    return pd.DataFrame({'fraction': [fraction]})