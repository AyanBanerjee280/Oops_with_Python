#Class atrributes

class employee:
    company = "google"

Ayan = employee()
Samuel = employee()
print(Ayan.company)
print(Samuel.company)
employee.company = "Youtube"
print(Samuel.company)



#Instance attributes
# An attribute that belongs to the instant
Ayan.salary = 400  
Samuel.salary = 500
Ayan.salary = 400
print(Ayan.salary)
print(Samuel.salary)
#If two attributes are same then first preference will be given to object and second to class
