class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def name(self):
        a = "Name: " + self.fname + " " + self.lname
        return a


class student(person):
    def __init__(self, fname, lname, major, grad_year, gpa, email):
        super().__init__(fname, lname)
        self.major = major
        self.grad_year = grad_year
        self.gpa = gpa
        self.email = email

    def student_info(self):
        b = "Major: " + self.major + ", Graduation Year: " + self.grad_year + ", GPA: " + self.gpa + ", Email: " + self.email
        return b


class faculty(person):
    def __init__(self, fname, lname, department, start_date, is_adjunct, is_tenured, salary, email):
        super().__init__(fname, lname)
        self.department = department
        self.start_date = start_date
        self.is_adjunct = is_adjunct
        self.is_tenured = is_tenured
        self.salary = salary
        self.email = email

    def faculty_info(self):
        c = "Department: " + self.department + ", Start Date: " + self.start_date + ", Adjunct: " + self.is_adjunct + \
            ", Tenured: " + self.is_tenured + ", Salary: " + self.salary + ", Email: " + self.email
        return c


class staff(person):
    def __init__(self, fname, lname, department, start_date, position, salary, email):
        super().__init__(fname, lname)
        self.department = department
        self.start_date = start_date
        self.position = position
        self.salary = salary
        self.email = email

    def staff_info(self):
        d = "Department: " + self.department + ", Start Date: " + self.start_date + \
            ", Position: " + self.position + ", Salary: " + self.salary + ", Email: " + self.email
        return d


def write_student(x):
    name = x.name()
    info = x.student_info()
    total = name + ", " + info
    with open('Lists/Student_List.txt', 'a') as f:
        f.write(total + "\n")


def write_faculty(x):
    name = x.name()
    info = x.faculty_info()
    total = name + ", " + info
    with open('Lists/Faculty_List.txt', 'a') as f:
        f.write(total + "\n")


def write_staff(x):
    name = x.name()
    info = x.staff_info()
    total = name + ", " + info
    with open('Lists/Staff_List.txt', 'a') as f:
        f.write(total + "\n")


def read_lists(name):
    with open(name, 'r') as f:
        x = f.read()
        return x

