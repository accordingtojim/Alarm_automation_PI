from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from turtle import left
import config

def openNewWindow():
    # Toplevel object which will be treated as a new window
    number_of_bb = StringVar()
    number_of_br = StringVar()
    number_of_inverter = StringVar()
    number_type0 = StringVar()
    number_HVAC = StringVar()
    #number_of_Ginverter = StringVar()
    
    frame1 = Toplevel()
    frame1.geometry("500x450")
    frame1.resizable(True, True)
    frame1.title("Define each Hybrid House")
    
    # A Label widget to show in toplevel
    #Label(frame1,text ="Define first topology").grid(column=0,row=0,sticky=W)
    
    # adding image (remember image should be PNG and not JPG)
    # img = PhotoImage(file = "C:/Users/VB2117/CODICE jimmy/tkinter/logo1.png")
    # img1 = img.subsample(2, 2)
    # Label(frame1, image = img1).grid(row = 0, column = 1, sticky=E ,columnspan = 2, rowspan = 2)

    # empty label 1
    empty_label = Label(frame1, text="")
    empty_label.grid(row=0,column=0,columnspan=3,sticky=N,pady=0)
    
    # Battery Bank LABEL
    num_bb_label = Label(frame1, text="Insert the number of Battery Bank")
    num_bb_label.grid(row=1,column=2,padx=0)
    
    # empty label 2
    empty_label = Label(frame1, text="")
    empty_label.grid(row=2,column=0,columnspan=2,sticky=N,pady=0)
    
    # Battery Bank entry    
    bb_entry = Entry(frame1, textvariable=number_of_bb)
    bb_entry.grid(row=3,column=2,padx=0)
    bb_entry.focus()
    
    # empty label 3
    empty_label = Label(frame1, text="")
    empty_label.grid(row=4,column=0,columnspan=2,sticky=N,pady=0)
    
    # Battery Rack label
    num_inv_label = Label(frame1, text="Insert the number of Battery rack for each battery bank") #to be ddefined
    num_inv_label.grid(row=5,column=2,padx=0)
    
    # empty label 4
    empty_label = Label(frame1, text="")
    empty_label.grid(row=6,column=0,columnspan=2,sticky=N,pady=0)
    
    # Battery Rack entry
    Ginv_entry = Entry(frame1, textvariable=number_of_br)
    Ginv_entry.grid(row=7,column=2,padx=0)   #sticky = W
    
    # empty label 5
    empty_label = Label(frame1, text="")
    empty_label.grid(row=8,column=0,columnspan=2,sticky=N,pady=0)

    # Inverter label
    num_inv_label = Label(frame1, text="Insert the number of Inverter (Default = 2)") #to be ddefined
    num_inv_label.grid(row=9,column=2,padx=0)
    
    # empty label 6
    empty_label = Label(frame1, text="")
    empty_label.grid(row=10,column=0,columnspan=2,sticky=N,pady=0)
    
    #Inverter entry    
    Inv_entry = Entry(frame1, textvariable=number_of_inverter)
    Inv_entry.grid(row=11,column=2,padx=0)
    
    # empty label 7
    empty_label = Label(frame1, text="")
    empty_label.grid(row=12,column=0,columnspan=2,sticky=N,pady=0)
    
     # Number HVAC label
    num_TOP_label = Label(frame1, text="Insert the number of HVAC (Default = 1)")
    num_TOP_label.grid(row=13,column=2,padx=0)
    
    # empty label 8
    empty_label = Label(frame1, text="")
    empty_label.grid(row=14,column=0,columnspan=2,sticky=N,pady=0)
    
    # Number HVAC entry
    TOP_entry = Entry(frame1, textvariable=number_HVAC)
    TOP_entry.grid(row=15,column=2,padx=0)
    
    # empty label 9
    empty_label = Label(frame1, text="")
    empty_label.grid(row=16,column=0,columnspan=3,sticky=N,pady=0)
    
     # Number topology label
    num_TOP_label = Label(frame1, text="How many of this topology in the plant")
    num_TOP_label.grid(row=17,column=2,padx=0)
    
    # empty label 10
    empty_label = Label(frame1, text="")
    empty_label.grid(row=18,column=0,columnspan=2,sticky=N,pady=0)
    
    # Number topology entry
    TOP_entry = Entry(frame1, textvariable=number_type0)
    TOP_entry.grid(row=19,column=2,padx=0)
    
    # empty label 11
    empty_label = Label(frame1, text="")
    empty_label.grid(row=16,column=0,columnspan=3,sticky=N,pady=0)
      
    # Exit button
    exit_button = Button(frame1,text='Save and exit',command=lambda:config.destroy_ww(frame1))                #lambda: frame1.quit())
    exit_button.grid(row=19,column=1,padx=20,sticky=S)
     
    frame1.mainloop()
    config.n_battery_bank.append(number_of_bb.get())
    config.n_battery_rack.append(number_of_br.get())
    config.n_CBESS.append(number_of_inverter.get())
    config.array_type_HH.append(number_type0.get())
    config.n_HVAC_HH.append(number_HVAC.get())





    
