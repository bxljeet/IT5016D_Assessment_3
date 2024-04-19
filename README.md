#BALJEET CODING
* This File is to understand how the code in hello.py file works.
* First I selected a topic of "Python program to check if year is leap year or not".
Coding start
#Coding start
* So i first created an variable named "year" and to input the year in "year" variable i used input function. Since years are numeric, i used into function so the code can run properly.
* I put "enter a year/n* in input function so people can understand that you have to enter year in terminal:
year = int(input("enter a Year\n*))
厶
* To check if year is leap year or not i used "if", "elif" and "else" statements in the code.
* To check if year is a leap year in Python is found by checking the divisibility of the year with 4 and 400. If a year is perfectly divisible by 4, then it is a leap year. However, if it is a century year (ending with 00), then it will be checked with 400.
* So i used "if" statement for the divisibilty of the year with 400 and 100, Also, i used "elif" statement fot the divisibilty of the year with 4 and non-divisibility with 100. And at last, i used "else" statement so if year does not complete the if and elif statment the year won't be Leap
* if year meets the "if" condition i used printO function to print year, "is a leap year and the first year is variable of this code.
if (year % 400 = = 0) and (year % 100 = = 0):
print (year, "Is a leap year")
* The output will look like:
x year is a leap year (here x is taken as an example for the year)
year = int(input(enter a Year\ni))
* To check if year is leap year or not i used "if", "elif" and "else" statements in the code.
* To check if year is a leap year in Python is found by checking the divisibility of the year with 4 and 400. If a year is perfectly divisible by 4, then it is a leap year. However, if it is a century year (ending with 00), then it will be checked with 400.
* So i used "if" statement for the divisibilty of the year with 400 and 100. Also, i used "elif" statement fot the divisibilty of the year with 4 and non-divisibility with 100. And at last, i used "else" statetment so if year does not complete the if and elif statment the year won't be Leap year.
* if year meets the "if" condition i used printo function to print "year, "is a leap year" and the first year is variable of this code.
if (year % 400 == 0) and (year % 100 = = 0):
print(year, "is a leap year")
* The output will look like:
x year is a leap year (here x' is taken as an examplifor the year)
* if year meets the "elif" condition i used printO function to print year, "is a leap year" and the first year is variable of this code.
elif (year % 4 = =0) and (year % 100!= 0):
print(year, "is a leap year")
* The output will look like:
x year is a leap year (here x' is taken as an example for the year)
* if year doesn't meet neither "if nor "else" condition, it will go to "else" statement and i used printO function to print "year. "is not a leap year" and the first year is variable of this code.
else:
print (year, "is not a leap year")
