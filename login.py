from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from tkinter import messagebox
from bson.objectid import ObjectId


client= MongoClient(host='localhost', port=27017)
db = client['DataPython']
collection = db['users']



root=Tk()
root.title("login")
root.geometry("925x500+300+100")
root.configure(bg="#fff")
root.resizable(False,False)



# function login
def signin():
    def readData():
        Data_Users = collection.find({})
        return Data_Users

    def UpdateTree():
        for dt in tree.get_children():
            tree.delete(dt)
        for result1 in readData():
            tree.insert("", END, values=(result1["_id"], result1["FirstName"], result1["LastName"], result1["Age"], result1["userName"], result1["Tel"]), tag='header')
    def delete_data():
                selected_item = tree.selection()
                if(selected_item):
                    deleteData = str(tree.item(selected_item[0])['values'][0])
                    result = messagebox.askyesno("Confirmation", "Are you sure?")
                    if(result):
                        delete(str(deleteData))
                else:
                    messagebox.showerror("select one","data not selected")
                    
    def delete(id):
        collection.delete_one({"_id":ObjectId(id)})
        UpdateTree()
        print('success')

    username=user.get()
    password=passw.get()
    
    users=db.admin.find_one({"username": username, "password": password})

    if (users==None):
        messagebox.showerror("invalid","invalid username and password")
    else:
        print("Login successful")
        root.destroy()
        root2=Tk()
        root2.title("User management")
        root2.geometry('1100x700+200+30')
        root2.configure(bg="#fff")
        root2.resizable(False,False)


        # create a Treeview widget
        tree = ttk.Treeview(root2, columns=(1,2,3,4,5,6), height=25, show="headings")
        tree.place(x=25, y=170, width=1050, height=700)
        heading=Label(root2,text='User management',fg="#6366f1",bg="white",font=("Arial",30,"bold"),underline=0) 
        heading.place(x=400,y=30)

        

        tree.heading(1, text="ID", anchor=CENTER)
        tree.heading(2, text="First Name")
        tree.heading(3, text="Last Name")
        tree.heading(4, text="Age")
        tree.heading(5, text="userName")
        tree.heading(6, text="Tel")

        tree.column(1, width=150)
        tree.column(2, width=75)
        tree.column(3, width=75)
        tree.column(4, width=20)
        tree.column(5, width=100)
        tree.column(6, width=100)


        for result in readData():
            tree.insert("", END, values=(result["_id"], result["FirstName"], result["LastName"], result["Age"], result["userName"], result["Tel"]), tag='header')
        
        tree.tag_configure('header', font=('Arial', 11))
        style = ttk.Style()

        style.configure("Treeview", rowheight=40)
        style.configure('Treeview.Heading', font=('Arial', 12, 'bold'))


        #Form ADD
        def functionADD():
            root3=Tk()
            root3.title("Add User")
            root3.geometry("925x500+300+100")
            root3.configure(bg="#fff")
            root3.resizable(False,False)
