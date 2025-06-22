# Importing argparse for parsing command-line arguments
import argparse

# Conversion function: Celsius → Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Conversion function: Fahrenheit → Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Conversion function: Celsius → Kelvin
def celsius_to_kelvin(c):
    return c + 273.15

# Conversion function: Kelvin → Celsius
def kelvin_to_celsius(k):
    return k - 273.15

# Conversion function: Fahrenheit → Kelvin (via Celsius)
def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

# Conversion function: Kelvin → Fahrenheit (via Celsius)
def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

# Main function to handle CLI logic
def main():
    # Setting up argument parser with a description
    parser = argparse.ArgumentParser(description="Convert temperature between Celsius, Fahrenheit, and Kelvin.")

    # Adding required positional arguments:
    # from_unit: the unit to convert from (C/F/K)
    # to_unit: the unit to convert to (C/F/K)
    # value: the numeric temperature value to convert
    parser.add_argument("from_unit", choices=["C", "F", "K"], help="Unit to convert from: C, F, or K.")
    parser.add_argument("to_unit", choices=["C", "F", "K"], help="Unit to convert to: C, F, or K.")
    parser.add_argument("value", type=float, help="Temperature value to convert.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Extracting the values from arguments and standardizing to uppercase
    f, t, v = args.from_unit.upper(), args.to_unit.upper(), args.value

    # If the from and to units are the same, no conversion needed
    if f == t:
        print(f"No conversion needed. {v}°{f} = {v}°{t}")
    
    # Handling all valid conversion cases
    elif f == "C" and t == "F":
        print(f"{v}°C = {celsius_to_fahrenheit(v):.2f}°F")
    elif f == "F" and t == "C":
        print(f"{v}°F = {fahrenheit_to_celsius(v):.2f}°C")
    elif f == "C" and t == "K":
        print(f"{v}°C = {celsius_to_kelvin(v):.2f}K")
    elif f == "K" and t == "C":
        print(f"{v}K = {kelvin_to_celsius(v):.2f}°C")
    elif f == "F" and t == "K":
        print(f"{v}°F = {fahrenheit_to_kelvin(v):.2f}K")
    elif f == "K" and t == "F":
        print(f"{v}K = {kelvin_to_fahrenheit(v):.2f}°F")
    
    # Fallback in case of an unhandled case (though argparse ensures valid choices)
    else:
        print("Invalid conversion.")

# Entry point: ensures main() is called when script is run directly
if __name__ == "__main__":
    main()
