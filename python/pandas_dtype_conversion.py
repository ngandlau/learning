import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1.0, np.nan,  None, 10.0],
    'B': [1.0, np.nan,  10.0, 10.0],
    'C': [1.0, 5.0,     None, 10.0],
})

if __name__ == "__main__":
    # this works
    df['float_to_int'] = df['C'].astype('Int64')

    # this throws error 'Cannot convert non-finite values (NA or inf) to integer'
    df['float_to_int'] = df['C'].astype('int64')