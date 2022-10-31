#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

#========================================= FUNCTIONS ==========================================================
    
def register_user():

        new_file = open('user.txt','r') 
        
        user_list = []
           
        #enter the new user's username and password
        #enter password twice to confirm password  
        new_user = input("Enter usename: ").lower()
        new_password = input("Enter password: ")
        confirm_new_password = input("Re-enter your password: ")
        
        for user in new_file:
            user_n = user.split(", ")
            user_list.append(user_n[0])
        
        print(user_list)
        
        on = True
        while on:
            if new_user in user_list:
                print("The user name already exists, please choose another name. ")
                new_user = input("Enter another user name: ").lower()
            elif new_user not in user_list:
                print("ok")
                on = False
            
        new_file.close()
        #if name in list: then do stuff  
        
        #if the passwords do not match. re-enter them again
        while confirm_new_password != new_password:
            new_password = input("Enter password: ")
            confirm_new_password = input("Re-enter your password: ")
            if confirm_new_password == new_password:
                break
        
        #write new user to text file    
        with open('user.txt', 'a+') as add_user_file:
            add_user_file.write(f'\n{new_user}, {new_password}') 
     
            
def add_task():
        #get task information   
        add_user = input("Enter username for the task: ").lower()
        task_title = input("Enter the title of the task: ").lower()
        task_description = input("Enter the description of the task: ").lower()
        print("Date example format is: 27 Aug 2022.")
        task_due_date = input("Enter the date for the task to be completed: ").lower()
        #task_completion = input("Is the task completed? Yes/No ").capitalize()
        
        #using the datetime library get today's date.
        task_date = datetime.today()
        #date format
        task_date = task_date.strftime("%d %b %Y")
        
        #write the task information into file
        with open('tasks.txt', 'a') as task_file:
            task_file.write(f"\n{add_user}, {task_title}, {task_description}, {task_date}, {task_due_date}, No")

           
def view_all():
      #open task file and read the whole file  
        with open('tasks.txt', 'r') as task_file:
            file_content = task_file.readlines()
            
            #stores the number of task
            task_number = 0
            #dict variable for all the tasks
            alltasks = {}
            #go through each line in the file
            for line in file_content:
                #split the file with a comma and space after the comma
                add_user, task_title, task_description, task_due_date, task_date, task_completion = line.split(", ") 
                #increment task number by for for every task
                task_number += 1
                alltasks[task_number] = line.strip('\n').split(', ')
                #print task information to be viewed by admin
                print("This is task number: ", task_number)
                print(f'''Added user: {add_user} 
                      Task title: {task_title} 
                      Task description: {task_description}
                      Due date of task: {task_due_date}
                      Completed date: {task_date}
                      Task Completed: {task_completion}''')
 
    
def view_mine():
    #open tasks file to be read
        with open('tasks.txt','r') as task_file:
            #contents = task_file.readlines()
            #stores the number of task
            task_number = 0
            #dict variable for all the tasks
            alltasks = {}
            for line in task_file:
                #split the file with a comma and space after the comma
                add_user, task_title, task_description, task_due_date, task_date, task_completion = line.split(", ") 
                
                #increment task number by for for every task
                task_number += 1
                alltasks[task_number] = line.strip('\n').split(', ')
                #task number to keep track of the tasks
                            
                #print task information to be viewed by user
                if username == add_user:
                    print("This is task number: ", task_number)
                    print(f'''Added user: {add_user} 
                      Task title: {task_title} 
                      Task description: {task_description}
                      Due date of task: {task_due_date}
                      Completed date: {task_date}
                      Task Completed: {task_completion}''')
                    
            task_files(alltasks)

