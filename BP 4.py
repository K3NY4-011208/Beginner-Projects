print("Temperature Converter")

choice = input("Convert from (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == "C":
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result}°F")
elif choice == "F":
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result}°C")
else:
    print("Invalid choice.")
