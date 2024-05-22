import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# function
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(f"{km_output:.2f}Km")

# By clicking enter
def on_enter(event):
    convert()

# Window
window = ttk.Window(themename='vapor')
window.title('Converter')
window.geometry('360x200')

# title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int, font='Calibri 20', width=5)
miles_label = ttk.Label(master=input_frame, text='Miles', font='Calibri 30')
button = ttk.Button(master=input_frame, text='Convert', command=convert)

entry.pack(side='left')
miles_label.pack(side='left')
button.pack(side='left', padx=10)

input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Calibri 30', textvariable=output_string)
output_label.pack(pady=12)

# bind the Enter key to the convert function
window.bind('<Return>', on_enter)

# run
window.mainloop()
