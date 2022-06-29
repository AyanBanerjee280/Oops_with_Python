#Create a class with a class attribute a; create an object from it and set a directly using object.a = 0
#Does this change the class attribute?


class sample:
    a = 'Ayan'

obj = sample()
obj.a = "Vicky"
print(sample.a)
print(obj.a)


#Answer: Yes itdoes not change the class attribute


class sample:
    a = 'Ayan'

obj = sample()
obj.a = "Vicky"
sample.a = "Vickky" #This changes the class atrribute as it changes the instance attribute
print(sample.a)
print(obj.a)
