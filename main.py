my_name = input("what is your name ?")
my_age = input("how old are you ?")
print(f'your name is {my_name} and I am {my_age} years old' )

first_number = int (input('enter the first number:'))
secound_number = int (input('enter the secound number:'))
operation = input(" enter the operation")
if operation == '+' :
    print(first_number + secound_number)
elif operation == "-" :
    print (first_number - secound_number)
elif operation == "*" :
         print(first_number * secound_number)
elif operation == "/" :
          print(first_number / secound_number)

else : 
       print (" the operation is not valid")

bus_capacity = 25
people = int (input( 'how many people are in the bus '))
people_1 = int (input(" enter the pepole how want to enter the bus "))

empty_seats = bus_capacity - people

if empty_seats > people_1:
       print ('ther are empty seats' )
elif empty_seats < people_1:
       print ('ther are no empty seats' )
elif empty_seats == people_1:
       print ('the seats full')



