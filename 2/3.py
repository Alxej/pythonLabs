import re


def function(text: str):
    return len(re.findall(r'[А-ЯЁA-Z]{2,}', text))


if __name__ == '__main__':
    print(function(" А курс информатики в вузе соответствует ФГОС и ПООП, что подтверждено ФГУ"))
    print(function(" СССР и США"))
