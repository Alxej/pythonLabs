import pandas as pd


def sellers(n):
    # Чтение данных из CSV файла
    df = pd.read_csv('6/tranzaktions.csv', sep="\t")
    # Формирование имени колонки для конкретного продавца
    seller_column = f'seller_{n}'
    seller = df[df["Продавец"] == seller_column]["Цена (млн)"]
    print(seller)
    # Вычисление суммы и среднего значения вырученных средств для продавца
    sum_n = seller.sum()
    print(sum_n)
    avg_n = round(seller.mean())
    print(avg_n)

    # Вычисление среднего значения для автомобилей с ценой >= 2 миллиона
    avg2_n = round(seller[seller.ge(2)].mean())
    print(avg2_n)
    # Возврат суммы значений
    return sum_n + avg_n + avg2_n


if __name__ == "__main__":
    sel_n = sellers(2)
    print(sel_n)