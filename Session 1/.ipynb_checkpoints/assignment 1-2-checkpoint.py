def is_prime_number(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else: 
            return True

number = int(input("Enter number: "))

while number > 0:
    print("Number " + str(number) + " is a prime number: " + str(is_prime_number(number)))
    number = int(input("Enter number: "))
