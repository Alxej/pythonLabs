import re


def function(find_str: str):
    return len(re.findall(r'\b[ОоЭэ]\w+', find_str))


if __name__ == "__main__":
    print(function('Сказала Ольга: "Это верно ,что 2+2=4"'))
    print(function('Это надо знать. Это - классика'))
