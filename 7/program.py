import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def read_document():
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

    my_file_path = path + '\\creditcard.csv'
    return pd.read_csv(my_file_path)


def split_data(dataframe: pd.DataFrame, ratio: float):
    y = dataframe["Class"]
    x_train, x_test, y_train, y_test = train_test_split(dataframe,
                                                        y,
                                                        test_size=ratio,
                                                        stratify=y)
    return dataframe, y, x_train, x_test, y_train, y_test


if __name__ == "__main__":
    document = read_document()[:50000]
    x, y, x_train, x_test, y_train, y_test = split_data(dataframe=document,
                                                        ratio=0.3)
    print(np.unique(y_test))