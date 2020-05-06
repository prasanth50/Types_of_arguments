"""This method if used when we don't know the number of arguments given by user."""
def add(*a):
    b=0
    for i in a:
        b+=i
    print(b)
add(10,21,35,67,43)