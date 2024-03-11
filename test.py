


import time
e = "Enter Any Data"
print(e)
for i in range(10):
    print(i)
time.sleep(10)
class MyClass:
    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):
        print("Class method")

    @property
    def my_property(self):
        return "Property value"

obj = MyClass()
obj.static_method()
obj.class_method()
print(obj.my_property)
#input("Press Enter to close the application...")
