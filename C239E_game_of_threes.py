def threes(number):
    while number != 1:
        step = 0
        if number % 3 == 1:
            step = -1
        elif number % 3 == 2:
            step = 1
        print(number, step)
        number = (number + step) // 3
    print(1)

threes(31337357)