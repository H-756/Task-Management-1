#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
# Here i created a list that adds each line read from the user file.
user_accounts = []
with open("user.txt", "r") as f:
    user_credentials = f.readlines()
    for line in user_credentials:
        user_accounts.append(line.strip().split(", "))

# Using a bolean i was able to ask user to log in and validate user credentials against the user file using a for loop combined with an indented if statement.
user_not_logged_in = True

while user_not_logged_in:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    for user in user_accounts:
        stored_username = user[0]
        stored_password = user[1]

        if stored_username == username and stored_password == password:
            user_not_logged_in = False
            print("You have succesfully logged in!")
            break

    if user_not_logged_in:
        print("You have entered invalid credentials!")


while True:
    # Presenting the menu to the user and 
    # Making sure that the user input is coneverted to lower case.
    # For task 2 i ensured to create a new menu using an if function to display it for the admin only!
    if username == "admin":                                                   
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
st - View Stats
e - Exit
: ''').lower()
    
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# For task 2 i have formatted so only admin can register a new user.
# i used a nested if statement to confirm passwords and then added the new details to the user file.
    if menu == 'r':

        if username == "admin":
            new_username = input("Please input a new username: ")
            new_password = input("Please input a new password: ")
            confirm_new_password = input("Confrim new password: ")
            if confirm_new_password == new_password:
                with open("user.txt", "a+") as f1:
                    f1.write("\n" + new_username + ", " + new_password)

# Appropriate error messages was created for each scenario.
            else:
                print("The password was not correctly confirmed. Please ensure that the password and confirmation match exactly.")
        else:
            print("Only admin can register a new user")

    elif menu == 'a':

# Appropriate varibales where created to obtain all the information needed to add a new task and ive added this new information to the task file in the same order as previous tasks.
        added_username = input("Please enter the username of the person this task will be assigned to: ")
        task = input("Enter the title of the task: ")
        task_description = input("Please describe the task assigned: ")
        date_assigned = input("Enter the current date: ")
        due_date = input("Enter the due date of the tast (e.g. 19 jan 2023): ")
        completion = input("Is the task completed? (enter 'yes' or 'no')")

        with open("tasks.txt", "a+") as f2:
            f2.write(f"\n{added_username}, {task}, {task_description}, {date_assigned}, {due_date}, {completion}")


    elif menu == 'va':

 # I have created an empty list that will be used to append all the tasks to it to form a nested list.
 # This will allow me to print the positions freely to achieve the desired output.      
        all_tasks_list = []

        with open("tasks.txt", "r") as f2:
            all_tasks = f2.readlines()
            for line in all_tasks:
                all_tasks_list.append(line.strip().split(", "))
            for list in all_tasks_list:
                print('-' * 200)
                print("\nTask:" + "\t\t\t\t" + "".join(list[1]))
                print("Assigned to:" + "\t\t\t" + "".join(list[0]))
                print("Date assigned:" + "\t\t\t" + "".join(list[3]))
                print("Due date:" + "\t\t\t" + "".join(list[4]))
                print("Task complete?" + "\t\t\t" + "".join(list[5]))
                print("Task description:" + "\t\t" + "".join(list[2]) + "\n")
            print('-' * 200)
            
     
    elif menu == 'vm':
       
# A similiar processed was used here as "va" however i did use a for loop to check if the user has a task, by checking the username against the 0 position of every line in the tasks file.
# A bolean was used to produce to an no task message if the user had no tasks.
        all_tasks_list = []
        user_has_task = False

        with open("tasks.txt", "r") as f2:
            specific_task = f2.readlines()
            for line in specific_task:
                all_tasks_list.append(line.strip().split(", "))
            for list in all_tasks_list:
                if list[0] == username:
                    user_has_task = True
                    print("\nTask:" + "\t\t\t\t" + "".join(list[1]))
                    print("Assigned to:" + "\t\t\t" + "".join(list[0]))
                    print("Date assigned:" + "\t\t\t" + "".join(list[3]))
                    print("Due date:" + "\t\t\t" + "".join(list[4]))
                    print("Task complete?" + "\t\t\t" + "".join(list[5]))
                    print("Task description:" + "\t\t" + "".join(list[2]))
            if not user_has_task:
                print("You have no tasks")

# For task 2 i read from both: user and tasks files to produce the stats desired.
# Of course i added the condition so only  the admin can use the st menu.               
    elif menu == "st" and username == "admin":
        with open("tasks.txt", "r") as f1:
            number_of_tasks = len(f1.readlines())
        with open("user.txt", "r") as f1:
            number_of_users = len(f1.readlines())
        print("\nThe number of tasks are: " + str(number_of_tasks))
        print("The number of users are: " + str(number_of_users) + "\n")


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")