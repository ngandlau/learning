## Talk: Guide to Sparkling Data Science Code

References:
* github.com/corriebar/code-complexity
* flake8

Avoid mixing abstraction levels in the same function:

```python
# a function with mixed levels of abstraction
def function(df):
    df = df[~df['age'] >= 100]    # low abstraction
    df = add_features(df)        # high abstraction
    return df

# a function with same levels of abstraction
def function(df):
    df = remove_customers_older_than(df, age=80)
    df = add_features(df)
    return df
```

There are simple metrics to calculate "cleanliness" of your code. Example:

* (Avg) Number of lines (per function)
* (Avg) Length of function names
* (Avg) Number of arguments in functions
* Levels of nested code
* ...

Tools like `flake8` have tools to calculate these metrics, e.g. `flake8-cognitive-complexity`.

You may want to write wrapper functions around the flake8-code-complexity-tools to only receive the data that these tools return. Then do your own analysis and visualizations.

Ideas:
* Calculate complexity metrics
* Visualize the current complexity of your codebase. Most complexity metrics are on the function-level. Hence you get a complexity for each function. You can then rank the functions in your codebase according to their current complexity. Then, you can prioritize which functions you should refactor first.
* It's a matter of culture:
    * 2 hours per month per person to prettify functions. Tackle functions with high complexity first.
    * Have a reading group around "Clean Code" and other books.

She doesn't really like tools like Black that enforce a certain formatting. Me neither tbh.

## Talk: What are you yield from?

References:
* Presenter: Maxim Danilor
* bitbucket.org/danilormy/europython2023
* Check out "David Beasley"
* https://github.com/dabeaz/generators
* https://dabeaz-course.github.io/practical-python/Notes/06_Generators/04_More_generators.html
* Check out Maxim's Talk at Pycon 2022

* We use lists too often.
* Using generators & yields can simplify code
* FastAPI is a library that makes heavy use of generators/yields. Check the repo to learn more.

## Talk about synthetic data

When you train a GAN, the generator never sees actually data. It only ever receives noise as input. If you only use a trained Generator to generate Synthetic Data, it should be GDPR-conform.

How can we measure the goodness of a synthetic dataset that is based on a real dataset? 
* You can measure whether pairwise correlations between columns are similar. For example, `correlation(df_syn['age'], df_syn['salary']) = 0.7` and `correlation(df_real['age'], df_syn['salary'] = 0.75)`. You can then take the average of all pairwise correlations to get an overall "goodness-of-synthetic-data"-score.
* You can inspect each column visually by comparing a column's distribution in the synthetic dataset versus the real dataset. `hist(data=df, x='age', hue='is_real_data')`

## Monorepos

References:
* https://monorepo.tools/ :star:
* poetry-workspace 

* He doesn't like `git submodule`s. It's hard to keep everything synchronized. That's because `git submodule`s are on the commit-level not on the branch-level.
* There are different approaches to Monorepos:
    * CI-based monorepos
    * integrated monorepos
    * package-based monorepos
* The opinionated best approach is a package-based monorepo.

In a **package-based monorepo** your repo looks like this:

```
myrepo/
    src/
        model/
            neuralnet.py
            boosting.py
            pyproject.toml  # <- a package within your monorepo
        data/
            load.py
            preprocess.py
            transform.py
            pyproject.toml  # <- another package
        utils/
            decorators.py
            pyproject.toml  # <- third package
```

* Any commit should have <= 10 changed lines of code. Any feature branch should have <= 10 commits.
* In monorepos you can use _absolute paths_.
* You have synchronized package versions f.a. packages in your monorepo. For example, when you release a new version, all of your packages `model`, `data`, `utils` will have the same version, e.g. `model_v1.4`, `data_v1.4`, `utils_v1.4`. That is nice, because then you know which versions actually work together.
* Poetry may provide a cool feature called **poetry-workspace**, but it's still in development.

## Talk: ... by Miroslav Sedivy

References:
* tatoeba.org
* openstreetmap, openseamap, wheelmap
* brouter.org
* overpass-turbo.eu
* everydoor (Apple AppStore)
* python packages `faker`, `mimesis` for creating artificial (test) data

```python
places = {'Berlin': 2, 'Frankfurt': 0.6, 'Duesseldorf': 0.4}

# randomly draw cities, but draw bigger cities more often
random.choice(values=places.keys(), weights=places.values())
```

## Workshop: Decorators

See notebook `decorators.ipynb`