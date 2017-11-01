import sys
import mean as m
import math


def variance(numbers):
    mean = m.mean(numbers)
    xminus_mean = []
    for i in numbers:
        x = (i - mean) ** 2
        xminus_mean.append(x)
    return sum(xminus_mean) / (len(xminus_mean) - 1)


def std_dev(numbers):
    return math.sqrt(variance(numbers))


def main(args):
    print(args[0])


if __name__ == '__main__':
    main(sys.argv)
