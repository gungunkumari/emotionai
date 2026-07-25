import pandas as pd


def compare_models(results):

    df = pd.DataFrame(results)

    print(df)

    df.to_csv("model_comparison.csv", index=False)