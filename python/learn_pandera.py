import pandera as pa
from pandera import SchemaModel, Column, Check, Float, Field
from typing import List
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


class SchemaNPuncStops(SchemaModel):
    n_stops: Series[Float]
    n_punctual_stops: Series[Float]

class SchemaPunc(SchemaNPuncStops):
    # punctualities must be Floats and values between 0.0 and 1.0
    punctuality: Series[Float] = Field(ge=0.0, le=1.0)

@pa.check_types
def calculate_punctuality(df: DataFrame[SchemaNPuncStops]) -> DataFrame[SchemaPunc]:
    dfpunc = df.copy()
    dfpunc['punctuality'] = dfpunc['n_punctual_stops'] / dfpunc['n_stops']
    return dfpunc.pipe(DataFrame[SchemaPunc])

if __name__ == '__main__':
    df_schema = DataFrame[SchemaNPuncStops]({
        'n_stops': [100., 100., 100.],
        'n_punctual_stops': [80.0, 60.0, 50.0]
    })
    df_valid = pd.DataFrame({
        'n_stops': [100., 100., 100.],
        'n_punctual_stops': [80.0, 60.0, 50.0]
    })

    df_invalid_cols = pd.DataFrame({
        'n_stops': [100., 100., 100.],
    })
    # print(calculate_punctuality(df=df_valid))
    print(calculate_punctuality(df=df_schema))
    print(calculate_punctuality(df=df_valid))
    # print(calculate_punctuality(df=df_invalid_cols))
