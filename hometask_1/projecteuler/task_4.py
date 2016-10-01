"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
if __name__ == '__main__':
    start_number_first = 999
    palindromic_numbers = list()
    while (start_number_first > 99):
        start_number_second = 999
        while (start_number_second > 99):
            product = start_number_first * start_number_second
            if (str(product) == str(product)[::-1]):
                palindromic_numbers.append(product)
            start_number_second -= 1
        start_number_first -= 1

    print(sorted(palindromic_numbers)[-1])
