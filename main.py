import os

running = True

while running:
    print("Hello there, this is a project done By Ivan and Abhishek")
    action = str(input("Do you want to continue? [Y/N] :")).lower()
    if action == 'y' or action == 'yes':
        print("Ok, Which mode you want to continue?")
        print("To continue with Radius, Press 'r' or Type 'Radius'")
        print("To continue with Diameter, Press 'd' or Type 'Diameter'")
        print("To continue with Area, Press 'a' or Type 'Area'")
        print("To continue with Perimeter, Press 'p' or Type 'Perimeter'")
        print("To Quit, Press 'q' or 'n' or Type 'Quit' or 'No'")
        command = str(input("Command: ")).lower()
        if command == 'r' or command == 'radius':
            c = input("Enter the radius of the circle.")
            os.system(f'python app.py -r {c}')
            running = False
        elif command == 'd' or command == 'diameter':
            c = input("Enter the diameter of the circle.")
            os.system(f'python app.py -d {c}')
            running = False
        elif command == 'a' or command == 'area':
            c = input("Enter the area of the circle.")
            os.system(f'python app.py -a {c}')
            running = False
        elif command == 'p' or command == 'perimeter':
            c = input("Enter the perimeter of the circle.")
            os.system(f'python app.py -p {c}')
            running = False
        elif command == 'q' or command == 'quit':
            print("Closing out of the app...")
            running = False
        else:
            print('wrong command')
            print("Closing out of the app...")
            running = False
    if action == 'n' or action == 'no':
        print("Closing out of the app...")
        running = False