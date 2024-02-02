from tkinter import*
from tkinter import messagebox

win=Tk()

win.title('Student Form')
win.configure(bg='black')
win.geometry('500x500')


def insert():
    f_name=str(enter_name.get())
    f_lastname=str(enter_lastname.get())
    f_avrage=float(enter_avrage.get())
    f_age=int(enter_age.get())
    
    data=f'{f_name}_ {f_lastname}_ {f_avrage}_ {f_age}'
    
    if f_avrage<=20 and f_avrage>=17:
        messagebox.showinfo('Avrage','You are good at subjects school.')
        
    elif f_avrage<17 and f_avrage>=13:
        messagebox.showinfo('Avrage','You are not bad at subjects school.')
            
    elif f_avrage<13 and f_avrage>=0:
       messagebox.showinfo('Avrage','You are need more practice at subjects school.')



    if  f_avrage<=20 and f_avrage>=0:

                
        lst_box.insert(END,data)
        
        enter_name.delete(0,END)
        enter_lastname.delete(0,END)
        enter_avrage.delete(0,END)
        enter_age.delete(0,END)
    
        
        enter_name.focus_set()
        
    else:
        messagebox.showerror('Avrage','Enter your correct avrge between 20 and 0 please.')
        
        
def fetch():
    index=lst_box.curselection()
    data=lst_box.get(index)
    spliting=data.split('_')
    f_name=spliting[0]
    f_lastname=spliting[1]
    f_avrage=spliting[2]
    f_age=spliting[3]
    
    lst_box.delete(index)
    
    enter_name.insert(0,f_name)
    enter_lastname.insert(0,f_lastname)
    enter_avrage.insert(0,f_avrage)
    enter_age.insert(0,f_age)
    
def delete():
    index=lst_box.curselection()
    result=messagebox.askquestion('Delete','Are you sure you want to delete this item?')
    if result=='yes':
        lst_box.delete(index)
        


def clear():
    result=messagebox.askquestion('Clear','Are you sure you want to clear everything?')
    if result=='yes':
        lst_box.delete(0,END)
        
        
def exit():
    result=messagebox.askquestion('Exit','Are you sure you want exit?')
    if result=='yes':
        
        win.destroy()
    
                        
        
lbl_name=Label(win,text='Name:',font='arial 17 bold',bg='black',fg='light blue')
lbl_name.place(x=20,y=30)

lbl_name=Label(win,text='lastname:',font='arial 17 bold',bg='black',fg='light blue')
lbl_name.place(x=20,y=70)

lbl_name=Label(win,text='Avrage:',font='arial 17 bold',bg='black',fg='light blue')
lbl_name.place(x=20,y=110)

lbl_name=Label(win,text='Age:',font='arial 17 bold',bg='black',fg='light blue')
lbl_name.place(x=20,y=150)


enter_name=Entry(win,font='arial 17 bold',bg='gray',fg='white',width=25)
enter_name.place(x=100,y=30)

enter_lastname=Entry(win,font='arial 17 bold',bg='gray',fg='white',width=22)
enter_lastname.place(x=140,y=70)

enter_avrage=Entry(win,font='arial 17 bold',bg='gray',fg='white',width=23)
enter_avrage.place(x=125,y=110)

enter_age=Entry(win,font='arial 17 bold',bg='gray',fg='white',width=26)
enter_age.place(x=85,y=150)


btn_insert=Button(win,text='Insert',font='arial 17 bold',bg='green',fg='orange',command=insert)
btn_insert.place(x=20,y=430)

btn_fetch=Button(win,text='Fetch',font='arial 17 bold',bg='green',fg='orange',command=fetch)
btn_fetch.place(x=120,y=430)

btn_delete=Button(win,text='Delete',font='arial 17 bold',bg='green',fg='orange',command=delete)
btn_delete.place(x=220,y=430)

btn_clear=Button(win,text='Clear',font='arial 17 bold',bg='green',fg='orange',command=clear)
btn_clear.place(x=330,y=430)

btn_exit=Button(win,text='Exit',font='arial 17 bold',bg='green',fg='orange',command=exit)
btn_exit.place(x=430,y=430)


lst_box=Listbox(win,font='arial 13 bold',bg='purple',fg='black',width=50)
lst_box.place(x=20,y=200)


win.mainloop()
