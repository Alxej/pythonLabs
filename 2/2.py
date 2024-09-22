import re


def function(find_str: str):
    return len(re.findall(r'[a-zA-Zа-яёА-ЯЁ]+(?:-[a-zA-Zа-яёА-ЯЁ]+){1,4}|[a-zA-Zа-яёА-ЯЁ]+', find_str))


if __name__ == "__main__":
    print(function("""Он --- серо-буро-малиновый слон!!>>>:->А не кот."""))
    print(function("""Он - человек!!>>>:->А не кот."""))