"""#####################DOCUMENTATION#######################
Graphical UserInterface Address Book Made Using TkinterPy
This is Just a Demo of Address Book Working Using TkinterPy
      #CODE--DEEPAKCHAKRAVARTHY
#########################################################"""
#IMPORT FILES
from tkinter import * 
import tkinter.messagebox
from PIL import ImageTk, Image 
def helpdev():#help action
    tkinter.messagebox.showinfo("AddressBook Help","This is Sample of Address Book")
    tkinter.messagebox.showinfo("AddressBook Contact","for contact deepakchakravarthy.d@gmail.com")
def restart():#to RESTART THE APPLICATION
    import address
def radioaction():
    notassign = var8.get()
def box():
    from tkinter import messagebox
    messagebox.showinfo("Address Book", "Thank You")
def clear():#TO CLEAR THE ENTRY
    e1 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 50)  
    
    e2 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark green").place(x = 170,y = 100)
    
    e3 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 150)
    
    e4 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark green").place(x = 170,y = 200)
    
    e5 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 250)
    
    e6 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 300)
    
    e7 = Entry(top,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 350)
def save():
    tkinter.messagebox.showinfo("Address Book", "Thank You Contact Saved")
    FullName = var1.get()
    
    NickName = var2.get()
    
    Emailid  = var3.get()
    
    phonenum = var4.get()
    
    DOB      = var5.get()
    
    ADDRESS  = var6.get()
    
    STATE    = var7.get()
    
    f = open("user.bat","w")
    
    f.write("@echo   FULL NAME %s  \n"%FullName)
    
    f.write("@echo   NICK NAME %s  \n"%NickName)
    
    f.write("@echo   EMAIL ID  %s  \n"%Emailid)
    
    f.write("@echo   Phonenum  %d  \n"%phonenum)
    
    f.write("@echo   dob       %s  \n"%DOB)
    
    f.write("@echo   address   %s  \n"%ADDRESS)
    
    f.write("@echo   State     %s  \n"%STATE)
    
    f.write("pause")
    
    f.close()
    
    print(FullName)#test
    
    print(NickName)
top= Tk()
menubar = Menu(top)
top.title("Address Book")#TITLE BAR
#VARIABLES DATA TYPE(FOR ENTRY)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = IntVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
#Variable For RadioButton Value
var8 = IntVar()
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=restart)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=helpdev)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
top.config(menu=menubar)
#Background Image
img = ImageTk.PhotoImage(Image.open('bg.png'))
w = Label(top,image = img)
w.pack(side = "bottom", fill = "both", expand = "yes")
w.pack()
#Screen Resolution
top.geometry("1366x768")
top.config(bg='brown')
#Labels
name = Label(top, text = "FULLNAME",font = 'HarlowSolid 12 bold ',background = "black",fg = "aqua").place(x = 20,y = 50)

nick = Label(top, text = "NICKNAME",font = 'HarlowSolid 12 bold',background = "black",fg = "yellow").place(x = 20, y =100)

email = Label(top, text = "EMAIL ID",font = 'HarlowSolid 12 bold',background = "black",fg = "red").place(x = 20, y =150)

Phonenum = Label(top, text = "PHONE NUMBER",font = 'HarlowSolid 12 bold',background = "black",fg = "white").place(x = 20, y =200)

dob = Label(top, text = "DATE OF BIRTH",font = 'HarlowSolid 12 bold',background = "black",fg = "blue").place(x = 20, y =250)

Address = Label(top, text = "ADDRESS",font = 'HarlowSolid 12 bold',background = "black",fg = "light green").place(x = 20, y =300)

state = Label(top, text = "STATE",font = 'HarlowSolid 12 bold',background = "black",fg = "blue").place(x = 20, y =350)

GROUP = Label(top, text = "GROUP",font = 'HarlowSolid 12 bold',background = "black",fg = "light pink").place(x = 20, y =400)
#sbmitbtn = Button(top, text = "Continue",command = box ,activebackground = "pink", activeforeground = "blue").place(x = 222, y = 300)

#ENTRY  BOX FOR THE USERS
e1 = Entry(top,textvariable = var1,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 50)

e2 = Entry(top,textvariable = var2,font = 'HarlowSolid 12 bold',fg = "dark green").place(x = 170,y = 100)

e3 = Entry(top,textvariable = var3,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 150)

e4 = Entry(top,textvariable = var4,font = 'HarlowSolid 12 bold',fg = "dark green").place(x = 170,y = 200)

e5 = Entry(top,textvariable = var5,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 250)

e6 = Entry(top,textvariable = var6,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 300)

e7 = Entry(top,textvariable = var7,font = 'HarlowSolid 12 bold',fg = "dark blue").place(x = 170,y = 350)
#GROUP IN CONTACTS --->RadioButton
R1 = Radiobutton(top,text = "Not Assigned",variable = var8,value = 1,command = radioaction,indicatoron =0,font = 'calibri 10 bold',fg = "pink",bg = "black").place(x = 160,y=400)

R2 = Radiobutton(top,text = "Family",variable = var8,value = 2,command = radioaction,indicatoron=0,font = 'calibri 10 bold',fg = "pink",bg = "black").place(x = 160,y=450)

R3 = Radiobutton(top,text = "Friends",variable = var8,value = 3,command = radioaction,indicatoron=0,font = 'calibri 10 bold',fg = "pink",bg = "black").place(x = 160,y=500)

R4 = Radiobutton(top,text = "ICE Emergency Contact",variable = var8,value = 4,command = radioaction,indicatoron=0,font = 'calibri 10 bold',fg = "pink",bg = "black").place(x = 160,y=550)

#BUTTONS FOR SAVE AND CLEAR
easybtn = Button(top, text = "     SAVE      ",command =save ,font = 'Algerian 14 bold underline',background = "green",fg = "yellow",activebackground ="red",activeforeground = "blue").place(x = 1100,y = 250) 
sbmitbtn = Button(top, text = "     Clear     ",command = clear,font = 'Algerian 14 bold underline',background = "yellow",fg = "black",activebackground = "pink", activeforeground = "blue").place(x = 1100, y = 300)
top.mainloop()