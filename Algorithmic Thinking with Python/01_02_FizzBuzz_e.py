
# Multiple of 3 -- Fizz
# Multiple of 5 -- Buzz
# Multiple of 3 and 5 -- FizzBuzz

for i in range(1,1000):
    if i%3==0 and i%5==0:
        print("FizzBuzz", end=", ")
    elif i%3==0:
        print("Fizz", end=", ")
    elif i%5==0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")