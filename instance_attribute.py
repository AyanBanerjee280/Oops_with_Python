#Below two are classes

class employee:
    company = "google"
    salary = 100

Ayan = employee()
Samuel = employee()
print(Ayan.salary)
#Below two are objects, aka instance attributes
# Ayan.salary = 400  
# Samuel.salary = 500
Ayan.salary = 45 #if this is commented out class salary 100 will be printed
print(Ayan.salary) #Preference is given to object, if there is no object the preference will be given to class
print(Ayan.address) #this line throws an error because address is not an object or aS class

