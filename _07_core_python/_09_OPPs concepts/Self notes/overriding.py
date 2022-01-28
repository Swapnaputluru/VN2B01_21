class College:
    def ksrm(self):
       pass

class College1(College):
    def ksrm(self):
        print("location is kurnool")


c1 = College1()
c1.ksrm()

# override variables

class Names:
    name = "swapna"

class Name(Names):
    name = "sunny"

print(Names.name)
print(Name.name)
