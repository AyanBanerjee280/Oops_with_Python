# #STATIC METHOD
# class employee:
#     company = "Google"   #self is automatically passed ś
#     def getsalary(self):
#         print(f"Salary for this Employee working in {self.company} is {self.salary}.")

#     def greet(self):
#         print("Good Morning, Sir")

# Harry = employee()
# Harry.salary = 1000000
# Harry.greet()

#STATIC METHOD
class employee:
    company = "Google"   #self is automatically passed ś
    def getsalary(self, signature):
        print(f"Salary for this Employee working in {self.company} is {self.salary}.\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Harry = employee()
Harry.salary = 1000000
Harry.getsalary("Thanks!")
Harry.greet()
Harry.time()