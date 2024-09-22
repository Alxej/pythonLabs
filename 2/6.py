import datetime


def function(dt1: str, dt2: str):
    date1 = datetime.datetime(year=int(dt1[:4]),
                              month=int(dt1[4:6]),
                              day=int(dt1[6:8]),
                              hour=int(dt1[9:11]),
                              minute=int(dt1[12:14]),
                              second=int(dt1[15:17]))

    date2 = datetime.datetime(year=int(dt2[:4]),
                              month=int(dt2[4:6]),
                              day=int(dt2[6:8]),
                              hour=int(dt2[9:11]),
                              minute=int(dt2[12:14]),
                              second=int(dt2[15:17]))

    difference = date1 - date2
    return int(abs(difference.total_seconds()) / 3600)


if __name__ == '__main__':
    print(function("20211212 12:12:12", "20211212 11:12:12"))
    print(function("20211212 12:12:12", "20211213 12:13:13"))