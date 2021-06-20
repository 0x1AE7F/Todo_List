#!/usr/bin/env python3
from os import replace
import time

print("Welcome to your TODO List")
time.sleep(1)
print("Commands:")
time.sleep(0.25)
print("1: Show Pending")
time.sleep(0.25)
print("2: Add to List")
time.sleep(0.25)
print("3: Remove from List")
selection = input(": ")

def todo_show():

    #getting list
    f = open("./list.txt", 'r')

    #reaing list
    todolist = f.read()
    print(todolist)
    f.close()


def todo_new():

    #getting list
    f = open("./list.txt", 'a')

    new_todo_task = input("Name of new Task\n : ")

    #writing task to newline in file
    f.write(new_todo_task + "\n")
    f.close()

def todo_remove():

    #getting list
    f = open("./list.txt", "r+")


    lines = f.read()


    #putting contents of file in a list variable
    todo_list = [lines]
    f.close()
    todo_list = str(todo_list)

    #deleting unused characters
    todo_list = todo_list.replace("n", "\n")
    todo_list = todo_list.replace('[', "")
    todo_list = todo_list.replace(']', "")
    todo_list = todo_list.replace("'", "")

    todo_remove_input = input("TODO Name\n: ")
    
    todo_list.replace(todo_remove_input, " ")
    print(todo_list)


#deciding task on selecion

if selection == "1":
    todo_show()
elif selection == "2":
    todo_new()
elif selection == "3":
    # Showing the todo list
    todo_show()
    todo_remove()

input()