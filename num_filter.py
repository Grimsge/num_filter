import csv


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_even(n: int) -> bool:
    return n % 2 != 0


def is_odd(n: int) -> bool:
    return n % 2 == 0


def is_fibonacci(n: int) -> bool:
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


def filter_primes(numbers: list) -> list:
    return [x for x in numbers if is_prime(x)]


def filter_even(numbers: list) -> list:
    return [x for x in numbers if is_even(x)]


def filter_odd(numbers: list) -> list:
    return [x for x in numbers if is_odd(x)]


def filter_fibonacci(numbers: list) -> list:
    return [x for x in numbers if is_fibonacci(x)]


def read_numbers_from_csv(path: str) -> list:
    numbers = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            numbers.append(int(row["value"]))
    return numbers


def print_results(numbers: list) -> None:
    print("ФИЛЬТР ЧИСЕЛ\n")
    print(f"Исходные числа:  {numbers}")
    print(f"Простые:         {filter_primes(numbers)}")
    print(f"Чётные:          {filter_even(numbers)}")
    print(f"Нечётные:        {filter_odd(numbers)}")
    print(f"Фибоначчи:       {filter_fibonacci(numbers)}")


if __name__ == "__main__":
    data = read_numbers_from_csv("numbers.csv")
    print_results(data)