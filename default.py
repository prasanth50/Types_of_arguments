"""if if want a parameter to be a defalut we assign that initially
   But, if we pass they in input section they get it from there as shown below"""
def person(name,age=18):
    print(name)
    print(age)
person('Prasanth',22)