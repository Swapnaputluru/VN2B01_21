print("-----------------With class method----------------------")

class Sachivalayam:

    job_type = "Temporary"
    salary = 15000

    def __init__(self, job_role, area):
        self.job_role = job_role
        self.area = area

    def display(self):
        print("instance and class variables are printed:", self.job_role,self.area,Sachivalayam.salary,Sachivalayam.job_type)

#  class variables we will print by using class name

    @classmethod
    def govt(cls):
        print("Only class variables print:", cls.salary, cls.job_type)


s1= Sachivalayam("Assistant Engineer,", "Tadpatri,")
s1.display()  # we will get both class variables and instance variables in instance method
Sachivalayam.govt()  # only get class variables in class method
print("--------------")
s2= Sachivalayam("Survivor,", "Chitoor,")
s2.display()
Sachivalayam.govt()
print("--------------")
s3= Sachivalayam("Digital Assistant,", "Karnool,")
s3.display()
Sachivalayam.govt()

print("-----------------With class method----------------------")


class FeeReimbursement:
    def __init__(self, name, father_occupation, annual_income):
        self.name = name
        self.father_occupation = father_occupation
        self.annual_income = annual_income

    def display(self):
        print(self.name,self.father_occupation, self.annual_income)

    def check(self,father_occupation,annual_income):
        if father_occupation == "not government":
            print("Eligible for Fee Reimbursement")
            if annual_income < 100000:
                print("Eligible for Fee Reimbursement")
            else:
                print("Not Eligible for Fee Reimbursement because annual income more than 1 lack")
        else:
            print("Not eligible for Fee Reimbursement bacause father is govt.employee")


f1 = FeeReimbursement("swapna,","not government,",70000)
f1.display()
c1 = f1.father_occupation,f1.annual_income
f1.check(c1, c1)

print("----------------------------")
f2 = FeeReimbursement("Akash,","not government,",150000)
f2.display()
c2 = f2.father_occupation,f2.annual_income
f2.check(c2, c2)

print("----------------------------")
f3 = FeeReimbursement("Manu,","government,",70000)
f3.display()
c3 = f3.father_occupation,f3.annual_income
f3.check(c3, c3)