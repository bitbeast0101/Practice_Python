// THE YEAR YOU TURN 100
def hundredyears() :
	current_year = 2017
	name,age =  input("Enter your name : "),input("Enter your age : ")
	number = int(input("No of times message to be repeated: "))
	dob = current_year - int(age)
	i = 1
	while i <= number :
		print("The year you turn 100 : " + str(dob+100))
		i += 1
hundredyears()
