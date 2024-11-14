import pandas as pd


def frame_data(list1, list2, indices, value):
    df1 = pd.DataFrame(list1, index=indices)
    df2 = pd.DataFrame(list2, index=indices)

    df1.sort_index(inplace=True)
    df1 = df1.head(2)
    df1_filtered = df1[df1.lt(value).all(axis=1)]

    df2 = df2.iloc[:, :2]
    df2_filtered = df2[df2.gt(value).all(axis=1)]

    total_sum = df1_filtered.sum() + df2_filtered.sum()

    return float(total_sum)


if __name__ == "__main__":
    print(frame_data([[4,5],[7,8]], [[20,30],[4,5]], ['C','D'], 6))
