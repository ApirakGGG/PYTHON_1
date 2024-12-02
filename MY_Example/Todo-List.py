import tkinter as tk 
from tkinter import messagebox

#function for todo List
def add_task():
    task = task_entry.get(); #ดึงข้อความจากInput Field
    if task != "" :
        task_listbox.insert(tk.END , task) #insert task in listbox
        task_entry.delete(0 , tk.END) #delete massage from task input
    else :
        messagebox.showwarning("Warming", "You must enter the task")

#function for delete task in todo list
def delete_task() :
    try :
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except :  
        messagebox.showwarning("Warning", "you must select a task to delete")

#function for clear all task in todo list
def clear_task() :
    task_listbox.delete(0, tk.END)

#functoin to exist program
def exit_button() :
    root.quit()

#create tkinter window
root = tk.Tk()
root.title("TODO LIST Application")
root.geometry("900x900")


#create input field
task_entry = tk.Entry(root , width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root , text="Add Task" , width=30 ,background="yellow" , command=add_task) 
add_task_button.pack(pady=5)

#create list for show position todo list 
task_listbox = tk.Listbox(root , width=100 , height= 10)
task_listbox.pack(pady=10)

#create manage button for listbox 
delete_button =tk.Button(root, text="Delete Task" , width=30 , command=delete_task)
delete_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear Task", width=30 , command=clear_task)
clear_button.pack(pady=5)

exits_button = tk.Button(root , text="Exit Task", width=30, command=exit_button)
exits_button.pack(pady=5)

#start Program 
root.mainloop()