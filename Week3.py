
#LAB EXERCISE 1: GRADE CALCULATOR

numerical_score = int(input("Numerical Score (1-100): "))

if not (1 <= numerical_score <= 100):
    print("Out of range")
    exit()
    
if( 90 <= numerical_score <= 100):
    print("Grade: A")

elif( 80 <= numerical_score <= 89):
    print("Grade: B")

elif(70 <= numerical_score <= 79):
    print("Grade: C")

elif(60 <= numerical_score <= 69):
    print("Grade: D")

elif(numerical_score < 60):
    print("Grade: F")

else:
    print("Error")


#LAB EXERCISE 2: LIMITED LOGIN ATTEMPTS

password = "cool123"
maximum_attempts = 3
available_attempts = 0

while available_attempts < maximum_attempts:
    entered_password = input("Please enter your Password: ")
    
    if entered_password == password:
        print("Login Succesful.")
        break
    else:
        available_attempts += 1
        print(f"Incorrect password. {available_attempts} from {maximum_attempts}")

if available_attempts == maximum_attempts:
    print("No more attempts left. Try again later.")
    exit()


#LAB EXERCISE 3: FILTERING EVEN NUMBERS


numbers = (1, 2, 3, 4 , 5, 6, 7, 8, 9, 10)

for num in numbers:
    if num %2 !=0:
        continue
    print(num)