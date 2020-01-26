import sys
print("", "Formula Screen \n")
print("", "[1] Gravity Formula -   Force of Gravity =  (Gravitational Constant x Mass of First object x Mass of Second Object) / Distance^2 \n")
print("", "[2] Thermal Convection -  Rate of Heat Transfer = (Convection Coefficient x Surface Area of Heat Transfer x Temperature Difference)\n")
print("", "[Q] Quit \n")

choice = input("Please choose an Equation! ")
    
while choice == "1" or choice == "2": 

    if choice == "1":
        print("", "This is the Gravity Formula. Which variable will we be looking for?\n")
        print("", "[G] Force of Gravity \n") 
        print("", "[M] Mass of First Object \n")
        print("", "[N] Mass of Second Object \n")
        print("", "[R] Distance between the two objects \n")
        print("", "[Q] Back \n")
        action = input("Find which Variable? ")

        if action == 'G':
            print("Solving for the Force of Gravity. Please enter the remaining values. \n")
            first_Variable = input("Mass of the First Object: ")
            second_Variable = input("Mass of the Second Object: ")
            third_Variable = input("Distance between the two objects: ")
            ans = int(first_Variable) * int(second_Variable) *  0.0000000000667 / int(third_Variable) * int(third_Variable)
            print("The Force of Gravity is: ", ans)
        
    
        elif action == "M":
            print("Solving for the Mass of the First Object. Please enter the remaining values. \n")
            first_Variable = input("Force of Gravity: ")
            second_Variable = input("Mass of the Second Object: ")
            third_Variable = input("Distance between the two objects: ")
            ans = int(first_Variable) * int(third_Variable) * int(third_Variable) / 0.0000000000667 * int(second_Variable)
            print("The Mass of the First object is: ", ans)

        elif action == 'N':
            print("Solving for the Mass of the Second object. Please enter the remaining values. \n")
            first_Variable = input("Force of Gravity: ")
            second_Variable = input("Mass of the First object: ")
            third_Variable = input("Distance between the two objects: ")
            ans = int(first_Variable) * int(third_Variable) * int(third_Variable) / 0.0000000000667 * int(second_Variable)
            print("The Mass of the Second object is: ", ans)

        elif action == 'Q':
            print("", "Formula Screen \n")
            print("", "[1] Gravity Formula -   Force of Gravity =  (Gravitational Constant x Mass of First object x Mass of Second Object) / Distance^2 \n")
            print("", "[2] Thermal Convection -  Rate of Heat Transfer = (Convection Coefficient x Surface Area of Heat Transfer x Temperature Difference)\n")
            print("", "[Q] Quit \n")
            choice = input()
      

    

    elif choice == "2":
        print("", "This is the Thermal Convection Formula. Which variable will we be looking for?\n")
        print("", "[R] Rate of Heat Transfer \n")
        print("", "[H] Convective Heat Transfer Coefficient \n")
        print("", "[A] Surface Area of Heat Transfer \n")
        print("", "[T] Temperature Difference between the surface and fluid \n")
        print("", "[Q] Back \n")
        action = input("Find which Variable? ")

        if action == 'R':
            print("Solving for Heat transferred per unit. Please enter the remaining values \n")
            first_Variable = input("Value for Heat transfer Coefficient (h): ")
            second_Variable = input("Value for Heat transfer area of the surface (A): ")
            third_Variable = input("Value for Temperature difference between the surface and fluid (d): ")
            ans = int(first_Variable) * int(second_Variable) * int(third_Variable)
            print(ans)

        elif action == 'H':
            print("Solving for the Confection Coefficient. Please enter the remaining values. \n")
            first_Variable = input("Value for Heat transfer Coefficient (h): ")
            second_Variable = input("Value for Heat transfer area of the surface (A): ")
            third_Variable = input("Value for Temperature difference between the surface and the bulk fluid (d): ")
            ans = int(first_Variable) * int(second_Variable) * int(third_Variable)
            print(ans)

        elif action == 'A':
            print("Solving for the Area of the surface. Please enter the remaining values. \n")
            first_Variable = input("Value for Heat transfer Coefficient (h): ")
            second_Variable = input("Value for Heat transfer area of the surface (A): ")
            third_Variable = input("Value for Temperature difference between the surface and the bulk fluid (d): ")
            ans = int(first_Variable) * int(second_Variable) * int(third_Variable)
            print(ans)

        elif action == 'T':
            print("Solving for the Temperature Difference. Please enter the remaining values. \n")
            first_Variable = input("Value for Heat transfer Coefficient (h): ")
            second_Variable = input("Value for Heat transfer area of the surface (A): ")
            third_Variable = input("Value for Temperature difference between the surface and the bulk fluid (d): ")
            ans = int(first_Variable) * int(second_Variable) * int(third_Variable)
            print(ans)

        elif action == "Q":
            print("", "Formula Screen \n")
            print("", "[1] Gravity Formula -   Force of Gravity =  (Gravitational Constant x Mass of First object x Mass of Second Object) / Distance^2 \n")
            print("", "[2] Thermal Convection -  Rate of Heat Transfer = (Convection Coefficient x Surface Area of Heat Transfer x Temperature Difference)\n")
            print("", "[Q] Quit \n")
            choice = input()
