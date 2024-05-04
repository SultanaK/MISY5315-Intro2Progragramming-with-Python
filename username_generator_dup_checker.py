#Import Section

from datetime import date   #import this for Date
import getpass
from unittest.util import sorted_list_difference              #import this for User

#Flower Box Section

#########################################################
#                                                       
#  Name:  Khandaker Razia Sultana                         
#   Date:  08/29/2023
#   Program Description: Create a unique username with duplicate checker
#
#  This program will take your username
#  generator project and improve on it. This program will ask the end user 3
#  questions, what is your first name, what is your last name, what year were
#  you born. This input will need to be validated and while loops used to force
#  the end user to enter the correct data
#                                                       
#########################################################

#Variables section

    #All variables needed for will be declared here
#declared varibale for for storing first name    
first_name=""
#declared varibale for for storing last name
last_name=""
#declared varibale for for storing borth year
birth_year=""
#declared list for for storing employee all data in tuple
employee_data_tuples_list =[]
#declared set for for storing employee data
#employee_data={}
#declared a string for for storing validation of employee information
is_correct=""
#declared list for for storing all possible yes values user could enter
yes_Llist=["Yes", "YES","yes","Y","y"]
#declared a empty list for for storing user names
username_list =[]
#declared a empty list for for storing sorted user names
user_sorted_list =[]
##emp_no_duplicate_data =[]
employee_data_dictionary = {} # initializing dictionary varialble that will hold employee data

#Input section
    
    #All input logic will be in this section
    #Make sure to use line comments to fully explain the inputs
# start a while loop ask the user 3 questions and start to ask the end user for at least 5 employees.
while len(employee_data_tuples_list) < 5:
    #You will ask for user input for "What is your first name?" and validate the data length least a length of 2.
    first_name=input("Enter your first name: ")
    if len(first_name) < 2:
       first_name = input("Enter your first name: ")
    #You will ask for user input for "Enter your last name?" and validate the data length least a length of 2.    
    last_name=input("Enter your last name: ")
    if len(last_name) < 2:
       last_name = input("Enter your last name: ") 
    #You will ask for user input for "Enter your birth year?" and validate the data length least a length of 4.    
    birth_year=input("Enter your birth year: ")
    if len(birth_year) < 4:
       birth_year = input("Enter your birth year: ")
    #Print to check information back out to the employee    
    print("Did you enter " + first_name + "  " + last_name +" birth year "+ " "+birth_year)
#Ask to confirm the information.   
    is_correct = input('Please enter your choise Yes or no \n   anything else to exit\n  : ')

    #if the employee answers Yes then update the employee data list with the information
    if is_correct in yes_Llist:
       employee_data =(first_name, last_name, birth_year)
       employee_data_tuples_list.append(employee_data)
    #after update the employee data list with the information it will clear the value for next user to store the data
       first_name=""
       last_name=""
       birth_year=""
    #if the employee answers No it will clear the value for next user to store the data
    else:
        first_name=""
        last_name=""
        birth_year=""  

#Process section

    #All processing of user input and calculations will be in this section
# this for loop is to create employee usernames in the format: first initial last name year of birth 
for employee in employee_data_tuples_list:
    #get employee first name from the employeee list 
   employee_first_name= employee[0]
    #get employee last name from the employeee list 
   employee_last_name=employee[1]
   #get employee birth year from the employeee list 
   emp_birth_year = employee[2]
   #get employee first name initial from the employeee list and convert it to lower case
   first_int = employee_first_name[0].lower()
   last_name_username = employee_last_name.lower()
   #get employee last name from the employeee list and convert it to lower case
   #get employee last 2 digit of birth year from the employeee list 
   birth_year_int = emp_birth_year[-2:]
    # building the new username, 
   username = first_int + last_name_username + birth_year_int
  
 #remove duplicate username
   if username in username_list:
       username = employee_first_name.lower() + last_name_username[0:1].lower() + birth_year_int
       #username = first_int.lower()+ employee_last_name.lower() + birth_year_int
       username_list.append(username)
      #employee__data__dictionary[username]= employee_data
      
   else:
       username_list.append(username)

   employee_data_dictionary[username]= employee #this line will create a dictionary where username is key

#sort the user list
user_sorted_list = list(username_list) # copying info to new variable sorted__username__list
user_sorted_list.sort() #sort usernames

#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted

print(getpass.getuser())
print(date.today())
print("-----------------------------------------------------------")
print("Employee Data list that you used to gather user input" + str(employee_data_tuples_list))
print("Username list with all usernames" + str(username_list))
print("Employee data dictionary"+ str(employee_data_dictionary))
print("Username list that has been sorted"+str(user_sorted_list))


