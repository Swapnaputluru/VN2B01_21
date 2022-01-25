from asyncore import dispatcher


def adding(a, b):
    add = a + b
    print(add)

def adding(a, b, c):
    add = a + b + c
    print(add)


adding(1,2,3)

@dispatcher (int,int)
def adding(a, b):
    add = a + b
    print(add)
@dispatcher (int,int,int)
def adding(a, b, c):
    add = a + b + c
    print(add)

adding(2,3)
adding(1,2,3)