import re


def write(input_path: str, output_path: str):
    matches = []
    with open(input_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.findall(r'KEEP[\s\S]*pressure=[0-9]*', line)
            if len(match) > 0:
                matches.append(re.findall(r'pressure=[0-9]*', match[0])[0]
                               .split("=")[-1])
    if len(matches) > 0:
        with open(output_path, 'a') as output:
            output.write('\n'.join(matches))


def get_sum(input_path: str):
    with open(input_path, 'r') as f:
        lines = f.readlines()
    integers = [int(line.strip()) for line in lines]
    minimal = min(integers)
    maximum = max(integers)
    average = sum(integers) / len(integers)
    return minimal + maximum + int(average)


if __name__ == '__main__':
    write(input_path='2/extra/n_log1.txt', output_path='2/out/out1.txt')
    print(get_sum('2/out/out1.txt'))