#task fileto allow user to mark whether they have completed a task or not and to edit tasks_counter
def task_files(task_dict):
    
    while True:
        #ask user to enter the task number they want to edit
        select_task = int(input('Enter a task number to select a task or -1 to exit: '))
        
        #if -1 is entered then end the program
        if select_task == -1:
            break
        
        #When another number is entered then give the user an option to either mark task or edit task
        task_choice = input('''Choose an option below
                            ma - Mark a task as completed. 
                            ed - Edit a task.\n''').lower()
        
        
        #if 'ma' is entered change the task completion as 'Yes'
        if task_choice ==  'ma':
            task_dict[select_task][-1] = "Yes"   
        elif task_choice == 'ed':
            edit = input('''Would like to change the username or the date: 
                         u - username
                         dd - Date\n''')
            
            if edit == 'u':
                username_update = input("Enter the new username: ").lower()
                task_dict[select_task][0] = username_update   
            elif edit == 'dd':
                print("The date should be in the format of 07 Feb 2022. ")
                due_date_ed = input("Enter the date you want to change: ")  
                due_date_update = input("Enter the new due date: ")         
        print("\n".join([", ".join(t) for t in task_dict.values()]))
        with open('tasks.txt','w') as op_file:
            op_file.write("\n".join([", ".join(t) for t in task_dict.values()]))

            
def reports():
    
    print("Display stats report:\n")
    
    with open("task_overview.txt", "w+") as task_overview:
        print(task_report())
        
    with open("user_overview.txt", "w+") as user_overview:
        print(user_report())
   

def task_report():
    
    dict_tasks = {}
    completed_tasks = 0
    incompleted_tasks = 0
    overdue_tasks = 0
    num_user_tasks = 0
    
    with open("tasks.txt", "r") as task_file:
        con = task_file.readlines()
        
        for line in con:
            num_user_tasks += 1
            dict_tasks[num_user_tasks] = line.strip('\n').split(', ')
            
    for line in con:
        task = line.strip('\n').split(', ')
        print(task)
        
        if task[-1].strip('\n') =="Yes":
            completed_tasks += 1
        elif task[-1].strip('\n') =="No":
            incompleted_tasks += 1
            
        date_check = datetime.strptime(task[-2], '%d %b %Y')
        
        #check if task is overdue
        if date_check < datetime.today() and 'No' == task[-1].strip('\n'):
            overdue_tasks +=1
        
        #check if dictionary is empty
        if len(dict_tasks) == 0:
            print("Nothing in here. ")
        
        #calculate the percentage
        incomplete_percent = (incompleted_tasks * 100) /  len(dict_tasks)
        overdue_percent   = (overdue_tasks * 100) / len(dict_tasks)
        
        #write to task overdue file
        with open ('task_overview.txt', 'w') as task_view_file:
            task_view_file.write(f"The total number of tasks created is: {len(dict_tasks)}\n")
            task_view_file.write(f"The total number of tasks completed is: {completed_tasks}\n")
            task_view_file.write(f"The total number of incomplete tasks is: {incompleted_tasks}\n")
            task_view_file.write(f"The total number of tasks overdue is: {overdue_tasks: .0f}\n")
            task_view_file.write(f"The percentage of tasks that are incomplete is: {incomplete_percent: .0f}\n")
            task_view_file.write(f"The percentage of tasks that are overdue is: {overdue_percent: .0f}\n")
            

def user_report():
    dict_users = {}
    total_users = 0
    
    with open('user_overview.txt','w', encoding='utf-8') as user_overview:
        #the users are added to count
        for new_user in dict_users:
            if new_user in dict_users or "admin" in dict_users:
                total_users += 1
            else: 
                break
    
    dict_tasks = {}
    number_of_task_users = 0
    total_tasks = 0
    
    with open('tasks.txt','r') as task_file:
        con = task_file.readlines()
        #get the length of the dictionary
        total_tasks = len(dict_tasks)         
        
        with open('user.txt', 'r') as user_file:
            user_con = user_file.readlines()
            #get the total users in dictionary
            number_of_task_users = len(user_con)
            
            for line in user_con:
                user_name = line.split(', ')[0]
                completed_tasks = 0
                incomplete_tasks =0
                overdue_tasks = 0
                specific_user_tasks = 0
                percent_incomplete = 0
                percent_completed = 0
                percent_overdue = 0
                
                
                #for each task in the task file
                for line in con:
                    task = line.strip('\n').split(', ')
                    
                    #validating if user in the user list matches with that specific user's task number
                    if user_name == task[0]:
                        specific_user_tasks += 1
                        
                        #check task completion and add counters
                        if task[-1].strip('\n') =='Yes': 
                            completed_tasks += 1
                        elif task[-1].strip('\n') == 'No': 
                            incomplete_tasks += 1
                        
                        #check if overdue status date_check is datetime object
                        date_check = datetime.strptime(task[-2], '%d %b %Y')
                        
                        if date_check < datetime.today() and 'No' == task[-1].strip('\n'):
                            overdue_tasks += 1
                            
                    #prevent zero value error
                    try:
                        if incomplete_tasks > 0:
                            percent_incomplete = (total_tasks / incomplete_tasks) * 100
                        if completed_tasks > 0:
                            percent_completed = (total_tasks / completed_tasks) * 100
                
                        if overdue_tasks > 0:
                            percent_overdue = (total_tasks / (incomplete_tasks + overdue_tasks)) * 100
                    except ZeroDivisionError:
                        pass        
                #write to user overview file
                with open('user_overview.txt', 'a+') as user_f:
                    #total assigned tasks to user
                    user_f.write(f'Total tasks assigned to user: {total_tasks}\n')
                    # tasks assigned to a user
                    user_f.write(f'Total tasks assigned to {user_name}: {specific_user_tasks}\n')
                    #% of completed tasks
                    user_f.write(f'Total percentage of tasks completed: {percent_completed}\n')
                    #% of incomplete tasks
                    user_f.write(f'Total percentage of tasks not completed: {percent_incomplete}\n')
                    #% of overdue tasks
                    user_f.write(f'Total percentage of tasks overdue: {percent_overdue}\n')


