# Simple Calculator Program
# Created for Git/GitHub Learning

print("=== Simple Calculator ===")
print("Choose your mode:")
print("1. Normal Calculator")
print("2. Fun Calculator")

mode = input("Enter your choice (1 or 2): ")

if mode == "2":
    print("\n🎉 FUN CALCULATOR MODE! 🎉")
    print("=" * 30)
else:
    print("\n=== Normal Calculator Mode ===")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate results
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Show results
print(f"\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(f"{num1} ÷ {num2} = {division}")