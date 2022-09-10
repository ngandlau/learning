"""
An elegant way to define a data preprocessing pipeline using function composition.
The idea comes from https://www.youtube.com/watch?v=L_KlPZ5qBOU
"""

import pandas as pd
from functools import reduce

data = {'age': [18, 30, 40, 45], 'salary_per_month': [1000, 4000, 5000, 8000]}
df = pd.DataFrame(data)

Preprocessor = Callable([pd.DataFrame], pd.DataFrame)

def create_column_age_group(df: pd.DataFrame) -> pd.DataFrame:
	df['age_group'] = df['age'].map(lambda age: if age < 18: 'young' else 'old')
	return df

def create_column_salary_per_year(df: pd.DataFrame) -> pd.DataFrame:
	df['salary_per_year'] = df['salary'] * 12
	return df

def compose(*functions: Preprocessor) -> Preprocessor:
	return reduce(lambda f, g: lambda x: g(f(x)))

if __name__ == '__main__':
	# define preprocessing pipeline
	preprocessor = Preprocessor(
		create_column_age_group,
		create_column_salary_per_year
	)
	
	# apply preprocessing pipeline to dataframe
	df_preprocessed = preprocessor(df)


