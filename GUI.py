from tkinter import *
from tkcalendar import Calendar, DateEntry
import main
import school_database

root = Tk()
root.geometry("400x600")
root.title("School Personnel Database")
root.config(bg='DeepSkyBlue4')


img = PhotoImage(file="UniversityLogo.png")
img = img.subsample(5, 4)                           # subsample shrinks the image, in this case by 4x


frame1 = LabelFrame(root, padx=5, pady=5)
frame1.config(bg='gold')
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, padx=5, pady=5)
frame2.config(bg='gold')
frame2.grid(row=1, column=0, padx=10, pady=10)

frame3 = LabelFrame(root, padx=5, pady=5)
frame3.config(bg='gold')
frame3.grid(row=2, column=0, padx=10, pady=10)

frame4 = LabelFrame(root, padx=5, pady=5)
frame4.config(bg='DeepSkyBlue4')

frame4a = LabelFrame(root, padx=5, pady=5)
frame4a.config(bg='gold')

new_person_frame = LabelFrame(root, padx=5, pady=5)
new_student_frame = LabelFrame(root, padx=5, pady=5)
new_faculty_frame = LabelFrame(root, padx=5, pady=5)
new_staff_frame = LabelFrame(root, padx=5, pady=5)

frame6 = LabelFrame(root, padx=5, pady=5)

frame7 = LabelFrame(root, padx=5, pady=5)

frame8 = LabelFrame(root, padx=5, pady=5)


a = StringVar()
a1 = StringVar()
a2 = StringVar()

b = StringVar()
b1 = StringVar()
b2 = StringVar()

c = StringVar()
d = StringVar()

e = StringVar()
e1 = StringVar()

f = StringVar()
f1 = StringVar()

g = StringVar()
h = StringVar()

i = StringVar()
i1 = StringVar()

j = StringVar()

k = StringVar()
k1 = StringVar()
k2 = StringVar()

ll = StringVar()


student_fnlab = Label(new_student_frame, text="First Name")
faculty_fnlab = Label(new_faculty_frame, text="First Name")
staff_fnlab = Label(new_staff_frame, text="First Name")

student_lnlab = Label(new_student_frame, text="Last Name")
faculty_lnlab = Label(new_faculty_frame, text="Last Name")
staff_lnlab = Label(new_staff_frame, text="Last Name")

major_lab = Label(new_student_frame, text="Major")

grad_year_lab = Label(new_student_frame, text="Grad. Year")
gpa_lab = Label(new_student_frame, text="GPA")

faculty_dept_lab = Label(new_faculty_frame, text="Department")
staff_dept_lab = Label(new_staff_frame, text="Department")

faculty_start_date_lab = Label(new_faculty_frame, text="Start Date")
staff_start_date_lab = Label(new_staff_frame, text="Start Date")

is_adjunct_lab = Label(new_faculty_frame, text="Adjunct")
tenured_lab = Label(new_faculty_frame, text="Is Tenured")

faculty_salary_lab = Label(new_faculty_frame, text="Salary")
staff_salary_lab = Label(new_staff_frame, text="Salary")

position_lab = Label(new_staff_frame, text="Position")

student_email_lab = Label(new_student_frame, text="Email")
faculty_email_lab = Label(new_faculty_frame, text="Email")
staff_email_lab = Label(new_staff_frame, text="Email")


subject_list = ["African American Studies", "Anthropology", "Architecture", "Art", "Biology", "Biomedical Engineering",
                "Chemical Engineering", "Chemistry", "Civil Engineering", "Classics", "Communications",
                "Comparative Literature", "Computer Science", "Dentistry", "Economics", "Education",
                "Electrical Engineering", "English", "Environmental Sciences", "Geography", "Geology",
                "Gender Studies", "History", "Industrial Engineering", "Jewish Studies", "Law", "Linguistics",
                "Mathematics", "Mechanical Engineering", "Media Studies", "Medicine", "Music", "Nursing",
                "Pharmaceutical Science", "Philosophy", "Physics", "Political Science", "Psychology", "Social Work",
                "Sociology", "Theater and Dance"]


student_fn_ent = Entry(new_student_frame, text="First Name", textvariable=a)
faculty_fn_ent = Entry(new_faculty_frame, text="First Name", textvariable=a1)
staff_fn_ent = Entry(new_staff_frame, text="First Name", textvariable=a2)

student_ln_ent = Entry(new_student_frame, text="First Name", textvariable=b)
faculty_ln_ent = Entry(new_faculty_frame, text="First Name", textvariable=b1)
staff_ln_ent = Entry(new_staff_frame, text="First Name", textvariable=b2)

