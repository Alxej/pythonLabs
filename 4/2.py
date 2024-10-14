import numpy as np


def function(price1: list, price2: list):
    n_price1 = np.array(price1)
    n_price2 = np.array(price2)
    n_price1 = n_price1[::2]
    n_price2 = n_price2[::2]
    price_avg1 = n_price1.mean()
    price_avg2 = n_price2.mean()
    price_avg = (price_avg1 + price_avg2) / 2
    price = np.concatenate([n_price1[n_price1 < price_avg], n_price2[n_price2 < price_avg]]) # noqa E501
    price_avg, price_std = int(price.mean()), int(price.std())
    return price_avg + price_std


if __name__ == "__main__":
    print(function([11, 22, 33, 44, 55, 66, 77], [11, 22, 33, 44, 55, 66, 77]))
    print(function([15, 22, 33, 44, 55, 66, 77], [17, 22, 33, 44, 55, 66, 77]))
