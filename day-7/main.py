# def greet():
#   print("Hello")
#   print("how do you do?")
#   print("Isn't the weather nice today?")
  
# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
  
# greet_with_name("lucas")

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}")
  
# greet_with(location="Nowhere", name="jane")

def prime_checker(number):
    is_prime = True
    for i in range(2 , number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a priem number.")


n = int(input("Check this number: "))
prime_checker(number=n)
