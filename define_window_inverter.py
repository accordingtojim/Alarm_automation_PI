from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from turtle import left
import config

def openNewWindow():
    # Toplevel object which will be treated as a new window

    number_of_inverter = StringVar()
    number_of_Ginverter = StringVar()
    
    frame1 = Toplevel()
    frame1.geometry("800x450")
    frame1.resizable(True, True)
    frame1.title("Define type of inverter")
    
    # A Label widget to show in toplevel
    #Label(frame1,text ="Define first topology").grid(column=0,row=0,sticky=W)
    
    # adding image (remember image should be PNG and not JPG)
    # img = PhotoImage(file = "C:/Users/VB2117/CODICE jimmy/tkinter/logo1.png")
    # img1 = img.subsample(2, 2)
    # Label(frame1, image = img1).grid(row = 0, column = 1, sticky=E ,columnspan = 2, rowspan = 2)

    # empty label 1
    empty_label = Label(frame1, text="")
    empty_label.grid(row=0,column=0,columnspan=3,sticky=N,pady=0)
    
    # Inverter LABEL
    num_inv_label = Label(frame1, text="Insert the number of C-BESSHD Inverter")
    num_inv_label.grid(row=1,column=2,padx=200)
    
    # empty label 2
    empty_label = Label(frame1, text="")
    empty_label.grid(row=2,column=0,columnspan=2,sticky=N,pady=0)
    
    #Inverter entry    
    Inv_entry = Entry(frame1, textvariable=number_of_inverter)
    Inv_entry.grid(row=3,column=2,padx=200, sticky=W)
    Inv_entry.focus()
    
    # empty label 3
    empty_label = Label(frame1, text="")
    empty_label.grid(row=4,column=0,columnspan=2,sticky=N,pady=0)
    
    # General inverter label
    num_Ginv = Label(frame1, text="Insert the number of other Inverter") #to be ddefined
    num_Ginv.grid(row=5,column=2,padx=200)
    
    # empty label 4
    empty_label = Label(frame1, text="")
    empty_label.grid(row=6,column=0,columnspan=2,sticky=N,pady=0)
    
    # General inverter entry
    Ginv_entry = Entry(frame1, textvariable=number_of_Ginverter)
    Ginv_entry.grid(row=7,column=2,padx=200,sticky=W)
    
    # empty label 5
    empty_label = Label(frame1, text="")
    empty_label.grid(row=8,column=0,columnspan=2,sticky=N,pady=0)
      
    # Exit button
    exit_button = Button(frame1,text='Save',command=lambda:config.destroy_ww(frame1))                #lambda: frame1.quit())
    exit_button.grid(row=9,column=1,padx=20,sticky=S)
     
    frame1.mainloop()
    config.n_CBESS.append(number_of_inverter.get())
    config.n_other_inverter.append(number_of_Ginverter.get())






    
