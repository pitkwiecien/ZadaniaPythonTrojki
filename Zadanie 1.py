with open('sources/liczby.txt', 'r') as file:
    count = 0
    first_number = None
    for line in file:
        if line[0] == line[-2]:  # -2 zamiast -1 ponieważ ostatni znak w kazdej linii jest pusty
            if first_number is None:
                first_number = line[::-1]
            count += 1

    print(f"Takich liczb jest {count}")
    print(f"Pierwsza liczba spełniająca ten warunek to {first_number}")
