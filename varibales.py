def var(name):
    print("Hello", name)
var("Mandeep")


def default_Greet(name="Utsab"):
    print("Hey" ,name)
default_Greet("Mandip")
default_Greet()


def namenage(age, name="Biswas"):
    print("Hey, your name is" ,name ,"and your age is" ,age)
namenage(12, 'Agniz')
namenage(12)


x = 10
y = "string"
z = int(9.3)
a = {"apple", "banana", "cherry"}
b = {
  "brand": "Cheap",
  "model": "Mbappe",
  "year": 2024
}
c = ("apple", "banana", "cherry")
e = float(7)
nonetype = None

print(type(x),x)
print(type(y),y)
print(type(z),z)
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(e),e)
print(type(nonetype))


'''
A function that takes year of birth as input and calculates the age of a person right now parameters default parameter name is equals to Raji Samal non default parameter year of birth

'''



def assi(DOB, name = "Rajesh Hamal"):
    year = 2024 - DOB
    print("Hey",name, "Your age is" ,year, "years")
assi(2023)