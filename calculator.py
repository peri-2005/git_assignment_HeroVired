You said: You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.  a. Create a repository name: git_assignment_HeroVired  b. Create a ‘dev’ branch and add this code.Here is the step-by-step guide to setting up your repository and adding the square root feature to the dev branch for CalculatorPlus.1. Initialize the RepositoryFirst, create your local directory, initialize Git, and create the required repository name.bash# Create the project directory
mkdir git_assignment_HeroVired
cd git_assignment_HeroVired

# Initialize a new Git repository
git init
Use code with caution.2. Create the Base ApplicationCreate the core Python file named calculator.py with the basic arithmetic functions.python# calculator.py
import math

class CalculatorPlus:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
Use code with caution.Commit this initial application to your default branch (usually main or master):bashgit add calculator.py
git commit -m "Initial commit: Add basic arithmetic operations"
Use code with caution.3. Create the dev BranchNow, create and switch to the dev branch where you will implement the new square root feature.bashgit checkout -b dev
Use code with caution.4. Implement the Square Root FeatureUpdate calculator.py inside your dev branch to include the square root function.python# calculator.py (Updated)
import math

class CalculatorPlus:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    # New feature added in dev branch
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(a)