import pandas as pd
import numpy as np
import kagglehub


def first_task():
    transaction = [120, -31, '20.1', 12.3, 'bank', 12, -4, -7, 150, 'mr.', 23, 32, 21]
    t = pd.Series(transaction, index=range(10, 23))
    new_t = t[t.map(type).eq(int)]
    print(new_t.var(ddof=1))
    print(new_t.mean())


def second_task():
    s = pd.Series(np.random.normal(size=200))
    s = s ** 2
    s.index = s.index + 2
    print(len(s[s.gt(2)]))
    s = s[1::2]
    print(s[s.lt(2)].sum())


def third_task():
    path = kagglehub.dataset_download("ybifoundation/credit-card-transaction")
    my_file_path = path + '\\CreditCardTransaction.csv'
    df = pd.read_csv(my_file_path)

    dfs = df.sample(n=10000, random_state=np.random.seed(12))
    print(dfs['Department'].value_counts().nlargest(3))
    mask = dfs["Year"].eq(2022)
    new_dfs = dfs[mask]
    mask1 = new_dfs["Month"].isin([1, 2])
    new_dfs = new_dfs[mask1]
    median = new_dfs["TrnxAmount"].median()
    print(new_dfs["TrnxAmount"])
    print(median)
    dfs["Разность"] = abs(dfs["TrnxAmount"] - abs(median))
    print(dfs)


if __name__ == "__main__":
    third_task()