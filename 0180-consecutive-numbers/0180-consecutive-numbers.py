import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev_num'] = logs['num'].shift(1)
    logs['next_num'] = logs['num'].shift(-1)
    
    consecutive_nums_df = logs[(logs['num'] == logs['prev_num']) & (logs['num'] == logs['next_num'])]
    consecutive_nums = consecutive_nums_df['num'].drop_duplicates()
    
    result = pd.DataFrame({'ConsecutiveNums': consecutive_nums})
    
    return result