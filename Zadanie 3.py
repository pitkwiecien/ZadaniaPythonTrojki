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


def has_duplicates(collection):
    items = set()
    for item in collection:
        items.add(item)
    return len(items) != len(collection)


def remove_duplicates(from_list):
    without_duplicates = []
    for elem in from_list:
        if not has_duplicates(elem):
            without_duplicates.append(elem)
    return without_duplicates


def get_max_divisors(from_list):
    max_divisors = 0
    for item in from_list:
        disassembled = disassemble(item)
        divisors = len(disassembled)
        if divisors > max_divisors:
            max_divisors = divisors
    return max_divisors


def split_to_levels(from_list):
    divisor_amount_list = [[] for _ in range(get_max_divisors(contents) + 1)]
    for item in from_list:
        divisors = len(disassemble(item))
        divisor_amount_list[divisors].append(item)
    return divisor_amount_list


def get_perfect_list(from_list, depth):
    divisor_amount_list = split_to_levels(from_list)
    levels = len(divisor_amount_list)

    perfect_list = [[] for _ in range(depth + 1)]
    for i in range(len(perfect_list) - 1, 0, -1):
        if i == 0:
            continue
        else:
            for added_list_index in range(i, levels - (depth - i)):
                perfect_list[i] += divisor_amount_list[added_list_index]

    return perfect_list


def write_list(to_file, from_list):
    with open(to_file, "w+") as file:
        for elem in from_list:
            line = ""
            for number in elem:
                line += str(number) + " "
            file.write(line + "\n")


def get_perfect_fives(from_list, write_file=None):
    perfect_list = get_perfect_list(from_list, 5)

    eq = []
    for n5 in perfect_list[5]:
        for n4 in perfect_list[4]:
            if (n5 % n4) != 0 or n4 > n5:
                continue
            for n3 in perfect_list[3]:
                if (n4 % n3) != 0 or n3 > n4:
                    continue
                for n2 in perfect_list[2]:
                    if (n3 % n2) != 0 or n2 > n3:
                        continue
                    for n1 in perfect_list[1]:
                        if (n2 % n1) == 0 and n2 > n1:
                            eq.append((n1, n2, n3, n4, n5))

    eq = remove_duplicates(eq)

    if write_file is not None:
        write_list(write_file, eq)

    return eq


def get_perfect_threes(from_list, write_file=None):
    perfect_list = get_perfect_list(from_list, 3)
    eq = []
    for n3 in perfect_list[3]:
        for n2 in perfect_list[2]:
            if (n3 % n2) != 0 or n2 > n3:
                continue
            for n1 in perfect_list[1]:
                if (n2 % n1) == 0 and n2 > n1:
                    eq.append((n1, n2, n3))
    eq = remove_duplicates(eq)

    if write_file is not None:
        write_list(write_file, eq)

    return eq


contents = get_ints("sources/liczby.txt")

fives = get_perfect_fives(contents, "returns/piatki.txt")
threes = get_perfect_threes(contents, "returns/trojki.txt")

print(f"takich trójek jest: {len(threes)}")
print(f"takich piątek jest: {len(fives)}")
