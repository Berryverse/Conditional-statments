# if, else, elif
#"on" and "and"
a = input("Your first number goes here: ")
b = input("Your second number goes here: ")
#----------------------------conditional part----------------------------------
if a==b:
    print("a is equal to b")
elif a>b and b<a:
    print("A is greater")
elif b>a and b<a:
    print("B is greater")
elif a!=b:
    print("The numbers are not equal")