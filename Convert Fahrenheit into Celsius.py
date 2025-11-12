# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage
f = 98.6
result = fahrenheit_to_celsius(f)
print("Temperature in Celsius:", result)