major_drop = OptionMenu(new_student_frame, ll, *subject_list)

grad_year_ent = Entry(new_student_frame, text="Grad. Year", textvariable=c)
gpa_ent = Entry(new_student_frame, text="GPA", textvariable=d)

# faculty_dept_ent = Entry(new_faculty_frame, text="Department", textvariable=e)
# staff_dept_ent = Entry(new_staff_frame, text="Department", textvariable=e1)
faculty_dept_drop = OptionMenu(new_faculty_frame, e, *subject_list)
staff_dept_drop = OptionMenu(new_staff_frame, e1, *subject_list)

faculty_start_date_ent = DateEntry(new_faculty_frame, locale='en_US', date_pattern='mm/dd/yyyy', textvariable=f)
staff_start_date_ent = DateEntry(new_staff_frame, locale='en_US', date_pattern='mm/dd/yyyy', textvariable=f1)

# is_adjunct_ent = Entry(frame5, text="Adjunct", textvariable=g)
# tenured_ent = Entry(new_faculty_frame, text="Is Tenured", textvariable=h)

is_adjunct_drop = OptionMenu(new_faculty_frame, g, "Yes", "No")
is_tenured_drop = OptionMenu(new_faculty_frame, h, "Yes", "No")

faculty_salary_ent = Entry(new_faculty_frame, text="Salary", textvariable=i)
staff_salary_ent = Entry(new_staff_frame, text="Salary", textvariable=i1)

position_ent = Entry(new_staff_frame, text="Position", textvariable=j)

student_email_ent = Entry(new_student_frame, text="Email", textvariable=k)
faculty_email_ent = Entry(new_faculty_frame, text="Email", textvariable=k1)
staff_email_ent = Entry(new_staff_frame, text="Email", textvariable=k2)


def validate_student(*args):
    global a
    global b
    global c
    global d
    global k
    global ll

    if a.get() == '' or b.get() == '' or c.get() == '' or d.get() == '' or k.get() == '' or ll.get() == '':
        submit_student_but.configure(state=DISABLED)
    else:
        submit_student_but.configure(state=NORMAL)


def validate_faculty(*args):
    global a1
    global b1
    global e
    global f
    global g
    global h
    global i
    global k1

    if a1.get() == '' or b1.get() == '' or e.get() == '' or f.get() == ''\
            or g.get() == '' or h.get() == '' or i.get() == '' or k1.get() == '':
        submit_faculty_but.configure(state=DISABLED)
    else:
        submit_faculty_but.configure(state=NORMAL)


def validate_staff(*args):
    global a2
    global b2
    global e1
    global f1
    global i1
    global j
    global k2

    if a2.get() == '' or b2.get() == '' or e1.get() == '' or f1.get() == '' or i1.get() == '' or j.get() == '' \
            or k2.get() == '':
        submit_staff_but.configure(state=DISABLED)
    else:
        submit_staff_but.configure(state=NORMAL)


def new_person():
    global frame1
    global frame2
    global frame3
    global frame4
    global frame4a

    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()

    frame4.pack(padx=10, pady=10)
    frame4.config(bg='gold')

    frame4a.pack(padx=10, pady=10)
    frame4a.config(bg='gold')

    canvas4.grid(row=0, columnspan=3)
    canvas4.create_image(105, 100, image=img)

    new_student_but.grid(row=1, column=0)
    new_faculty_but.grid(row=1, column=1)
    new_staff_but.grid(row=1, column=2)


def new_student():
    global frame4
    global frame4a
    global new_student_frame

    frame4.pack_forget()
    frame4a.pack_forget()
    new_student_frame.grid()

    student_fnlab.grid(row=0, column=0)
    student_lnlab.grid(row=1, column=0)
    major_lab.grid(row=2, column=0)
    grad_year_lab.grid(row=3, column=0)
    gpa_lab.grid(row=4, column=0)
    student_email_lab.grid(row=5, column=0)

    student_fn_ent.grid(row=0, column=1)
    student_ln_ent.grid(row=1, column=1)
    major_drop.grid(row=2, column=1)
    ll.set(subject_list[0])
    grad_year_ent.grid(row=3, column=1)
    gpa_ent.grid(row=4, column=1)
    student_email_ent.grid(row=5, column=1)

    a.trace('w', validate_student)
    b.trace('w', validate_student)
    c.trace('w', validate_student)
    d.trace('w', validate_student)
    k.trace('w', validate_student)
    ll.trace('w', validate_student)

    submit_student_but.grid(row=6, column=1)
    home_but_student.grid(row=6, column=2)


