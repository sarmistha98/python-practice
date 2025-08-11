#Type casting
#Implicit

integer_number=123
float_number=1.23
new_number=integer_number+float_number
print("value:",new_number)
print("Data Type:",type(new_number))
print(int(new_number))

#Explicit

num_string="12"
num_integer=23
print("Data type of num_string before type casting:",type(num_string))
num_string=int(num_integer) # use explaicit type casting
print("Data type of num_string after type casting:",type(num_string))
num_sum=num_integer+num_string
print("sum:",num_sum)
print("Data type of num_sum:",type(num_sum))