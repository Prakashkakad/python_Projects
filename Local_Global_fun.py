x = 7 #Global  variable
def my_fun():
    global x
    x = 9

my_fun()
print(x)
