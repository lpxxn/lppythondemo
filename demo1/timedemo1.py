from datetime import datetime

v1 = 1


def ConvertTimeStampToTime(time_stamp):
    data = datetime.fromtimestamp(time_stamp)
    # global v1
    print(v1)
    print(data)


print(__name__)
if __name__ == "__main__":
    ConvertTimeStampToTime(1530512099)
