# User Interface (UI):

#     Create a command-line interface (CLI) for the To-Do List Application.

#     Display a welcoming message and a menu with the following options:

#             Welcome to the To-Do List App!

#             Menu:
#             1. Add a task
#             2. View tasks
#             3. Mark a task as complete
#             4. Delete a task
#             5. Quit

# To-Do List Features:

#     Implement the following features for the To-Do List:

#         Adding a task.

#         Viewing the list of tasks 

#         Marking a task as complete. (Bonus) (Hint: Use string manipulation to add "X" to the end of a task)

#         Deleting a task.

#         Quitting the application.

# User Interaction:

#     Allow users to interact with the application by selecting menu options using input().

#     Implement input validation to handle unexpected user input gracefully. (BONUS)

# Error Handling:

#     Implement error handling where necessary using try, except, else, and finally blocks to handle potential issues.

# Code Organization:

#     Organize your code into functions to promote modularity and readability.

#     Use meaningful function names with appropriate comments.

# Testing and Debugging:

#     Thoroughly test your application to identify and fix any bugs.

#     Consider edge cases, such as empty task lists or incorrect user input.

# Optional Features (Bonus):

#     If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

# GitHub Repository:

#     Create a GitHub repository for your project.

#     Commit your code to the repository regularly.

#     Include a link to your GitHub repository in your project documentation.

def add_todo (to_do_list):
        to_do = input("Please add a chore to your To-Do List: ")
        to_do = to_do.capitalize()
        if to_do in to_do_list:
             print("That chore is already on your todo list")
        else:
            to_do_list.append(to_do)

    
def remove_todo(to_do_list):
    # take an item via user input and try to remove it from the list
    try:
        to_do = input("What item would you like to remove? ")
        to_do = to_do.capitalize()
        to_do_list.remove(to_do)
    except: 
        print(f"{to_do} does not exist. You can't remove things that don't exist!")

def mark_todo_complete(to_do_list):
        completed_todo = input("Which chore have you completed? ")
        completed_todo = completed_todo.capitalize()
        for i, chore in enumerate(to_do_list):
                if chore == completed_todo:
                        to_do_list[i] += " (Done-zo)"
                        
    

to_do_list= []

def main(to_do_list):
    while True:
            print("""            
Welcome to the To-Do List App!

Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
              
              """)
            try:
                menu_item = int(input("What would you like to do? Please input a number 1-5:  " ))

                if menu_item == 1:
                        add_todo(to_do_list)
                elif menu_item == 2:
                        for item in to_do_list:
                                print(item)
                        pass
                elif menu_item == 3:
                        mark_todo_complete(to_do_list)
                        print(to_do_list)
                elif menu_item == 4:
                        remove_todo(to_do_list)
                elif menu_item == 5:
                        print(to_do_list)
                        break
                else:
                        print("That's not between 1-5! Try again.")
                   
            except ValueError:
                print("That is not a number! ")

         

main(to_do_list)
