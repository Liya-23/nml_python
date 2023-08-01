from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

#colors
background_color = "#06283D"
framebg_color = "#EDEDED"
framefg_color = "#06283D"

root = Tk()
root.title("Apply At Newly Made Leaders Academy")
root.geometry("1435x1020")
root.config(bg=background_color)

file=pathlib.Path("Register_data.xlsx")
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet["A0"] = "Hero"
    sheet["A1"] = "First Name"
    sheet["B1"] = "Middle Name"
    sheet["C1"] = "Last Name"
    sheet["D1"] = "ID Number"
    sheet["E1"] = "Email"
    sheet["F1"] = "Phone Number"
    sheet["G1"] = "Date Of Birth"
    sheet["H1"] = "Gender"
    sheet["I1"] = "Year Applied For"
    sheet["J1"] = "Date"    

    file.save("Register_data.xlsx")


root.mainloop()