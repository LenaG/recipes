'''
R2D- takes recipes and comments out the directions and serving size and makes ingredients into dict() which are scalable by convert.py

'''

r_name = "Vegetarian_Meatballs.txt"
# assigned result of calling open to the variable f (file object)
f = open(r_name)
all_lines = f.readlines()
f.close()

recipe = dict()
# all_lines is a list of strings
for l in all_lines[:1]:
    print l
    # making a list of items contained in l, split when space occurs
    x = l.split()
    # index into first value of x and make it into integer
    amt = int(x[0])
    ingredient = x[1]
    measurement = "count"
    recipe[ingredient] = [amt, measurement]
    
    print recipe


