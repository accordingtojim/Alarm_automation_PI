from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from turtle import left
import define_window_inverter as dwi
import define_window_battery as dwb
import config

def openNewWindow():        
    # Toplevel object which will be treated as a new window
    number_of_PH = StringVar()
    number_of_EH = StringVar()
    number_type0 = StringVar()
    config.counter += 1
    frame1 = Toplevel()
    frame1.geometry("800x400")
    frame1.resizable(True, True)
    frame1.title("Define "+config.num_assign(config.counter)+" topology")
    
    # A Label widget to show in toplevel
    #Label(frame1,text ="Define first topology").grid(column=0,row=0,sticky=W)
    
    # adding image (remember image should be PNG and not JPG)
    # img = PhotoImage(file = "C:/Users/VB2117/CODICE jimmy/tkinter/logo1.png")
    # img1 = img.subsample(2, 2)
    # Label(frame1, image = img1).grid(row = 0, column = 1, sticky=E ,columnspan = 2, rowspan = 2)

    # empty label 1
    empty_label = Label(frame1, text="")
    empty_label.grid(row=0,column=0,columnspan=3,sticky=N,pady=0)
    
    # PH LABEL
    num_PH_label = Label(frame1, text="Insert number of PH")
    num_PH_label.grid(row=1,column=2,padx=200)
    
    # empty label 2
    empty_label = Label(frame1, text="")
    empty_label.grid(row=2,column=0,columnspan=2,sticky=N,pady=0)
    
    #PH entry    
    PH_entry = Entry(frame1, textvariable=number_of_PH)
    PH_entry.grid(row=3,column=2,padx=200, sticky=W)
    PH_entry.focus()
    
    # empty label 3
    empty_label = Label(frame1, text="")
    empty_label.grid(row=4,column=0,columnspan=2,sticky=N,pady=0)
    
    # EH label
    num_EH_label = Label(frame1, text="Insert the number of EH")
    num_EH_label.grid(row=5,column=2,padx=200)
    
    # empty label 4
    empty_label = Label(frame1, text="")
    empty_label.grid(row=6,column=0,columnspan=2,sticky=N,pady=0)
    
    # EH entry
    EH_entry = Entry(frame1, textvariable=number_of_EH)
    EH_entry.grid(row=7,column=2,padx=200,sticky=W)
    
    # empty label 5
    empty_label = Label(frame1, text="")
    empty_label.grid(row=8,column=0,columnspan=2,sticky=N,pady=0)
      
    # Number topology label
    num_TOP_label = Label(frame1, text="How many of this topology in the plant")
    num_TOP_label.grid(row=9,column=2,padx=0)
    
    # empty label 6
    empty_label = Label(frame1, text="")
    empty_label.grid(row=10,column=0,columnspan=2,sticky=N,pady=0)
    
    # Number topology entry
    TOP_entry = Entry(frame1, textvariable=number_type0)
    TOP_entry.grid(row=11,column=2,padx=0)
    
    # empty label 7
    empty_label = Label(frame1, text="")
    empty_label.grid(row=12,column=0,columnspan=3,sticky=N,pady=0)
 
    # Next button
    next_button = Button(frame1,text='Next Topology', command=openNewWindow)
    next_button.grid(row=14,column=3,padx=0,sticky=E)
    
    # empty label 8
    empty_label = Label(frame1, text="")
    empty_label.grid(row=14,column=0,columnspan=3,sticky=N,pady=30)
    
    # Exit button
    exit_button = Button(frame1,text='Save',command=lambda: config.destroy_ww(frame1))                #lambda: frame1.quit())
    exit_button.grid(row=15,column=1,padx=20,sticky=S)
    
    # Define PH button
    OK_button = Button(frame1,text='Define PH', command=dwi.openNewWindow)
    OK_button.grid(row=3,column=2,padx=10,sticky=E)
    
    # Define EH button
    OK_button = Button(frame1,text='Define EH', command=dwb.openNewWindow)
    OK_button.grid(row=7,column=2,padx=10,sticky=E)
    
    frame1.mainloop()

    config.array_PH.append(number_of_PH.get())
    config.array_EH.append(number_of_EH.get())
    config.array_type.append(int(number_type0.get()))
    





    
