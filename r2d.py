'''
R2D- takes recipes and comments out the directions and serving size and makes ingredients into dict() which are scalable by convert.py

'''

from fractions import Fraction

r_name = "Vegetarian_Meatballs.txt"
# assigned result of calling open to the variable f (file object)
f = open(r_name)
all_lines = f.readlines()
f.close()

recipe = dict()
# all_lines is a list of strings
for l in all_lines[:3]:
    print l
    # making a list of items contained in l, split when space occurs
    x = l.split()
    # if line is empty continue
    if len(x) == 0 : 
        continue 
    # index into first value of x and make it into integer
    print x, "is a listl"
    amt = Fraction(x[0])
    if len(x) == 2 :
        ingredient = x[1]
        measurement = "count"
    # if measurement is there take is instead of defining as 'count' from indexing into the 3rd part of the list
    else: 
        measurement = x[1]
        #pasha made me do this i have no idea what's going on, very lost
        ingredient = " ".join(x[2:])
    recipe[ingredient] = [amt, measurement]
    
    print recipe


