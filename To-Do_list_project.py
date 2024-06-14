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
    to_do_list.append(to_do)
    
def remove_todo(to_do_list):
    # take an item via user input and try to remove it from the list
    try:
        to_do = input("What item would you like to remove? ")
        to_do_list.remove(to_do)
    # removing an item from a list that doesnt exist throws an error
    # handle trying to remove something that we havent added to our to_do_list yet
    except: # raise a ValueError for something that doesn't exist inside the list.
        print(f"{to_do} does not exist. You can't remove things that don't exist!")



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
        
        menu_item = int(input("What would you like to do?: " ))

        if menu_item == 1:
            add_todo(to_do_list)
        elif menu_item == 2:
            remove_todo(to_do_list)

            





    
  
main(to_do_list)
