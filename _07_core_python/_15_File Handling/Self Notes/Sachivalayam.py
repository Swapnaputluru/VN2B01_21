class Sachivalayam:

    job_type = "Temporary"
    salary = 15000

    def __init__(self, job_role, area):
        self.job_role = job_role
        self.area = area

    def display(self):
        print("instance and class variables are printed:", self.job_role,self.area,Sachivalayam.salary,Sachivalayam.job_type)


s1= Sachivalayam("Assistant Engineer,", "Tadpatri,")
s1.display()  # we will get both class variables and instance variables in instance method

print("--------------")
s2= Sachivalayam("Survivor,", "Chitoor,")
s2.display()

print("--------------")
s3= Sachivalayam("Digital Assistant,", "Karnool,")
s3.display()
