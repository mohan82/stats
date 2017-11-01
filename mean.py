import sys


def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


def mean(numbers): return sum(numbers) / len(numbers)


def median(numbers):
    sorted_num = sorted(numbers)
    if len(sorted_num) % 2 != 0:
        return sorted_num[int(len(sorted_num)/2)]
    else:
        middle = int(len(sorted_num) / 2)
        a = sorted_num[middle]
        b = sorted_num[middle - 1]
        return (a + b) / 2


def main(args):
    print(mean([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main(sys.argv)
