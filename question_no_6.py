#Can you change the harry paremeter inside a class to something else (say "Ayan")
#Try changingself to "slf" or "Ayan" and observe the effects

# class sample:
#     def __init__(self, name):
#         self.name = name

# obj = sample("Ayan")

# print(obj.name)


class sample:
    def __init__(Ayan, name):
        Ayan.name = name

obj = sample("Ayan")

print(obj.name)


class sample:
    def __init__(slf, name):
        slf.name = name

obj = sample("Ayan")

print(obj.name)

'''So the answer is that "self" can be changed into 
anything and it will work, but 
one shouuld not change self to 
anything because it will create confusion
among other coders '''