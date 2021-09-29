from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from conn_db.connect_db import *
from models.model import *
from tkinter import TclError


class SignIn:
    def __init__(self, window):
        self.dbconnect = DbConnection()
        self.win = window
        self.win.geometry('1350x1020+0+0')
        self.win.title('Login')
        # ============BACKGROUND IMAGE===============
        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        bg = Label(self.win, image=self.bg).place(relwidth=1, relheight=1)
        # ============ FLAME FOR FIELDS===============
        self.frame = Frame(self.win, bg='white')
        self.frame.place(height=410, width=670, x=400, y=200)

        # ============USER LOGO==============
        self.user_logo = (ImageTk.PhotoImage(file='../images/user.png'))
        user_logo = Label(self.frame, image=self.user_logo, bg='white').place(x=280, height=400, width=400)
        # =============FIELDS====================
        self.username = StringVar()
        self.password = StringVar()
        Label(self.frame, text='Username: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=70)
        self.ent_username = Entry(self.frame, font=('Comic Sans MS', 14, 'bold'), textvariable=self.username, bd='2',
                                  bg='lightgrey')
        self.ent_username.place(x=50, y=120)
        Label(self.frame, text='Password:', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=170)
        self.ent_password = Entry(self.frame, font=('Comic Sans MS', 14, 'bold'), show='*', textvariable=self.password,
                                  bd='2', bg='lightgrey')
        self.ent_password.place(x=50, y=220)
        Button(self.frame, text='Sign In', command=self.log, font=('Comic Sans MS', 14, 'bold')).place(x=110, y=270)
        # ============ FLAME FOR FIELDS===============
        self.frame2 = Frame(self.win, bg='white')
        self.frame2.place(height=100, width=670, x=400, y=620)
        # ============ BUTTON===============
        Button(self.frame2, text='Clear', command=self.clear, font=('Comic Sans MS', 14, 'bold')).place(x=20, y=20,height=50,width=100)
        Button(self.frame2, text='Register', command=self.log_signup, font=('Comic Sans MS', 14, 'bold')).place(x=200,y=20,height=50,width=150)
        Button(self.frame2, text='Exit', command=self.destroy_window, font=('Comic Sans MS', 14, 'bold')).place(x=440,y=20,height=50,width=100)

    def log(self):
        log_ref = Login(self.username.get(), self.password.get())
        if log_ref.get_username() == '' or log_ref.get_password() == '':
            Label(self.frame, text='Enter your username and password', bg='white',fg = 'red', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=20)
        else:
            query = 'select username, password from login where username = %s and password = %s;'
            values = (log_ref.get_username(), log_ref.get_password())
            datas = self.dbconnect.select_value(query, values)
            for data in datas:
                if data[0] == log_ref.get_username() and data[1] == log_ref.get_password():
                    messagebox.showinfo('Success','You have been logged in')
                    self.log_menupage()
            return Label(self.frame, text='Username or Password does not matched', bg='white',fg = 'red', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=20)

    def clear(self):
        username = self.ent_username
        password = self.ent_password
        username.delete(0, END)
        password.delete(0, END)

    def destroy_window(self):
        self.win.destroy()

    def log_menupage(self):
        mainpage = MenuPage(self.win,self.ent_username.get())

    def log_signup(self):
        signup = SignUp(self.win)


class SignUp:
    def __init__(self, window):
        self.dbconnect = DbConnection()
        self.win = window
        self.win.geometry('1350x1020+0+0')
        self.win.title('SignUp')
        # ============BACKGROUND IMAGE===============
        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        bg = Label(self.win, image=self.bg).place(relwidth=1, relheight=1)
        # ============ FLAME FOR FIELDS===============
        self.frame = Frame(self.win, bg='white')
        self.frame.place(height=550, width=750, x=300, y=200)

        self.username = StringVar()
        self.password = StringVar()
        self.password2 = StringVar()
        self.age = IntVar()
        self.address = StringVar()
        self.fullname = StringVar()
        self.email = StringVar()

        Label(self.frame, text='Username: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=50)
        self.ent_user = Entry(self.frame, textvariable=self.username, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_user.place(x=50, y=100)

        Label(self.frame, text='Password: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=150)
        self.ent_pass = Entry(self.frame, show='*', textvariable=self.password, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_pass.place(x=50, y=200)

        Label(self.frame, text='Confirm Password: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=250)
        self.ent_pass2 = Entry(self.frame, show='*', textvariable=self.password2, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_pass2.place(x=50, y=300)

        Label(self.frame, text='Age: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=50, y=350)
        self.ent_age = Entry(self.frame, textvariable=self.age, bd='2', bg='lightgrey', font=('Comic Sans MS', 14, 'bold'))
        self.ent_age.place(x=50, y=400)

        Label(self.frame, text='Address: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=350, y=50)
        self.ent_address = Entry(self.frame, textvariable=self.address, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_address.place(x=350, y=100)

        Label(self.frame, text='Full Name: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=350, y=150)
        self.ent_fullname = Entry(self.frame, textvariable=self.fullname, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_fullname.place(x=350, y=200)

        Label(self.frame, text='Email: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=350, y=250)
        self.ent_email = Entry(self.frame, textvariable=self.email, bd='2', bg='lightgrey',font=('Comic Sans MS', 14, 'bold'))
        self.ent_email.place(x=350, y=300)

        button = Button(self.frame, text='Register', command=self.reg, font=('Comic Sans MS', 14, 'bold'))
        button.place(x=370, y=350)

        # ============ FLAME FOR BUTTON===============
        self.frame2 = Frame(self.win, bg='white')
        self.frame2.place(height=100, width=750, x=300, y=760)

        Button(self.frame2, text='Clear', command=self.clear, font=('Comic Sans MS', 14, 'bold')).place(x=20, y=20, height=50,width=100)
        Button(self.frame2, text='Login', command=self.reg_signin, font=('Comic Sans MS', 14, 'bold')).place(x=200, y=20,height=50,width=150)
        Button(self.frame2, text='Exit', command=self.destroy_window, font=('Comic Sans MS', 14, 'bold')).place(x=440,y=20,height=50,width=100)

    # =========================== Register Code ============================
    def reg(self):
        reg_ref = Register(self.username.get(), self.password.get(),self.password2.get(), self.age.get(), self.address.get(),self.fullname.get(),self.email.get())
        if (reg_ref.get_username() or reg_ref.get_password() or reg_ref.get_password2() or reg_ref.get_age() or reg_ref.get_address() or reg_ref.get_fullname() or reg_ref.get_email())=='':
            Label(self.frame, text='Empty fields', bg='white', fg='red',font=('Comic Sans MS', 14, 'bold')).place(x=50, y=10)
        elif reg_ref.get_password() != reg_ref.get_password2():
            Label(self.frame, text='Confirm password does not matched', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=50,y=10)
        elif len(reg_ref.get_username()) < 5 or len(reg_ref.get_username()) > 20:
            Label(self.frame, text='Username must be between 5 to 20', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=50,y=10)
        elif len(reg_ref.get_password()) < 6 or len(reg_ref.get_password()) > 40:
            Label(self.frame, text='Password must be between 6 to 40', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=50,y=10)
        elif reg_ref.get_age() < 13:
            Label(self.frame, text='Age restriction: Age must be greater than 13', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=50,y=10)
        else:
            try:
                query = 'insert into login(username, password, age, address, fullname, email) values(%s,%s,%s,%s,%s,%s);'
                values = (reg_ref.get_username(),reg_ref.get_password(),reg_ref.get_age(),reg_ref.get_address(),reg_ref.get_fullname(),reg_ref.get_email())
                self.dbconnect.insert(query,values)
                messagebox.showinfo('Success', 'You have successfully created your account')
                self.reg_menupage()
            except IntegrityError:
                Label(self.frame, text='Username already exist', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=50,y=10)




    def clear(self):
        self.ent_user.delete(0, END)
        self.ent_pass.delete(0, END)
        self.ent_pass2.delete(0, END)
        # self.ent_age.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_email.delete(0, END)

    def destroy_window(self):
        self.win.destroy()

    def reg_signin(self):
        self.signin = SignIn(self.win)

    def reg_menupage(self):
        self.menupage = MenuPage(self.win, self.ent_user.get())


class MenuPage:
    def __init__(self, window,user):
        self.username = user
        self.win = window
        self.win.geometry('1350x1020+0+0')
        self.win.title('Home Page')
        self.win.config(bg='white')

        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        bg = Label(self.win, image=self.bg).place(relwidth=1, relheight=1)

        Label(self.win, text='Welcome: ' + self.username + ' to Freelancing Desktop Application', bg='white',
              font=('Comic Sans MS', 14, 'bold')).pack(fill=X, side=TOP)

        self.ads_logo = Image.open('../images/create_ad.png')
        self.logo_resized = self.ads_logo.resize((400, 250), Image.ANTIALIAS)
        self.ads_logo = ImageTk.PhotoImage(self.logo_resized)
        btn_ads = Button(self.win, text='Create Advertisement', image=self.ads_logo, command=self.menu_creatad,
                         font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=90, x=150)

        self.user_logo = Image.open('../images/user.png')
        self.user_logo_resized = self.user_logo.resize((400, 250), Image.ANTIALIAS)
        self.user_logo = ImageTk.PhotoImage(self.user_logo_resized)
        btn_user = Button(self.win, text='Update Profile', image=self.user_logo, command=self.menu_updatep,
                          font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=90,
                                                                                                             x=600)

        self.update_logo = Image.open('../images/setting.jpg')
        self.update_resized = self.update_logo.resize((400, 250), Image.ANTIALIAS)
        self.update_logo = ImageTk.PhotoImage(self.update_resized)
        btn_chang_pass = Button(self.win, text='Change Password', image=self.update_logo, command=self.menu_changep,
                                font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=420, x=150)

        self.logout_logo = Image.open('../images/logout.jpg')
        self.logout_resized = self.logout_logo.resize((400, 250), Image.ANTIALIAS)
        self.logout_logo = ImageTk.PhotoImage(self.logout_resized)
        btn_logout = Button(self.win, image=self.logout_logo, command=self.menu_logout,
                            font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=420,
                                                                                                               x=600)

    def menu_creatad(self):
        self.createad = MainPage(self.win, self.username)

    def menu_logout(self):
        self.logout = SignIn(self.win)

    def menu_updatep(self):
        self.updatep = UpdateProfile(self.win, self.username)

    def menu_changep(self):
        self.changep = ChangePassword(self.win, self.username)


class MainPage:
    def __init__(self, window,user):
        self.dbconnect = DbConnection()
        self.username = user
        self.win = window
        self.win.geometry('1500x1020+0+0')
        self.win.title('Freelancing Desktop Application')
        # ============BACKGROUND IMAGE===============
        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        Label(self.win, image=self.bg).place(relwidth=1, relheight=1)

        self.left_frame = Frame(self.win, bg='white')
        self.left_frame.place(height=700, width=500, x=20, y=50)

        Label(self.left_frame, text='Fill up all fields', bg='white', font=('Comic Sans MS', 16, 'bold')).pack(fill=X)
        # ============DECLARATION OF VARIABLES===============
        self.post_id = IntVar()
        self.position = StringVar()
        self.job_type = StringVar()
        self.language = StringVar()
        self.exp_time = IntVar()
        self.company = StringVar()
        # ============FORMS===============
        Label(self.left_frame, text='Post ID ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=100)
        self.ent_post_id = Entry(self.left_frame, textvariable=self.post_id, bg='lightgray', bd=2,font=('Comic Sans MS', 12, 'bold'))
        self.ent_post_id.place(x=10, y=130, height=30)

        Label(self.left_frame, text='Position', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=180)
        self.position = ttk.Combobox(self.left_frame, textvariable=self.position, font=('Comic Sans MS', 12, 'bold'))
        self.position['values'] = ('None', 'Senior Staff', 'Junior Staff', 'Web Designer', 'Web Developer', 'Other')
        self.position.current(1)
        self.position.place(x=10, y=230, height=30, width=200)

        Label(self.left_frame, text='Job Type ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=280)
        self.job_type = ttk.Combobox(self.left_frame, textvariable=self.job_type,font=('Comic Sans MS', 12, 'bold'))
        self.job_type['values'] = ('part-time', 'full-time', 'internship', 'seasonal jobs', 'contract')
        self.job_type.current(1)
        self.job_type.place(x=10, y=330, height=30, width=200)

        Label(self.left_frame, text='Programming Language ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=380)
        self.ent_language = Entry(self.left_frame, textvariable=self.language, bg='lightgray', bd=2,
                                  font=('Comic Sans MS', 12, 'bold'))
        self.ent_language.place(x=10, y=430, height=30)

        Label(self.left_frame, text='Experience Year ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10,
                                                                                                              y=480)
        self.ent_exp_time = Entry(self.left_frame, textvariable=self.exp_time, bg='lightgray', bd=2,
                                  font=('Comic Sans MS', 12, 'bold'))
        self.ent_exp_time.place(x=10, y=530, height=30)

        Label(self.left_frame, text='Company Name ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=580)
        self.ent_company = Entry(self.left_frame, bg='lightgray', textvariable=self.company, bd=2,
                                 font=('Comic Sans MS', 12, 'bold'))
        self.ent_company.place(x=10, y=630, height=30)

        # ============FLAME FOR BUTTONS===============
        self.button_frame = Frame(self.win, bg='white')
        self.button_frame.place(height=100, width=500, x=20, y=760)

        # ============BUTTONS===============
        Button(self.button_frame, text='Add', bg='white', font=('Comic Sans MS', 12, 'bold'), command=self.add).place(
            x=10, y=25, width=100)
        Button(self.button_frame, text='Update', bg='white', font=('Comic Sans MS', 12, 'bold'),
               command=self.update).place(x=130, y=25, width=100)
        Button(self.button_frame, text='Delete', bg='white', font=('Comic Sans MS', 12, 'bold'),
               command=self.delete).place(x=240, y=25, width=100)
        Button(self.button_frame, text='Clear', bg='white', font=('Comic Sans MS', 12, 'bold'),
               command=self.clear).place(x=350, y=25, width=100)

        self.search_by = StringVar()
        self.ent_search = StringVar()
        self.post_frame = Frame(self.win, bg='gray')
        self.post_frame.place(y=50, x=570, height=600, width=900)

        Label(self.post_frame, text='Search by:', bg='gray', font=('', 10, 'bold')).grid(row=1, column=0, sticky='w',
                                                                                         padx=10, pady=20)
        self.search = ttk.Combobox(self.post_frame, state='readonly', textvariable=self.search_by)
        self.search['values'] = ('language')
        self.search.current(0)
        self.search.grid(row=1, column=2, padx=10)

        self.ent_search = Entry(self.post_frame, width=20, textvariable=self.ent_search)
        self.ent_search.grid(row=1, column=3, padx=10)

        button = Button(self.post_frame, text='Search', command=self.search_data)
        button.grid(row=1, column=4, padx=10)

        button = Button(self.post_frame, text='Show All', command=self.retrieve_data)
        button.grid(row=1, column=5, padx=10)


        #==============SORTING ================================
        self.sort_by = StringVar()
        Label(self.post_frame, text='Sort by:', bg='gray', font=('', 10, 'bold')).grid(row=1, column=6, sticky='w',padx=20, pady=20)
        self.sort = ttk.Combobox(self.post_frame, state='readonly', textvariable=self.sort_by)
        self.sort['values'] = ('Post_ID')
        self.sort.current(0)
        self.sort.grid(row=1, column=7, padx=10)

        button = Button(self.post_frame, text='Sort', command=self.sorted_data)
        button.grid(row=1, column=8, padx=10)

        # =================TABLE FRAME INSIDE POST FRAME==========
        post_frame = Frame(self.post_frame, bg='white')
        post_frame.place(y=60, height=550, width=900)

        scroll_x = Scrollbar(post_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(post_frame, orient=VERTICAL)
        self.user_post = ttk.Treeview(post_frame,
                                      columns=('post_id', 'position', 'job_type', 'language', 'exp_time', 'company'),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_post.xview)
        scroll_y.config(command=self.user_post.yview)
        self.user_post.heading('post_id', text='Post ID')
        self.user_post.heading('position', text='Position')
        self.user_post.heading('job_type', text='Job Type')
        self.user_post.heading('language', text='Language')
        self.user_post.heading('exp_time', text='Experience Time')
        self.user_post.heading('company', text='Company')
        self.user_post['show'] = 'headings'
        self.user_post.column('post_id', width=50)
        self.user_post.column('position', width=150)
        self.user_post.column('job_type', width=100)
        self.user_post.column('language', width=150)
        self.user_post.column('exp_time', width=100)
        self.user_post.column('company', width=100)
        self.user_post.pack(fill=BOTH, expand=1)
        self.user_post.bind("<ButtonRelease-1>", self.get_value)
        self.retrieve_data()

        self.bottom_frame = Frame(self.win, bg='white').place(height=300, width=900, x=570, y=680)
        self.home_logo = Image.open('../images/home.png')
        self.logo_resized = self.home_logo.resize((240, 240), Image.ANTIALIAS)
        self.home_logo = ImageTk.PhotoImage(self.logo_resized)
        btn_ads = Button(self.bottom_frame, text='Back to Home', image=self.home_logo, command=self.create_menu,
                         font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=680, x=600)

        self.update_logo = Image.open('../images/setting.jpg')
        self.update_logo_resized = self.update_logo.resize((240, 240), Image.ANTIALIAS)
        self.update_logo = ImageTk.PhotoImage(self.update_logo_resized)
        btn_update = Button(self.bottom_frame, text='Change Password', image=self.update_logo, command=self.create_pass,
                            font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=680,
                                                                                                               x=900)

    def add(self):
        dr_ref = DataRecord(self.post_id.get(), self.position.get(), self.job_type.get(), self.language.get(),self.exp_time.get(), self.company.get())
        if dr_ref.get_post_id() == '' or dr_ref.get_position() == '' or dr_ref.get_job_type() == '' or dr_ref.get_language() == '' or dr_ref.get_exp_time()  == '' or dr_ref.get_company() == '':
            Label(self.left_frame, text='Empty Fields ', bg='white',fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
        
        else:
            try:
                query = 'insert into users(post_id, position, job_type, language, exp_time, company, username) values(%s, %s, %s, %s, %s, %s, %s);'
                values = (dr_ref.get_post_id(), dr_ref.get_position(), dr_ref.get_job_type(), dr_ref.get_language(),dr_ref.get_exp_time(), dr_ref.get_company(), self.username)
                self.dbconnect.insert(query, values)
                messagebox.showinfo('Success', 'You have created an Advertisement')
                self.retrieve_data()
            except IntegrityError:
                Label(self.left_frame, text='Post ID exists ', bg='white', fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=10,y=40)
            except TclError:
                Label(self.left_frame, text='Post ID must be in number ', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
            except:
                Label(self.left_frame, text='Something is wrong in fields', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
        self.retrieve_data()


    def update(self):
        dr_ref = DataRecord(self.post_id.get(), self.position.get(), self.job_type.get(), self.language.get(),self.exp_time.get(), self.company.get())
        if (dr_ref.get_post_id() or dr_ref.get_position() or dr_ref.get_job_type() or dr_ref.get_language() or dr_ref.get_exp_time() or dr_ref.get_company()) == '':
            Label(self.left_frame, text='Empty Fields ', bg='white',fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
        else:
            try:
                query = 'update users set position=%s, job_type=%s, language=%s, exp_time=%s, company=%s where post_id = %s;'
                values = (dr_ref.get_position(),dr_ref.get_job_type(), dr_ref.get_language(), dr_ref.get_exp_time(),dr_ref.get_company(), dr_ref.get_post_id())
                self.dbconnect.update(query, values)
                messagebox.showinfo('Success', 'You have successfully updated data')
            except IntegrityError:
                Label(self.left_frame, text='Post ID exists ', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
        self.retrieve_data()


    def delete(self):
        dr_ref = DataRecord(self.post_id.get(), self.position.get(), self.job_type.get(), self.language.get(),self.exp_time.get(), self.company.get())
        if (dr_ref.get_post_id() or dr_ref.get_position() or dr_ref.get_job_type() or dr_ref.get_language() or dr_ref.get_exp_time() or dr_ref.get_company()) =='':
            Label(self.left_frame, text='Empty Fields ', bg='white',fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)
        else:
            try:
                query = 'delete from users where post_id = %s;'
                values = (dr_ref.get_post_id(),)
                self.dbconnect.delete(query, values)
                messagebox.showinfo('Error', 'You have successfully deleted your record')
            except Error:
                print('Error')
        self.retrieve_data()

    def clear(self):
        self.ent_post_id.delete(0, END)
        self.position.set('None')
        self.job_type.set('None')
        self.ent_language.delete(0, END)
        self.ent_exp_time.delete(0, END)
        self.ent_company.delete(0, END)

    def retrieve_data(self):
        dr_ref = DataRecord(self.post_id.get(), self.position.get(), self.job_type.get(), self.language.get(),self.exp_time.get(), self.company.get())
        query = 'select post_id,position, job_type, language, exp_time, company from users;'
        datas = self.dbconnect.select(query)
        if len(datas) != 0:
            self.user_post.delete(*self.user_post.get_children())
            for data in datas:
                self.user_post.insert('', END, values=data)

    def search_data(self):
        query = 'select post_id, position, job_type, language, exp_time, company from users;'
        val = self.dbconnect.select(query)
        lst = []
        for i in val:
            lst.append(i[3])
        if self.linear_search(lst, self.ent_search.get()):
            query = "select post_id, position, job_type, language, exp_time, company from users where language = %s;"
            search_for = self.ent_search.get()
            item = self.dbconnect.select_value(query, (search_for,))
            if len(item) != 0:
                self.user_post.delete(*self.user_post.get_children())
                for data in item:
                    self.user_post.insert('', END, values=data)

    def sorted_data(self):
        query = 'select post_id, position, job_type, language, exp_time, company from users;'
        val = self.dbconnect.select(query)
        lsts = []
        for i in val:
            lsts.append(i[0:])
        if self.bubble_sort(lsts):
            if len(lsts) != 0:
                self.user_post.delete(*self.user_post.get_children())
                for data in lsts:
                    self.user_post.insert('', END, values=data)

    def get_value(self, event):
        de_ref = DataRecord(self.post_id.get(), self.position.get(), self.job_type.get(), self.language.get(),self.exp_time.get(), self.company.get())
        get_data = self.user_post.focus()
        content = self.user_post.item(get_data)
        row = content['values']
        self.post_id.set(row[0])
        self.position.set(row[1])
        self.job_type.set(row[2])
        self.language.set(row[3])
        self.exp_time.set(row[4])
        self.company.set(row[5])
        query = 'select post_id,position, job_type, language, exp_time, company from users;'
        datas = self.dbconnect.select(query)
        if len(datas) != 0:
            self.user_post.delete(*self.user_post.get_children())
            for data in datas:
                self.user_post.insert('', END, values=data)
                self.retrieve_data()
        else:
            Label(self.left_frame, text='Already deleted ', bg='white', fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=10, y=40)

    def create_menu(self):
        return MenuPage(self.win, self.username)

    def create_pass(self):
        return ChangePassword(self.win, self.username)

    @classmethod
    def linear_search(self, lst, name):
        for i in lst:
            if name == i:
                return True
        return False

    @classmethod
    def bubble_sort(self, lsts):
        n = len(lsts)
        for i in range(n):
            sorted = True
            for j in range(n - i - 1):
                if lsts[j] > lsts[j + 1]:
                    lsts[j], lsts[j + 1] = lsts[j + 1], lsts[j]
                    sorted = False
            if sorted:
                break
        return lsts


class ChangePassword:
    def __init__(self, window, user):
        self.username = user
        self.dbconnect = DbConnection()
        self.win = window
        self.win.title('Change Password')
        self.win.geometry('1350x1020+0+0')
        # ============BACKGROUND IMAGE===============
        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        bg = Label(self.win, image=self.bg).place(relwidth=1, relheight=1)

        self.side_frame = Frame(self.win, bg='white')
        self.side_frame.place(height=800, width=350, x=990, y=100)

        self.home_logo = Image.open('../images/home.png')
        self.logo_resized = self.home_logo.resize((300, 300), Image.ANTIALIAS)
        self.home_logo = ImageTk.PhotoImage(self.logo_resized)
        btn_ads = Button(self.side_frame, text='Back to Home', image=self.home_logo, command=self.change_menu,
                         font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=10, x=20)

        self.update_logo = Image.open('../images/user.png')
        self.update_logo_resized = self.update_logo.resize((300, 300), Image.ANTIALIAS)
        self.update_logo = ImageTk.PhotoImage(self.update_logo_resized)
        btn_update = Button(self.side_frame, text='Update Profile', image=self.update_logo, command=self.chng_up,
                            font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=400,
                                                                                                               x=20)

        self.old_password = StringVar()
        self.new_password = StringVar()
        self.conf_password = StringVar()

        self.frame = Frame(self.win, bg='white')
        self.frame.place(x=80, y=80, height=500, width=600)

        Label(self.frame, text='Old Password: ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=50, y=100)
        self.ent_old_pass = Entry(self.frame, show='*', font=('Comic Sans MS', 12, 'bold'),
                                  textvariable=self.old_password, bd='2', bg='lightgrey')
        self.ent_old_pass.place(x=300, y=100)

        Label(self.frame, text='New Password:', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=50, y=150)
        self.ent_new_pass = Entry(self.frame, show='*', font=('Comic Sans MS', 12, 'bold'),
                                  textvariable=self.new_password, bd='2', bg='lightgrey')
        self.ent_new_pass.place(x=300, y=150)

        Label(self.frame, text='Confirm New Password: ', bg='white', font=('Comic Sans MS', 12, 'bold')).place(x=50,
                                                                                                               y=200)
        self.ent_conf_pass = Entry(self.frame, show='*', font=('Comic Sans MS', 12, 'bold'),
                                   textvariable=self.conf_password, bd='2', bg='lightgrey')
        self.ent_conf_pass.place(x=300, y=200)

        btn_chng = Button(self.frame, text='Change Password', command=self.update_pass,
                          font=('Comic Sans MS', 12, 'bold'))
        btn_chng.place(x=300, y=250)

    # =========================== Code for update password  ============================
    def update_pass(self):
        new_password = self.new_password.get()
        conf_password = self.conf_password.get()
        chng_ref = Login(self.username, self.old_password.get())
        if (chng_ref.get_password() or new_password or conf_password) == '':
            Label(self.frame, text='Empty Fields', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=50, y=50)
        elif len(new_password) < 6 or len(new_password) > 40:
            Label(self.frame, text='Password must be between 6 to 40', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=50, y=50)
        else:
            query = 'select password from login where username = %s;'
            values = (chng_ref.get_username(),)
            datas = self.dbconnect.select_value(query, values)
            for data in datas:
                if data[0] == chng_ref.get_password():
                    if new_password == conf_password:
                        if data[0] != new_password and data[0] != conf_password:
                            query = 'update login set password=%s where username = %s;'
                            values = (new_password, self.username)
                            self.dbconnect.update(query,values)
                            messagebox.showinfo('Success','You have successfully updated your password')
                            self.change_menu()
                        else:
                            Label(self.frame, text='You cannot keep same password', bg='white', fg='red',font=('Comic Sans MS', 12, 'bold')).place(x=50, y=50)
                    else:
                        Label(self.frame, text='Confirm Password does not match', bg='white',fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=50, y=50)

                else:
                    Label(self.frame, text='Old Password does not match ', bg='white',fg='red', font=('Comic Sans MS', 12, 'bold')).place(x=50, y=50)



    def change_menu(self):
        menu = MenuPage(self.win, self.username)

    def chng_up(self):
        update = UpdateProfile(self.win, self.username)


class UpdateProfile:
    def __init__(self, window, user):
        self.username = user
        self.dbconnect = DbConnection()
        self.win = window
        self.win.geometry('1350x1020+0+0')
        self.win.title('User Profile')
        # ============BACKGROUND IMAGE===============
        self.bg = ImageTk.PhotoImage(file='../images/bg.jpg')
        bg = Label(self.win, image=self.bg).place(relwidth=1, relheight=1)

        # =========SIDE BUTTON==========
        self.side_frame = Frame(self.win, bg='white')
        self.side_frame.place(height=600, width=350, x=990, y=200)

        self.update_home_logo = Image.open('../images/home.png')
        self.logo_resized = self.update_home_logo.resize((300, 300), Image.ANTIALIAS)
        self.update_home_logo = ImageTk.PhotoImage(self.logo_resized)
        btn_ads = Button(self.side_frame, text='Back to Home', image=self.update_home_logo, command=self.update_home,
                         font=('Comic Sans MS', 14, 'bold'), bg='white', borderwidth=0, compound=TOP).place(y=10, x=20)

        self.frame = Frame(self.win, bg='white')
        self.frame.place(height=600, width=450, x=30, y=200)

        self.user_logo = Image.open('../images/user.png')
        self.user_logo_resized = self.user_logo.resize((400, 300), Image.ANTIALIAS)
        self.user_logo = ImageTk.PhotoImage(self.user_logo_resized)
        Label(self.frame, image=self.user_logo).place(x=20, y=10)
        self.user_profile()

        # ========== UPDATE PROFILE FORM==================
        self.frame2 = Frame(self.win, bg='white')
        self.frame2.place(height=600, width=450, x=500, y=200)

        self.age = IntVar()
        self.address = StringVar()
        self.fullname = StringVar()
        self.email = StringVar()

        Label(self.frame2, text='Full Name: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=100)
        self.ent_fname = Entry(self.frame2, textvariable=self.fullname, bd='2', bg='lightgrey',
                               font=('Comic Sans MS', 14, 'bold'))
        self.ent_fname.place(x=100, y=150)

        Label(self.frame2, text='Age: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=200)
        self.ent_age = Entry(self.frame2, textvariable=self.age, bd='2', bg='lightgrey',
                             font=('Comic Sans MS', 14, 'bold'))
        self.ent_age.place(x=100, y=250)

        Label(self.frame2, text='Address: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=300)
        self.ent_address = Entry(self.frame2, textvariable=self.address, bd='2', bg='lightgrey',
                                 font=('Comic Sans MS', 14, 'bold'))
        self.ent_address.place(x=100, y=350)

        Label(self.frame2, text='Email: ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=400)
        self.ent_email= Entry(self.frame2, textvariable=self.email, bd='2', bg='lightgrey',
                                 font=('Comic Sans MS', 14, 'bold'))
        self.ent_email.place(x=100, y=450)

        Button(self.frame2, text='Update ', command=self.update_profile, font=('Comic Sans MS', 14, 'bold')).place(
            x=100, y=500, height=50, width=100)
        Button(self.frame2, text='Clear', command=self.clear, font=('Comic Sans MS', 14, 'bold')).place(x=220, y=500,
                                                                                                        height=50,
                                                                                                        width=150)

    def user_profile(self):
        query = 'select username, age, address,fullname, email from login where username = %s;'
        values = (self.username,)
        result = self.dbconnect.select_value(query, values)
        for user in result:
            Label(self.frame, text='Username: ' + user[0], bg='white', fg='black', font=('', 14, 'bold'),
                  justify=LEFT).place(x=20, y=340)
            Label(self.frame, text='Fullname: ' + user[3], bg='white', fg='black', font=('', 14, 'bold'),
                  justify=LEFT).place(x=20, y=380)
            Label(self.frame, text='Age: ' + str(user[1]), bg='white', fg='black', font=('', 14, 'bold'),
                  justify=LEFT).place(x=20, y=420)
            Label(self.frame, text='Address: ' + user[2], bg='white', fg='black', font=('', 14, 'bold'),
                  justify=LEFT).place(x=20, y=460)

    def update_profile(self):
        pro_ref = ChangeProfile(self.username, self.age.get(),self.address.get(),self.fullname.get(),self.email.get())
        if pro_ref.get_age() =='' or pro_ref.get_address()== '' or pro_ref.get_address()=='' or pro_ref.get_email()=='':
            Label(self.frame2, text='Empty Fields ', bg='white',fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=50)
        elif pro_ref.get_age() < 13:
            Label(self.frame2, text='Age must be 13 or above ', bg='white', fg='red', font=('Comic Sans MS', 14, 'bold')).place(x=100, y=50)
        else:
            try:
                query = 'update login set age=%s, fullname=%s, address=%s, email=%s where username=%s;'
                values = (pro_ref.get_age(),pro_ref.get_fullname(), pro_ref.get_address(), pro_ref.get_email(), pro_ref.get_username())
                self.dbconnect.update(query,values)
                messagebox.showinfo('Success', 'Successfully updated')
                self.update_home()
            except:
                Label(self.frame2, text='Something error ', bg='white', font=('Comic Sans MS', 14, 'bold')).place(x=100,y=50)



    def clear(self):
        self.ent_fname.delete(0, END)
        self.ent_age.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_email.delete(0, END)

    def update_home(self):
        home = MenuPage(self.win, self.username)


root = Tk()
obj = SignIn(root)
root.mainloop()
