import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = followers.groupby('user_id').agg(
            followers_count = ('follower_id', 'count')).reset_index()
    
    
    return result