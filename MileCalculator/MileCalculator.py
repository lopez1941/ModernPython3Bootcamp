# convert miles to kilometers

question = float(input("How many miles did you travel today? "))
print(f"Thanks.  You entered {question}.")

print(type(question))
# miles = float(question) - casting the variable as a float at the start of it
kilometers = question * 1.60934

print(f"You traveled {question} miles, and that equals {kilometers} kilometers.")
#  It's kind of annoying that it gives you 7 decimal points of precision
#  You can use the round function to specify how precise you want to be
#  round(thing_being_rounded, number_of_decimal_points)

rounded_answer = round(kilometers, 2)
print(f"The rounded conversion is {rounded_answer} kilometers.")