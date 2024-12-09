import os

def Courses():
    print("--------------------------COURSE--------------------------------")
    print("Bachelor of Science in Computer technology")
    print("Bachelor of Science in Office Administration")
    print("Bachelor of Science in Business Administration")
    print("Bachelor of Criminology")
    print("Bachelor of Secondary Education")
    print("--------------------------COURSE--------------------------------")

def create_student():
    num_students = int(input("How many students would you like to register? "))
    with open("file.txt", "a") as file:
        for _ in range(num_students):
            student_name = input("Enter the name of the student: ")
            file.write(student_name + "\n")
    print(f"{num_students} student(s) have been registered successfully!")  

def read_students():
    if os.path.exists("file.txt"):
        with open("file.txt", "r") as file:
            students = file.readlines()
        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start = 1):
                print(f"{idx}. {student.strip()}")
        else:
            print("No students are registered yet.")
    else:
        print("No student data file found.")

def update_student():
    if os.path.exists("file.txt"):
        with open("file.txt", "r") as file:
            students = file.readlines()
        
        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                print(f"{idx}. {student.strip()}")
            
            student_idx = int(input("\nEnter the number of the student you want to update: ")) - 1
            if 0 <= student_idx < len(students):
                new_name = input("Enter the new name for the student: ")
                students[student_idx] = new_name + "\n"
                with open("file.txt", "w") as file:
                    file.writelines(students)
                print("Student name has been updated.")
            else:
                print("Invalid student number.")
        else:
            print("No students to update.")
    else:
        print("No student data file found.")

def delete_student():
    if os.path.exists("file.txt"):
        with open("file.txt", "r") as file:
            students = file.readlines()
        
        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                print(f"{idx}. {student.strip()}")
            
            student_idx = int(input("\nEnter the number of the student you want to delete: ")) - 1
            if 0 <= student_idx < len(students):
                deleted_student = students.pop(student_idx)
                with open("file.txt", "w") as file:
                    file.writelines(students)
                print(f"Student '{deleted_student.strip()}' has been deleted.")
            else:
                print("Invalid student number.")
        else:
            print("No students to delete.")
    else:
        print("No student data file found.")
        

def search_student():
        if os.path.exists("file.txt"):
            with open("file.txt", "r") as file:
                students = file.readlines()

        if students:
            search_name = input("Enter the name of the student to search for: ").strip()
            found_students = [student.strip() for student in students if search_name.lower() in student.lower()]
            
            if found_students:
                print("\nSearch Results:")
                for idx, student in enumerate(found_students, start=1):
                    print(f"{idx}. {student}")
            else:
                print(f"No students found with the name '{search_name}'.")
        else:
                print("No students are registered yet.")
    

def menu():
    while True:
        print("\nSchool Management Database 2024")
        print("1. View Courses")
        print("2. Register Students ")
        print("3. View Registered Students ")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            Courses()
        elif choice == '2':
            create_student()
        elif choice == '3':
            read_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            search_student()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    menu()