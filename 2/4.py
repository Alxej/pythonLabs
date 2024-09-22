import re


def function(variable: str):
    new_var = re.sub(r'[A-Z]', lambda x: "_" + x.group(0).lower(), variable)
    return new_var


if __name__ == '__main__':
    print(function("camelCaseVar"))
    print(function("myWonderfulVar"))