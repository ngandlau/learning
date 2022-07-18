import pandas as pd



class Preprocessor:
    df_in = None
    df_out = None

    def preprocess(self, df):
        print("== after assignment ==")
        self.df_in = df
        self.df_out = df
        print(id(self.df_in))
        print(id(self.df_out))

        print("== after filtering ==")
        self.df_out = self.df_out[self.df_out['numbers'] == 1]
        print(id(self.df_in))
        print(id(self.df_out))

        print("== after renaming a column ==")
        self.df_out = self.df_out.rename(columns={'numbers' : 'nums'})
        print(id(self.df_in))
        print(id(self.df_out))

        return self.df_out

if __name__ == '__main__':
    df = pd.DataFrame({'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']})
    preprocessor = Preprocessor()
    preprocessor.preprocess(df)

    print()
    print(preprocessor.df_in)
    print()
    print(preprocessor.df_out)


# foo@bar: ~$ python dataframe_copies.py

# == after assignment ==
# 140324637052976
# 140324637052976
# == after filtering ==
# 140324637052976
# 140324600054928
# == after renaming a column ==
# 140324637052976
# 140324600054688
#
#    numbers letters
# 0        1       a
# 1        2       b
# 2        3       c
#
#    nums letters
# 0     1       a