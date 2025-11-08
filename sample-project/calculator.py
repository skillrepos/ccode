# Sample Python calculator with intentional bugs

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug: No zero division check
    return a / b

def calculate_average(numbers):
    # Bug: Doesn't handle empty list
    total = sum(numbers)
    return total / len(numbers)

if __name__ == "__main__":
    print("Calculator module loaded")
    # Test with problematic input
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