def new_faculty():
    global frame4
    global frame4a
    global new_faculty_frame

    frame4.pack_forget()
    frame4a.pack_forget()
    new_faculty_frame.grid()

    faculty_fnlab.grid(row=0, column=0)
    faculty_lnlab.grid(row=1, column=0)
    faculty_dept_lab.grid(row=2, column=0)
    faculty_start_date_lab.grid(row=3, column=0)
    is_adjunct_lab.grid(row=4, column=0)
    tenured_lab.grid(row=5, column=0)
    faculty_salary_lab.grid(row=6, column=0)
    faculty_email_lab.grid(row=7, column=0)

    faculty_fn_ent.grid(row=0, column=1)
    faculty_ln_ent.grid(row=1, column=1)
    faculty_dept_drop.grid(row=2, column=1)
    e.set(subject_list[0])
    faculty_start_date_ent.grid(row=3, column=1, ipadx=29)
    is_adjunct_drop.grid(row=4, column=1, ipadx=69)
    g.set("Yes")
    is_tenured_drop.grid(row=5, column=1, ipadx=69)
    h.set("No")
    faculty_salary_ent.grid(row=6, column=1)
    faculty_salary_ent.insert(0, "$")
    faculty_email_ent.grid(row=7, column=1)

    submit_faculty_but.grid(row=8, column=1)
    home_but_faculty.grid(row=8, column=2)

    a1.trace('w', validate_faculty)
    b1.trace('w', validate_faculty)
    e.trace('w', validate_faculty)
    f.trace('w', validate_faculty)
    g.trace('w', validate_faculty)
    h.trace('w', validate_faculty)
    i.trace('w', validate_faculty)
    k1.trace('w', validate_faculty)


def new_staff():
    global frame4
    global new_staff_frame

    frame4.pack_forget()
    frame4a.pack_forget()
    new_staff_frame.grid()

    staff_fnlab.grid(row=0, column=0)
    staff_lnlab.grid(row=1, column=0)
    staff_dept_lab.grid(row=2, column=0)
    staff_start_date_lab.grid(row=3, column=0)
    position_lab.grid(row=4, column=0)
    staff_salary_lab.grid(row=5, column=0)
    staff_email_lab.grid(row=6, column=0)

    staff_fn_ent.grid(row=0, column=1)
    staff_ln_ent.grid(row=1, column=1)
    staff_dept_drop.grid(row=2, column=1)
    e1.set(subject_list[0])
    staff_start_date_ent.grid(row=3, column=1, ipadx=29)
    position_ent.grid(row=4, column=1)
    staff_salary_ent.grid(row=5, column=1)
    staff_salary_ent.insert(0, "$")
    staff_email_ent.grid(row=6, column=1)

    submit_staff_but.grid(row=7, column=1)
    home_but_staff.grid(row=7, column=2)

    a2.trace('w', validate_staff)
    b2.trace('w', validate_staff)
    e1.trace('w', validate_staff)
    f1.trace('w', validate_staff)
    i1.trace('w', validate_staff)
    j.trace('w', validate_staff)
    k2.trace('w', validate_staff)


def submit_student():
    s1 = main.student(student_fn_ent.get(), student_ln_ent.get(), ll.get(), grad_year_ent.get(), gpa_ent.get(),
                      student_email_ent.get())
    s2 = [student_fn_ent.get(), student_ln_ent.get(), ll.get(), grad_year_ent.get(), gpa_ent.get(), student_email_ent.get()]

    # main.write_student(s1)
    school_database.insert_to_database("student", s2)

    student_fn_ent.delete(0, 'end')
    student_ln_ent.delete(0, 'end')
    ll.set(subject_list[0])
    grad_year_ent.delete(0, 'end')
    gpa_ent.delete(0, 'end')
    student_email_ent.delete(0, 'end')


def submit_faculty():
    fac1 = None
    fac2 = None
    if list(faculty_salary_ent.get())[0] == "$":
        fac1 = main.faculty(faculty_fn_ent.get(), faculty_ln_ent.get(), e.get(), str(faculty_start_date_ent.get_date()),
                            g.get(), h.get(), faculty_salary_ent.get(), faculty_email_ent.get())
        fac2 = [faculty_fn_ent.get(), faculty_ln_ent.get(), e.get(), str(faculty_start_date_ent.get_date()),
                            g.get(), h.get(), faculty_salary_ent.get(), faculty_email_ent.get()]
    elif list(faculty_salary_ent.get())[0] != "$":
        fac1 = main.faculty(faculty_fn_ent.get(), faculty_ln_ent.get(), e.get(), str(faculty_start_date_ent.get_date()),
                            g.get(), h.get(), "$" + faculty_salary_ent.get(), faculty_email_ent.get())
        fac2 = [faculty_fn_ent.get(), faculty_ln_ent.get(), e.get(), str(faculty_start_date_ent.get_date()),
                            g.get(), h.get(), "$" + faculty_salary_ent.get(), faculty_email_ent.get()]

    # main.write_faculty(fac1)
    school_database.insert_to_database("faculty", fac2)

    faculty_fn_ent.delete(0, 'end')
    faculty_ln_ent.delete(0, 'end')
    e.set(subject_list[0])
    faculty_start_date_ent.delete(0, 'end')
    g.set("Yes")
    h.set("No")
    faculty_salary_ent.delete(0, 'end')
    faculty_email_ent.delete(0, 'end')