#___________________________________________________________

             # Div_titre
            frame=Frame(root3,width=350,height=350,bg="white")
            frame.place(x=390,y=60)
            #  titre
            heading=Label(frame,text='Add User',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",28,"bold"))
            heading.place(x=5,y=1)

            # Div_1
            frame=Frame(root3,width=350,height=350,bg="white")
            frame.place(x=10,y=100)
            # FirstName  
            def on_enter(e):
                first_name.delete(0, "end")
            def on_leave(e):
                name=first_name.get()
                if name=="":
                    first_name.insert(0,'FirstName') 
            first_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            first_name.place(x=30,y=80)
            first_name.insert(0,"FirstName")
            first_name.bind("<FocusIn>",on_enter)
            first_name.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
            # LastName 
            def on_enter(e):
                lastt_name.delete(0, "end")
            def on_leave(e):
                name=lastt_name.get()
                if name=="":
                    lastt_name.insert(0,'LastName') 
            lastt_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            lastt_name.place(x=30,y=150)
            lastt_name.insert(0,"LastName")
            lastt_name.bind("<FocusIn>",on_enter)
            lastt_name.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
            # Age  
            def on_enter(e):
                age.delete(0, "end")
            def on_leave(e):
                name=age.get()
                if name=="":
                    age.insert(0,'Age')
            age=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            age.place(x=30,y=215)
            age.insert(0,"Age")
            age.bind("<FocusIn>",on_enter)
            age.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
            # Number
            def on_enter(e):
                tele.delete(0, "end")
            def on_leave(e):
                name=tele.get()
                if name=="":
                    tele.insert(0,'Number')
            tele=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            tele.place(x=30,y=285)
            tele.insert(0,"Number")
            tele.bind("<FocusIn>",on_enter)
            tele.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=312)

            # Div_2
            frame=Frame(root3,width=350,height=350,bg="white")
            frame.place(x=560,y=100)
            # username 
            def on_enter(e):
                user3.delete(0, "end")
            def on_leave(e):
                name=user3.get()
                if name=="":
                    user3.insert(0,'Username')
            user3=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            user3.place(x=30,y=80)
            user3.insert(0,"UserName")
            user3.bind("<FocusIn>",on_enter)
            user3.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
            # Password  
            def on_enter(e):
                pw.delete(0, "end")
                pw.config(show="*")
            def on_leave(e):
                name=pw.get()
                if name=="":
                    pw.insert(0,'Password')
                    pw.config(show="")
            pw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
            pw.place(x=30,y=150)
            pw.insert(0,"Password")
            pw.bind("<FocusIn>",on_enter)
            pw.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
            # Confirm Password  
            def on_enter(e):
                cpw.delete(0, "end")
                cpw.config(show="*")
            def on_leave(e):
                name=cpw.get()
                if name=="":
                    cpw.insert(0,'Confirm Password')
                    cpw.config(show="")
            cpw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11) )
            cpw.place(x=30,y=215)
            cpw.insert(0,"Confirm Password")
            cpw.bind("<FocusIn>",on_enter)
            cpw.bind("<FocusOut>",on_leave)
            Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
            def insert():
                collection.insert_one({"FirstName":first_name.get(),"LastName":lastt_name.get() ,"Age":age.get(),"userName": user3.get(),"Tel": tele.get(),"password":pw.get(),"Confirm_password":cpw.get()})
                UpdateTree()
                root3.destroy()
                print("add suce")
                
            # Button 
            Button(frame,width=27,pady=0,text="ADD",bg="#57a1f8",fg="white",border=0,font=("Microsoft YaHei UI Light",13,"bold"),command=insert).place(x=25,y=295)
            root3.mainloop()
