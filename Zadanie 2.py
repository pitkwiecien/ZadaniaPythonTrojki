from typing import List


def get_ints(filename: str) -> List[int]:
    with open(filename, "r") as file:
        content = []
        for line in file:
            content.append(int(line[:-1]))
            if 'str' in line:
                break
        return content


def disassemble(number: int, found_divisors: tuple = ()) -> List[int]:
    new_found_divisors = list(found_divisors)
    broken = False
    for i in range(2, number):
        if number % i == 0:
            new_found_divisors.append(i)
            new_found_divisors = disassemble(round(number / i), tuple(new_found_divisors))
            broken = True
            break
    if not broken:
        new_found_divisors.append(number)
    return new_found_divisors


def count_distinct(in_list: list) -> int:
    values = set()
    for value in in_list:
        values.add(value)
    return len(values)


contents = get_ints("sources/liczby.txt")

max_divisors = [0, []]
max_unique_divisors = (0, [])
for item in contents:
    disassembled = disassemble(item)
    divisors = len(disassembled)
    unique_divisors = count_distinct(disassembled)
    if divisors > max_divisors[0]:
        max_divisors = (divisors, [item])
    elif divisors == max_divisors[0]:
        max_divisors[1].append(item)
    if unique_divisors > max_unique_divisors[0]:
        max_unique_divisors = (unique_divisors, [item])
    elif unique_divisors == max_unique_divisors[0]:
        max_unique_divisors[1].append(item)

max_divisors = list(max_divisors)
max_unique_divisors = list(max_unique_divisors)
max_divisors[1] = [str(i) for i in max_divisors[1]]
max_unique_divisors[1] = [str(i) for i in max_unique_divisors[1]]

print(f"Liczby o największej ilości dzielników: {', '.join(max_divisors[1])} ({max_divisors[0]} dzielników)")
print(f"Liczby o największej ilości unikalnych dzielników: {', '.join(max_unique_divisors[1])} ({max_unique_divisors[0]} unikalnych dzielników)")