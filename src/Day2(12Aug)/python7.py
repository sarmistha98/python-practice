#while loop with break statement
#WAP to terminate the loop when user eneter "end"

while True:
    user_input=input("Enter a name: ")
    if user_input=='end':
        print(f'The loop is ended.')
        break
    print(f'Hi {user_input}')