def submit_staff():
    st = None
    st2 = None
    if list(staff_salary_ent.get())[0] == "$":
        st = main.staff(staff_fn_ent.get(), staff_ln_ent.get(), e1.get(), str(staff_start_date_ent.get_date()),
                        position_ent.get(), str(staff_salary_ent.get()), staff_email_ent.get())
        st2 = [staff_fn_ent.get(), staff_ln_ent.get(), e1.get(), str(staff_start_date_ent.get_date()),
               position_ent.get(), str(staff_salary_ent.get()), staff_email_ent.get()]
    elif list(staff_salary_ent.get())[0] != "$":
        st = main.staff(staff_fn_ent.get(), staff_ln_ent.get(), e1.get(), str(staff_start_date_ent.get_date()),
                        position_ent.get(), "$" + str(staff_salary_ent.get()), staff_email_ent.get())
        st2 = [staff_fn_ent.get(), staff_ln_ent.get(), e1.get(), str(staff_start_date_ent.get_date()),
               position_ent.get(), "$" + str(staff_salary_ent.get()), staff_email_ent.get()]

    # main.write_staff(st)
    school_database.insert_to_database("staff", st2)

    staff_fn_ent.delete(0, 'end')
    staff_ln_ent.delete(0, 'end')
    e1.set(subject_list[0])
    staff_start_date_ent.delete(0, 'end')
    position_ent.delete(0, 'end')
    staff_salary_ent.delete(0, 'end')
    staff_email_ent.delete(0, 'end')


def show_lists():
    global frame1
    global frame2
    global frame3
    global frame4
    global frame4a

    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()

    frame4.pack(padx=10, pady=10)
    frame4.config(bg='gold')

    frame4a.pack(padx=10, pady=10)
    frame4a.config(bg='gold')

    canvas4.grid(row=0, columnspan=3)
    canvas4.create_image(105, 100, image=img)

    student_list_but.grid(row=1, column=0)
    faculty_list_but.grid(row=1, column=1)
    staff_list_but.grid(row=1, column=2)


def student_list():
    root.geometry("")

    global frame4
    global new_person_frame
    global frame6
    global frame7
    global frame8

    frame4.pack_forget()
    frame4a.pack_forget()
    new_person_frame.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()

    frame6.grid()

    list_of_students = []
    x = school_database.fetch("student")
    for ii in x:
        stu = main.student(ii[0], ii[1], ii[2], ii[3], ii[4], ii[5])
        stu_name = stu.name()
        stu_inf = stu.student_info()
        student = stu_name + ", " + stu_inf
        list_of_students.append(student)

    txt = Label(frame6, bg='DeepSkyBlue4', fg='MidnightBlue', font=('Times', 14, 'bold'),
                text="\n".join(list_of_students))
    txt.grid(row=0, column=0)

    home_but_6.grid(row=1, column=0)


def faculty_list():
    root.geometry("")

    global frame4
    global new_person_frame
    global frame6
    global frame7
    global frame8

    frame4.pack_forget()
    frame4a.pack_forget()
    new_person_frame.grid_forget()
    frame6.grid_forget()
    frame8.grid_forget()

    frame7.grid()

    list_of_faculty = []
    x = school_database.fetch("faculty")
    for ii in x:
        fac = main.faculty(ii[0], ii[1], ii[2], ii[3], ii[4], ii[5], ii[6], ii[7])
        fac_name = fac.name()
        fac_inf = fac.faculty_info()
        faculty = fac_name + ", " + fac_inf
        list_of_faculty.append(faculty)

    txt1 = Label(frame7, bg='DeepSkyBlue4', fg='MidnightBlue', font=('Times', 14, 'bold'),
                 text="\n".join(list_of_faculty))
    txt1.grid(row=0, column=0)

    home_but_7.grid(row=1, column=0)


