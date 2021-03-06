#!/usr/bin/env python3
from os import replace
import time
import subprocess
import sys

def todo_show():

    # getting list
    f = open("./list.txt", 'r')

    # reaing list
    todo_list = f.read()
    print(todo_list)
    f.close()


def todo_new():

    # getting list
    f = open("./list.txt", 'a')

    new_todo_task = input("Name of new Task\n: ")

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

    todo_remove_index = int(input("TODO ID\n: "))
    todo_list.pop(todo_remove_index)    
    
    todo_list_str = '\n'.join(todo_list)
    f = open('./list.txt', 'w')
    f.write(todo_list_str)
    print("Successfully writed file!")
    f.close()

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
    time.sleep(0.25)
    print("q: Quit")
    selection = input(": ")

    if selection == "1":
        todo_show()
    elif selection == "2":
        todo_new()
    elif selection == "3":
        todo_remove()
    elif selection == "q":
        exit()

def clear_screen():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        subprocess.run(['clear'])
    # elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    #     subprocess.run(['cls'])

main()
while input("Anything else? [y/N]\n: ") == "y":
    clear_screen()
    
    main()
