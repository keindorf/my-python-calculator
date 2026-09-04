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
print("Please enter two numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate results
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Show results with fun mode styling
if mode == "2":
    print(f"\n🌟 Results for {num1} and {num2}: 🌟")
    print("*" * 30)
    print(f"✨ {num1} + {num2} = {addition}")
    print(f"⭐ {num1} - {num2} = {subtraction}")
    print(f"🎯 {num1} × {num2} = {multiplication}")
    print(f"🚀 {num1} ÷ {num2} = {division}")
    print("*" * 30)

    # Fun messages based on numbers
    if num1 == num2:
        print("🔥 Wow! You entered the same number twice!")
    elif addition > 100:
        print("💯 That's a big sum!")
    else:
        print("📊 Great calculations!")
else:
    print(f"\nResults for {num1} and {num2}:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} × {num2} = {multiplication}")
    print(f"{num1} ÷ {num2} = {division}")

print("\nThanks for using the calculator!")