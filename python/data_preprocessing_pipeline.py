"""
An elegant way to define a data preprocessing pipeline using function composition.
The idea comes from https://www.youtube.com/watch?v=L_KlPZ5qBOU
"""

from functools import partial, reduce
from typing import Callable
import pandas as pd

data = {'age': [18, 30, 40, 45], 'salary_per_month': [1000, 4000, 5000, 8000]}
df = pd.DataFrame(data)

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]

def compose(*functions: Preprocessor) -> Preprocessor:
	return reduce(lambda f,g: lambda x: g(f(x)), functions)

def create_column_is_younger_than_18(df: pd.DataFrame) -> pd.DataFrame:
	df['is_younger_than_18'] = df['age'] < 18
	return df

def create_column_salary_per_year(df: pd.DataFrame) -> pd.DataFrame:
	df['salary_per_year'] = df['salary_per_month'] * 12
	return df

def multiply_column_by_constant(df: pd.DataFrame, column: str, constant: int) -> pd.DataFrame:
	df[column] = df[column] * constant
	return df


if __name__ == '__main__':
	# define preprocessing pipeline
	apply_preprocessing_pipeline = compose(
		create_column_is_younger_than_18,
		create_column_salary_per_year,
		partial(multiply_column_by_constant, column='salary_per_month', constant=2)
	)
	
	print(df.head())
	
	# apply preprocessing pipeline to dataframe *inplace*
	apply_preprocessing_pipeline(df)

	print(df.head())


