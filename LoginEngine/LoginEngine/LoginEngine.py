#Cocoanix LoginEngine
#2020 Cocoanix

#Username Part (Username Doesn't Matter)
print("LoginEngine v1")
print("")
print("")
print("Username:")
input()

#Password Part
print("")
print("Password:")
pass_key = input()

#Password Check Part
if pass_key == "admin":
	print("")
	print("Login Success!")
	input("Press Any Key To Exit!")

#If Password Doesn't Match Then Quit App
else:
	print("")
	print("Login Failed!")
	input("Press Any Key To Exit!")




