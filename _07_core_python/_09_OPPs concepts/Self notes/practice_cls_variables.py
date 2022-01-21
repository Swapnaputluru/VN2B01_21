print("Without class variables")


class StudentDetails:
    def __init__(self, student_name, student_id, branch, year, college_name):
        self.student_name = student_name
        self.student_id = student_id
        self.branch = branch
        self.year = year
        self.college_name = college_name

    def display(self):
        print("Details of student", self.student_name, self.student_id, self.branch, self.year,self.college_name)

    def Year(self,year):
        if year == 4:
            print("Eligible for placements")
        else:
            print("You have to wait till 4th year for placements")


s1 = StudentDetails("swapna", 14, "civil", 4, "JNTUA")
s1.display()
y1 =s1.year
print("Pursuing year is:", y1)
s1.Year(y1)


s1 = StudentDetails("Tommy", 1426, "EEE", 2, "KSRM")
s1.display()
y1 =s1.year
print("Pursuing year is:", y1)
s1.Year(y1)

print("Without class variables")


class BankDetails:
    coun = "India"

    def __init__(self, bank_name,bank_area, state):
        self.bank_name = bank_name
        self.bank_area = bank_area
        self.state = state

    def country(self):
        print("Bank details:", self.bank_name, self.bank_area,self.state,BankDetails.coun)


b1 = BankDetails("Canara Bank,", "Bangulore,", "Karnataka,")
b1.country()

b2 = BankDetails("ICICI Bank,", "Anantapur,", "Andhra Pradesh,")
b2.country()











