class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a + (-b)

    def multiply(self, a, b):
        # Handle negative numbers
        negative_result = False
        if a < 0:
            a = -a
            negative_result = not negative_result
        if b < 0:
            b = -b
            negative_result = not negative_result
        
        result = 0
        for _ in range(b):
            result = self.add(result, a)
        
        return -result if negative_result else result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        # Handle negative numbers
        negative_result = False
        if a < 0:
            a = -a
            negative_result = not negative_result
        if b < 0:
            b = -b
            negative_result = not negative_result
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)
        
        return -result if negative_result else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        
        # Handle negative numbers
        negative_result = a < 0
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        
        while a >= b:
            a = self.subtract(a, b)
        
        return -a if negative_result else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(-5, 1))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(1, 0))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))