def staff_list():
    root.geometry("")

    global frame4
    global new_person_frame
    global frame6
    global frame7
    global frame8

    frame4.pack_forget()
    frame4a.pack_forget()
    new_person_frame.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()

    frame8.grid()

    list_of_staff = []
    x = school_database.fetch("staff")
    for ii in x:
        staff = main.staff(ii[0], ii[1], ii[2], ii[3], ii[4], ii[5], ii[6])
        staff_name = staff.name()
        staff_inf = staff.staff_info()
        staff = staff_name + ", " + staff_inf
        list_of_staff.append(staff)

    txt2 = Label(frame8, bg='DeepSkyBlue4', fg='MidnightBlue', font=('Times', 14, 'bold'),
                 text="\n".join(list_of_staff))
    txt2.grid(row=0, column=0)

    home_but_8.grid(row=1, column=0)


def home():
    global frame1
    global frame2
    global frame3
    global new_student_frame
    global new_faculty_frame
    global new_staff_frame
    global frame6
    global frame7
    global frame8

    frame4.pack_forget()
    frame4a.pack_forget()
    new_student_frame.grid_forget()
    new_faculty_frame.grid_forget()
    new_staff_frame.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()

    root.geometry("400x600")

    frame1.grid(row=0, column=0, padx=10, pady=10)
    frame2.grid(row=1, column=0, padx=10, pady=10)
    frame3.grid(row=2, column=0, padx=10, pady=10)

    # is_adjunct_drop.grid_forget()

    # frame6.forget()

    home_but_student.grid_forget()
    home_but_faculty.grid_forget()
    home_but_staff.grid_forget()

    submit_student_but.grid_forget()
    submit_faculty_but.grid_forget()
    submit_staff_but.grid_forget()

    student_list_but.grid_forget()
    faculty_list_but.grid_forget()
    staff_list_but.grid_forget()

    student_fn_ent.delete(0, 'end')
    faculty_fn_ent.delete(0, 'end')
    staff_fn_ent.delete(0, 'end')
    student_ln_ent.delete(0, 'end')
    faculty_ln_ent.delete(0, 'end')
    staff_ln_ent.delete(0, 'end')
    grad_year_ent.delete(0, 'end')
    gpa_ent.delete(0, 'end')
    faculty_dept_drop.grid_forget()
    staff_dept_drop.grid_forget()
    faculty_start_date_ent.delete(0, 'end')
    staff_start_date_ent.delete(0, 'end')
    # is_adjunct_drop.delete(0, 'end')
    # is_tenured_drop.delete(0, 'end')
    faculty_salary_ent.delete(0, 'end')
    staff_salary_ent.delete(0, 'end')
    position_ent.delete(0, 'end')
    student_email_ent.delete(0, 'end')
    faculty_email_ent.delete(0, 'end')
    staff_email_ent.delete(0, 'end')


add_new_but = Button(frame3, text="New Entry", command=new_person)
add_new_but.grid(row=0, column=0, padx=5)

see_list_but = Button(frame3, text="See Lists", command=show_lists)
see_list_but.grid(row=0, column=1, padx=5)

new_student_but = Button(frame4a, text="New Student", command=new_student)
new_faculty_but = Button(frame4a, text="New Faculty", command=new_faculty)
new_staff_but = Button(frame4a, text="New Staff", command=new_staff)

submit_student_but = Button(new_student_frame, text="Submit", state=DISABLED, command=submit_student)
submit_faculty_but = Button(new_faculty_frame, text="Submit", state=DISABLED, command=submit_faculty)
submit_staff_but = Button(new_staff_frame, text="Submit", state=DISABLED, command=submit_staff)

student_list_but = Button(frame4a, text="Student List", command=student_list)
faculty_list_but = Button(frame4a, text="Faculty List", command=faculty_list)
staff_list_but = Button(frame4a, text="Staff List", command=staff_list)

home_but_student = Button(new_student_frame, text="Home", command=home)
home_but_faculty = Button(new_faculty_frame, text="Home", command=home)
home_but_staff = Button(new_staff_frame, text="Home", command=home)

home_but_6 = Button(frame6, text="Home", command=home)
home_but_7 = Button(frame7, text="Home", command=home)
home_but_8 = Button(frame8, text="Home", command=home)


canvas = Canvas(frame2, width=200, height=200)
canvas.pack(expand=YES, fill=BOTH)
canvas.create_image(105, 100, image=img)            # first two numbers are coordinates for the image

canvas4 = Canvas(frame4, width=200, height=200)


lab1 = Label(frame1, text="Welcome to Sample School Database",
             font=('Times', 22, 'bold'), bg='DeepSkyBlue3', fg='gold')
lab1.grid(row=0, column=0)


root.mainloop()
