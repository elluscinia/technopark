"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
if __name__ == '__main__':
    first = 1
    last = 2
    number = first + last
    result = 0 + last
    while (number < 4000000):
        if number % 2 == 0:
            result += number
        first, last = last, first + last
        number = first + last

    print(result)
