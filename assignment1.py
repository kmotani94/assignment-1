print("Answer 1")
print()

print("Hello, my name is \"Rishabh\". I love coding")
print("This is 'my first program'.")

x = input("Enter X: ")
y = input("Enter Y: ")
z = input("Enter Z: ")

print("Value 1 = " + x + ", Value 2 = " + y + ", Value 3 = " + z)
print("Datatype of X : " ,type(x))
print("Datatype of Y : " ,type(y))
print("Datatype of Z : " ,type(z))

# --------------------------------------------------------------------------

print()
print("Answer 2")
print()

print("Hello! My name is XYX")
print("\"Hello I am a candidate\"")
print("\"234.56\"")
print("\"34\"")
print("a+3j")

# --------------------------------------------------------------------------

print()
print("Answer 3")
print()

x=10+20*(45+67.0)
print(type(x))

x=(True and False) or False
print(type(x))

x=(True or True) and (not False and True)
print(type(x))

x=(3>89) or (34>32)
print(type(x))

x=not True and False
print(type(x))

# --------------------------------------------------------------------------

print()
print("Answer 4")
print()

num = int(input("Enter a number: "))

if (num%2==0 and num%5==0):
	print("Hurray it is what I am looking for")
else:
	print("wrong input")

# --------------------------------------------------------------------------

print()
print("Answer 5")
print()

num = int(input("Enter a number: "))

if (num>9 and num<51):
	print("Yes I am in the range")
else:
	print("Oops")
