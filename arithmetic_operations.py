# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1: The first number (float)
    - num2: The second number (float)
    - operation: The operation to perform (string)
                 Accepts 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - The result of the arithmetic operation (float)
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
        
python main.py
Arithmetic Operations
Enter the first number: 5
Enter the second number: 6
Enter the operation (add, subtract, multiply, divide): add
Result: 11.0

Enter the first number: 10
Enter the second number: 0
Enter the operation (add, subtract, multiply, divide): divide
Result: Error: Division by zero is not allowed.
git add fns_and_dsa/arithmetic_operations.py
git commit -m "Implement basic arithmetic operations"
git push origin main
