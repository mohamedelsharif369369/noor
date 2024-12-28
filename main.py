from tkinter import *
from tkinter import ttk
from db import DataBase
from tkinter import messagebox

db = DataBase("NOOR.db")

root = Tk()
root.title('NOOR')
root.geometry('1590x800+0+0')
root.resizable(False,False)
root.configure(bg='#2c3e50')

code = StringVar()
kmih = StringVar()
price = StringVar()
ml7ozat = StringVar()


#logo = PhotoImage(file='noor.jpg')
#lbl_logo = Label(root,image=logo)
#lbl_logo.place(x=80,y=520)

# =================| Entries Frame |=======================

entries_frame = Frame(
    root,
    bg='#2c3e50'
    )
entries_frame.place(
    x=1,
    y=1,
    width=360,
    height=510
    )
Title = Label(
    entries_frame,
    text='منظومة كروت الافراح',
    font=('Calibri',18,'bold'),
    bg='#2c3e50',fg='white'
    )
Title.place(
    x=10,
    y=1
    )

lblCode = Label(
    entries_frame,
    text='           الكود',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblCode.place(
    x=10,
    y=60
    )
txtCode = Entry(
    entries_frame,
    textvariable=code,
    width=20,
    font=('Calibri',16)
    ) 
txtCode.place(
    x=120,
    y=60
    )

lblKmih = Label(
    entries_frame,
    text='          الكميه',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblKmih.place(
    x=10,
    y=120
    )
txtKmih = Entry(
    entries_frame,
    textvariable=kmih,
    width=20,
    font=('Calibri',16)
    ) 
txtKmih.place(
    x=120,
    y=120
    )

lblPrice= Label(
    entries_frame,
    text='          السعر',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblPrice.place(
    x=10,
    y=180
    )
txtPrice= Entry(
    entries_frame,
    textvariable=price,
    width=20,
    font=('Calibri',16)
    ) 
txtPrice.place(
    x=120
    ,y=180
    )

lblMl7ozat = Label(
    entries_frame,
    text='     ملاحظات',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblMl7ozat.place(
    x=10,
    y=240
    )
txtMl7ozat = Entry(
    entries_frame,
    textvariable=ml7ozat,
    width=20,
    font=('Calibri',16)
    ) 
txtMl7ozat.place(
    x=120
    ,y=240
    )
# =================| Defines |=============================

def hide():
    root.geometry("360x510")

def show():
    root.geometry('1590x800+0+0')
    

btnHide = Button(
    entries_frame,
    text='اخفاء',
    bg='white',
    bd=1,
    relief=SOLID,
    cursor='hand2',
    command=hide
    )
btnHide.place(
    x=270,
    y=10
    )

btnShow = Button(
    entries_frame,
    text='اظهار',
    bg='white',
    bd=1,
    relief=SOLID,
    cursor='hand2',
    command=show
    )
btnShow.place(
    x=310,
    y=10
    )

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    code.set(row[1])
    kmih.set(row[2])
    price.set(row[3])
    ml7ozat.set(row[4])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert(
            "",
            END,
            values=row
            )

def delete():
    db.remove(row[0])
    clear()
    displayAll()
    
def clear():
    code.set("")
    kmih.set("")
    price.set("")
    ml7ozat.set("")

def add_emoloyee():
    if txtCode.get() == "" or txtKmih.get() == "" or txtPrice.get() == "" :
        messagebox.showerror(
            "Error",
            "من فضلك قم بملىء كافة الحقول"
            )
        return
    db.insert(
        txtCode.get(),
        txtKmih.get(),
        txtPrice.get(),
        txtMl7ozat.get()
        )
    #messagebox.showinfo("Success"," هل تريد اضافة خدمه جديده")
    clear()
    displayAll()


def update():
    if txtCode.get() == "" or txtKmih.get() == "" or txtPrice.get() == "" :
        messagebox.showerror(
            "Error",
            "من فضلك قم بملىء كافة الحقول"
            )
        return
    db.update(
        row[0],
        txtCode.get(),
        txtKmih.get(),
        txtPrice.get(),
        txtMl7ozat.get()
        )
    #messagebox.showinfo("Success","هل تريد تعديل هذه الخدمه ؟")
    clear()
    displayAll()

# ============================| Buttons Frame |===========================================================

btn_frame = Frame(
    entries_frame,
    bg='#2c3e50',
    bd=1,
    relief=SOLID
    )
btn_frame.place(
    x=10,
    y=400,
    width=335,
    height=100
    )

btnAdd = Button(
    btn_frame,
    text='اضافة كارت',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#16a085',
    bd=0,
    command=add_emoloyee
    ).place(x=4,y=5)

btnUpdate = Button(
    btn_frame,
    text='تعديل الكارت',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#2980b9',
    bd=0,
    command=update
    ).place(x=4,y=50)

btnDelete = Button(
    btn_frame,
    text='حذف الكارت',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#c0392b',
    bd=0,
    command=delete
    ).place(x=170,y=5)

btnClear = Button(
    btn_frame,
    text='مسح الحقول',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#f39c12',
    bd=0,
    command=clear
    ).place(x=170,y=50)

# ============================| Table Frame |===========================================================

tree_Frame = Frame(
    root,
    bg='white'
    )
tree_Frame.place(
    x=365,
    y=1,
    width=1230,
    height=795
    )

style = ttk.Style()

style.configure(
    "mystyle.Treeview",
    font=('Calibri',13),
    rowheight=50
    )
style.configure(
    "mystyle.Treeview.Heading",
    font=('Calibri',13)
    )

tv = ttk.Treeview(
    tree_Frame,
    columns=(1,2,3,4,5),
    style="mystyle.Treeview"
    )

tv.heading(
    "1",
    text="مسلسل"
    )
tv.column(
    "1",
    width="120"
    )

tv.heading(
    "2",
    text="الكود"
    )
tv.column(
    "2",
    width="180"
    )

tv.heading(
    "3",
    text="الكميه"
    )
tv.column(
    "3",
    width="180"
    )

tv.heading(
    "4",
    text="السعر"
    )
tv.column(
    "4",
    width="180"
    )

tv.heading(
    "5",
    text="ملحوظات"
    )
tv.column(
    "5",
    width="300"
    )

tv['show'] = 'headings'

tv.bind(
    "<ButtonRelease-1>",
    getData
    )

tv.place(
    x=1,
    y=1,
    height=794,
    width=1230
    )

displayAll()

root.mainloop()