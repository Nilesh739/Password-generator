import random
import string

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
      length: The desired length of the password.

  Returns:
      A random password string.
  """
  # Define character sets for different categories
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  # Combine all character sets
  all_characters = lowercase + uppercase + digits + punctuation

  # Ensure at least one character from each category
  password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(punctuation)

  # Fill the remaining slots with random characters from the combined set
  password += ''.join(random.choices(all_characters, k=length - 4))

  # Shuffle the characters for better randomness
  random.shuffle(list(password))

  # Return the generated password
  return ''.join(password)

def main():
  """
  Prompts user for password length and count, generates passwords, and displays them.
  """
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters. Please try again.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number for password length.")

  while True:
    try:
      count = int(input("Enter the number of passwords to generate: "))
      if count <= 0:
        print("Number of passwords cannot be zero or negative. Please try again.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number for the number of passwords.")

  # Generate and display passwords
  for _ in range(count):
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
  main()
