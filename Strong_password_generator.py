import random
def gen_pass():
    name=input("Enter your name----> ")
    birth_year=input("Enter you Birth year---> ")
    special_character=input("Enter your special character to make password with-----> ")
    num=input("Enter any of your favrouite object name----> ")
    l=[name, birth_year, special_character,num]
    random.shuffle(l)
    d=''.join(l)
    print(d)
gen_pass()