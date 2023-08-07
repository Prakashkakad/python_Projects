# --------------------Class
# class Details:
#     Name_car = "Tata Harrier"
#     Number_Plate = "MH15GJ2003"
#     Model = "4X"
#     Type = "4X4"
#
#     def car_info(self):
#         print(f"{self.Name_car} is an Very Nice SUV with {self.Type} and Its number is {self.Number_Plate}"
#               f"{self.Name_car} is an Very Nice SUV with {self.Type} and Its number is {self.Number_Plate}")
#
#
# a = Details()
#
# b = Details()
# b.Name_car = "Honda City"
#
# print(a.car_info())
# --------------------------------Constructors


# class Intro:

# class Intro:
#     def __init__(self, name, Occupation):
#         self.name = name
#         self.Occupation = Occupation
#
# obj1 = Intro("Prakash", "CloudsDevops")
# print(obj1.name, "is a", obj1.Occupation, "as Occupation.")
#
#
#
# obj2 = Intro("Sahil","Bussinessman")


# ================================Decorators
'''class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return self._value


obj = Myclass(10)
obj.show()
'''

# ================================Decorators
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

    return wrapper


@measure_time
def slow_function():
    time.sleep(4)
    print("Function executed")


slow_function()
