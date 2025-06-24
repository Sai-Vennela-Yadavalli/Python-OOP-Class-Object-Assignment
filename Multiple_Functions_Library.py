class Multiple_Functions():
    
    def Subfields():
        Lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in Lists:
            print(i)  

    def Odd_Even_check():
        num = int(input("Enter the number"))
        if (num%2) ==0:
            print(num, "is a Even Number")
            message = "Even Number"
        else:
            print(num, "is a Odd Number")
            message = "Odd Number"
        return message

    def eligible():
        gender = input("Your Gender")
        age = int(input("Your Age"))
    
        if gender == "Male" and age >=21:
            print("You are Eligible")
            message = "YOU ARE ELIGIBLE"
            
        elif gender == "Female" and age >=18:
            print("You are Eligible")
            message = "YOU ARE ELIGIBLE"
        else:
            print("You are NOT ELIGIBLE")
            message = "YOU ARE NOT ELIGIBLE"
    
        return message

    def percentage():
        marks1 = int(input("Subject1 = "))
        marks2 = int(input("Subject2 = "))
        marks3 = int(input("Subject3 = "))
        marks4 = int(input("Subject4 = "))
        marks5 = int(input("Subject5 = "))
    
        Total = marks1 + marks2 + marks3 + marks4 + marks5
        print("Total = ", Total)
        Percentage = (Total/5)
        print("Percentage = ", Percentage)

    def triangle():
        height = int(input("Height = "))
        breadth = int(input("Breadth = "))
    
        Area = (height*breadth)/2
        print("Area of Triangle = ", Area)
    
        height1 = int(input("Height1 = "))
        height2 = int(input("Height2 = "))
        breadth1 = int(input("Breadth1 = "))
        Perimeter = height1 + height2 + breadth1
        print("Perimeter of a Triangle = ", Perimeter)