#__________________________________________________________________
        def update_data():
                selected_item = tree.selection()
                if(selected_item):
                    updateData = str(tree.item(selected_item[0])['values'][0])
                    user_upd=collection.find_one({"_id":ObjectId(updateData)})
                    print(user_upd)
                    root4=Tk()
                    root4.title("Update User")
                    root4.geometry("925x500+300+100")
                    root4.configure(bg="#fff")
                    root4.resizable(False,False)

                    #__________________________________________________________________
                    # Modifier Utilisateur
                    # Div_titre
                    frame=Frame(root4,width=350,height=350,bg="white")
                    frame.place(x=390,y=60)
                    #  titre
                    heading=Label(frame,text='Update User',fg="green",bg="white",font=("Microsoft YaHei UI Light",28,"bold"))
                    heading.place(x=0,y=0)

                    # Div_1
                    frame=Frame(root4,width=350,height=350,bg="white")
                    frame.place(x=10,y=110)
                    # FirstName  
                    def on_enter(e):
                        first_name.delete(0, "end")
                    def on_leave(e):
                        name=first_name.get()
                        if name=="":
                            first_name.insert(0,'FirstName') 
                    first_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    first_name.place(x=30,y=80)
                    first_name.insert(0,user_upd["FirstName"])
                    first_name.bind("<FocusIn>",on_enter)
                    first_name.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
                    # LastName 
                    def on_enter(e):
                        lastt_name.delete(0, "end")
                    def on_leave(e):
                        name=lastt_name.get()
                        if name=="":
                            lastt_name.insert(0,'LastName') 
                    lastt_name=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    lastt_name.place(x=30,y=150)
                    lastt_name.insert(0,user_upd["LastName"])
                    lastt_name.bind("<FocusIn>",on_enter)
                    lastt_name.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
                    # Age  
                    def on_enter(e):
                        age.delete(0, "end")
                    def on_leave(e):
                        name=age.get()
                        if name=="":
                            age.insert(0,'Age')
                    age=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    age.place(x=30,y=215)
                    age.insert(0,user_upd["Age"])
                    age.bind("<FocusIn>",on_enter)
                    age.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)
                    # Number
                    def on_enter(e):
                        tele.delete(0, "end")
                    def on_leave(e):
                        name=tele.get()
                        if name=="":
                            tele.insert(0,'Number')
                    tele=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    tele.place(x=30,y=285)
                    tele.insert(0,user_upd["Tel"])
                    tele.bind("<FocusIn>",on_enter)
                    tele.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=312)

                    # Div_2
                    frame=Frame(root4,width=350,height=350,bg="white")
                    frame.place(x=560,y=110)
                    # username 
                    def on_enter(e):
                        user.delete(0, "end")
                    def on_leave(e):
                        name=user.get()
                        if name=="":
                            user.insert(0,'Username')
                    user=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    user.place(x=30,y=80)
                    user.insert(0,user_upd["userName"])
                    user.bind("<FocusIn>",on_enter)
                    user.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
                    # Password  
                    def on_enter(e):
                        pw.delete(0, "end")
                        pw.config(show="*")
                    def on_leave(e):
                        name=pw.get()
                        if name=="":
                            pw.insert(0,'Password')
                            pw.config(show="")
                    pw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
                    pw.place(x=30,y=150)
                    pw.insert(0,user_upd["password"])
                    pw.bind("<FocusIn>",on_enter)
                    
                    pw.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
                    # Confirm Password  
                    def on_enter(e):
                        cpw.delete(0, "end")
                        cpw.config(show="*")
                    def on_leave(e):
                        name=cpw.get()
                        if name=="":
                            cpw.insert(0,'Confirm Password')
                            cpw.config(show="")
                    cpw=Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11) )
                    cpw.place(x=30,y=215)
                    cpw.insert(0,user_upd["Confirm_password"])
                    cpw.bind("<FocusIn>",on_enter)
                    cpw.bind("<FocusOut>",on_leave)
                    Frame(frame,width=295,height=2,bg="black").place(x=25,y=244)

                    #function update db
                    def update_db():
                        collection.update_one({"_id":ObjectId(updateData)},{"$set":{"FirstName":first_name.get(),"LastName":lastt_name.get() ,"Age":age.get(),"userName": user.get(),"Tel": tele.get(),"password":pw.get(),"Confirm_password":cpw.get()}})
                        UpdateTree()
                        root4.destroy()


                    # Button 
                    Button(frame,width=27,pady=0,text="Update",bg="green",fg="white",border=0,font=("Microsoft YaHei UI Light",13,"bold"), command=update_db).place(x=25,y=295)
                    
                else:
                    messagebox.showerror("select one","data not selected")



#__________________________________________________________________

        Button(root2,width=10,pady=5,text="Add",bg="#57a1f8",fg="white",border=0,command=functionADD,font=("Arial", 12)).place(x=700,y=120)
        Button(root2,width=10,pady=5,text="Update",bg="green",fg="white",border=0,command=update_data,font=("Arial", 12)).place(x=820,y=120)
        Button(root2,width=10,pady=5,text="Delete",bg="#dc2626",fg="white",border=0,command=delete_data,font=("Arial", 12)).place(x=940,y=120)
        root2.mainloop()
       

img=PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Login',fg="#6366f1",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)



# Username

# username function 
def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'Username')
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
# Password
def on_enter2(e):
    passw.delete(0, "end")
    passw.config(show="*")
def on_leave2(e):
    name=passw.get()
    if name=="":
        passw.insert(0,'Password')
        passw.config(show="")
passw=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
passw.place(x=30,y=150)
passw.insert(0,"Password")
passw.bind("<FocusIn>",on_enter2)
passw.bind("<FocusOut>",on_leave2)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
# Button 
Button(frame,width=30,pady=5,text="Login",bg="#6366f1",fg="white",border=0,font=("Arial", 12),command=signin).place(x=35,y=220)


root.mainloop()