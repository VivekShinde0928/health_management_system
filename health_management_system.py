print('***Health Management System***\n') ##this progrm is valid for 2 people data

import time
t=time.asctime()

# def getdate():
#     import datetime
#     return datetime.datetime.today()

def log(k):
    if k==1:
        c=int(input('enter 1 for exer and 2 for food :'))
        if c==1:
            value=input('type here :')
            with open('vicky-exer.txt','a') as op:
                op.write(t + ' : '+ value+'\n' )
        if c==2:
            value=input('type here :')
            with open('vicky-food.txt','a') as op:
                op.write(t+' : '+value+'\n')
    if k==2:
        c=int(input('enter 1 for exer and 2 for food :'))
        if c==1:
            value=input('type here :')
            with open('ankit-exer.txt','a') as op:
                op.write(t+' : '+value+'\n' )
        if c==2:
            value=input('type here :')
            with open('ankit-food.txt','a') as op:
                op.write(value+'\n')

def retrieve(k):
    if k==1:
        c = int(input('enter 1 for exer and 2 for food :'))
        if c==1:
            with open('vicky-exer.txt') as op:
                print(op.read())
        if c==2:
            with open('vicky-food.txt') as op:
                print(op.read())
    elif k==2:
        c = int(input('enter 1 for exer and 2 for food :'))
        if c==1:
            with open('ankit-exer.txt') as op:
                print(op.read())
        if c==2:
            with open('ankit-food.txt') as op:
                print(op.read())

a=int(input('enter 1 for log or 2 for retrieve :'))

if a==1:
    b=int(input('enter 1 for vicky or 2 for ankit :'))
    log(b)
else:
    b=int(input('enter 1 for vicky or 2 for ankit :'))
    retrieve(b)


# #**this pgm pending coz i need to add new member and show new member added in list
#
# print('***Health Management System***\n')
#
# def log():
#     d = input('Enter name :')
#     e=int(input('Enter 1 for food or 2 for exer :'))
#     if e==1:
#         value = input('type here :')
#         with open(d+'_food.txt','a') as f:
#             f.write(value+'\n')
#     elif e==2:
#         value = input('type here :')
#         with open(d + '_exer.txt', 'a') as f:
#             f.write(value + '\n')
#     else:
#         print('something wrong in log')
#
# def retrieve():
#     d = input('Enter name :')
#     e=int(input('Enter 1 for food or 2 for exer :'))
#     if e==1:
#         #value = input('type here :')
#         with open(d+'_food.txt') as f:
#             print(f.read())
#     elif e==2:
#         #value = input('type here :')
#         with open(d + '_exer.txt') as f:
#             print(f.read())
#     else:
#         print('something wron in retrieve')
#
# if __name__ == '__main__':
#     name_list = ['arun', 'vicky', 'ankit']
#     while True:
#         a = int(input('\nenter 1 for new_name or 2 for update :')) ##dont enter 1 coz pgm pending due to i cant show list
#         if a==1:
#             while True:
#                 new_name=input('Enter new name :')
#                 name_list.append(new_name)
#                 print(name_list)
#                 user_input = ''
#                 while user_input!='q' and user_input!= 'c':
#                     user_input=input("enter q for quit or c to add more name : ")
#
#                 if user_input=='q':
#                  break
#                 elif user_input=='c':
#                  continue
#
