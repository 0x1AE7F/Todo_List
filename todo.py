#!/usr/bin/env python3
from os import replace
import time


def todo_show():

    # getting list
    f = open("./list.txt", 'r')

    # reaing list
    todolist = f.read()
    print(todolist)
    f.close()


def todo_new():

    # getting list
    f = open("./list.txt", 'a')

    new_todo_task = input("Name of new Task\n : ")

    # writing task to newline in file
    f.write(new_todo_task + "\n")
    f.close()


def todo_remove():
    # getting list
    f = open("./list.txt", "r+")

    # lines = f.read()

    # putting contents of file in a list 
    todo_list = []
    for line in f:
        line = line.replace('\n', '')

        todo_list.append(line)
    f.close()
    
    id = 0
    for todo in todo_list:
        print(f"{id}. {todo}")
        id += 1

    todo_remove_index = int(input("TODO ID: "))
    todo_list.pop(todo_remove_index)    
    
    todo_list_str = '\n'.join(todo_list)
    f = open('./list.txt', 'w')
    f.write(todo_list_str)
    print("Successfully writed file!")
    f.close()

todo_remove()
# deciding task on selecion

def main():
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
    if selection == "1":
        todo_show()
    elif selection == "2":
        todo_new()
    elif selection == "3":
        # Showing the todo list
        todo_show()
        todo_remove()

input()
