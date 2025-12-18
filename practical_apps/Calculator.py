#calculator App
print("Welcome to Nethan's Calculator App! Type 'exit' to quit.")

# Quadratic equation solver
def equation_solver():
    try:
        print("Enter the equation in the form of ax^2 + bx + c = 0")
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))

        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + (discriminant ** 0.5)) / (2 * a)
            root2 = (-b - (discriminant ** 0.5)) / (2 * a)
            return (root1, root2)
        elif discriminant == 0:
            root1 = -b / (2 * a)
            return (root1,)
        else:
            return None
    except ValueError:
        print("Invalid input. Please enter numeric values for a, b, and c.")
        return None

last_result = 0
while True:
    user_input = input("> ").strip().lower()
    
    # To exit the calculator
    if user_input == "exit" or user_input == "quit":
        print("Exiting the calculator. Goodbye!")
        break
    
    # To check if it is an expression (which starts with =)
    if user_input.startswith("="):
        expression = user_input[1:].strip()
        expression = expression.replace("ans", str(last_result))

        try:
            result = eval(expression)
            print(f"= {result}")
            last_result = result
        except ZeroDivisionError:
            print("You can't divide by zero.")
        except Exception as e:
            print(f"Error occurred: {e}")
    
    # To check if it is an equation
    elif user_input == "eqn" or user_input == "equation":
        roots = equation_solver()
        if roots is None:
            print("The equation has no real roots.")
        elif len(roots) == 1:
            print(f"The equation has one root: {roots[0]}")
        elif len(roots) == 2:
            print(f"The equation has two roots: {roots[0]} and {roots[1]}")
    
    else:
        print("Invalid input. Please start with '=' or type 'eqn' to solve an equation.")