def display_num():
    #store the counter for tasks and users
        tasks_counter = 0
        users_counter = 0

        #open tasks file to keep count of the tasks
        with open('tasks.txt', 'r+') as task_file:
            
            for line in task_file:
                
                #add 1 each time a new task is added
                tasks_counter += 1
            #print the counter
            print(f"The total number of tasks are {tasks_counter}")
            
        #open user file to keep count of the tasks   
        with open('user.txt', 'r+') as user_file:
            
            for line in user_file: 
                #add 1 each time a new user is added
                users_counter += 1
                
            #print the counter
            print(f"The total number of users are {users_counter}\n")
                                        
        
def menu():
    #if username is admin present this menu
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == 'admin':
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display stats, number of tasks and users
    d  - View number of tasks and users
    e - Exit
    : ''').lower()
    
    #if username is not admin present this menu
    else:
           menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

    #if 'r' is selected, to register a user, only admin can register a new user
    if menu == 'r':        
        register_user()    #call the register function
        
    #add user option  
    elif menu == 'a':  
        add_task()         #call the add usre function

    #view all tasks option
    elif menu == 'va':
        view_all()         #call the view_all function

    #view my tasks option
    elif menu == 'vm':
        view_mine()        #call the view_mine function
    
    #display all stats option
    elif menu == 'ds':
        reports()          #call the reports function
    
    #generate reports function
    elif menu == 'gr':
        task_report()      #call the task report function
        user_report()      #call the user report function
        
    #view number of tasks and users 
    elif menu == 'd':
        display_num()      #call the display numbers function
    
    #exit program
    elif menu == 'e':
        #print a message and terminate the program
        print('Goodbye!!!')
        exit()

    else:
        #print message so user can input again
        print("You have made a wrong choice, Please Try again")     
        
#====================================================== END OF FUNCTIONS =======================================================================
            
#====Login Section====

#open and read the user file
read_file = open('user.txt', 'r')
    
#create empty lists to store users and user password.
user_list = []
password_list = []

#remove newlines and sperate the username and password where there is ', '
#store them in a list
#store username in index 0 and password in index 1
for data in read_file:
    data_list = data.strip('\n').split(', ')
    user_list.append(data_list[0])
    password_list.append(data_list[1].strip("\n"))

#close the file
read_file.close()

#login details
#ask user to login
username = input("Enter username: ").lower()

#check if user name already exists
#if it does not display an error message and request they re-enter their username
while username not in user_list:
    print("Error, username not found, please enter again.")
    username = input("Enter username: ").lower()

#Once username is valid ask user to enter password
password = input("Enter password: ")

#print(password_list[user_list.index(username)])
#if password does not match username password index
#ask the user to re-enter password
while not (password_list[user_list.index(username)] ==password):
    print("Error, incorrect password.")
    password = input("Enter password: ")

#once user is logged in print success message.
print("You are logged in, welcome.")


while True:
    menu()