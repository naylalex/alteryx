def positive_divisor(number, i):
    if number % i == 0:
        print(i)
    elif number == i:
        return number
    if i <= number:
        return positive_divisor(number, i+1)
