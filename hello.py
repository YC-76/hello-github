name = input("What is your name? ")

while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Error: Please enter a valid number for your age.")

if age >= 65:
    print(f"Hello {name}, you are a Senior.")
elif age >= 18:
    print(f"Hello {name}, you are an Adult.")
else:
    print(f"Hello {name}, you are a Minor.")