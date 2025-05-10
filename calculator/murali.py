def is_prime(number):
  """
  Checks if a given number is a prime number.

  Args:
    number: An integer.

  Returns:
    True if the number is prime, False otherwise.
  """
  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6
  return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")