class Calculator:

    def add(self, a, b): 
        return a + b
         #here self define the currrent object
         
    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print("Addition:", calculator.add(10, 5))
print("Multiplication:", calculator.multiply(10, 5))