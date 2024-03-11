# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: Mohammad Ammar Bharmal, 03/10/2024, Created Script
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

print("""
     Welcome to Assignment 04: Course Registration Program!
        This program demonstrates the use of lists and
            files using the PyCharm IDE in Python
      """
      )

# Define the Data Constants
MENU: str = """
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""

# defining data constant with datatype and setting it with the csv file name
FILE_NAME: str
FILE_NAME = "Enrollments.csv"  # assigning value to the constant

# Define the Data Variables
# defining data constant with datatype and setting it as empty string
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
menu_choice: str

# assigning None to the constant
file_obj = None

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        print(csv_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "w")
        file_obj.write("First name,Last name,Course Name\n")
        file_obj.write(csv_data)
        file_obj.close()
        print(
            f"You have registered {student_first_name} {student_last_name} for {course_name}."
        )
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
