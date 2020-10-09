n = int(input("Enter a number: "))


# https://www.geeksforgeeks.org/python-program-to-concatenate-two-integer-values-into-one/
# Python program to concatenate
# two numbers


def num_concat(num1, num2):
    # Convert both the numbers to
    # strings
    num1 = str(num1)
    num2 = str(num2)

    # Concatenate the strings
    num1 += num2

    return int(num1)


print("Sample value of n is", n)
print("Expected Result:", n + num_concat(n, n) + num_concat(num_concat(n, n), n))
