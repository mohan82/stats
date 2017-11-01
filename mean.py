import sys
import matplotlib.pyplot as pyplot



def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


def mean(numbers):
    return sum(numbers)/len(numbers)


def main(args):
    print(mean([1, 2, 3, 4, 5, 6]))
    pyplot.pie([1,2,3])
    pyplot.show()


if __name__ == '__main__':
    main(sys.argv)
