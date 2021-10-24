def fizzbuzz(num1, num2):
    for number in range(1, 100 + 1):
        if number % num1 == 0 and number % num2 == 0:
            print('FizzBuzz')
        elif number % num2 == 0:
           print("Fizz")
        elif number % num1 == 0:
            print('Buzz')
        else:
            print(number)

fizzbuzz(3,7)