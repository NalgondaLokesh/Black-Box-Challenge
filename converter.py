import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def main():
    parser = argparse.ArgumentParser(description="Convert temperature between Celsius, Fahrenheit, and Kelvin.")

    parser.add_argument("from_unit", choices=["C", "F", "K"], help="Unit to convert from: C, F, or K.")
    parser.add_argument("to_unit", choices=["C", "F", "K"], help="Unit to convert to: C, F, or K.")
    parser.add_argument("value", type=float, help="Temperature value to convert.")

    args = parser.parse_args()

    f, t, v = args.from_unit.upper(), args.to_unit.upper(), args.value

    if f == t:
        print(f"No conversion needed. {v}°{f} = {v}°{t}")
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
    else:
        print("Invalid conversion.")

if __name__ == "__main__":
    main()
