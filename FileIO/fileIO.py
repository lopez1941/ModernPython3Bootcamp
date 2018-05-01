#import os

opened_file = "C:\\temp\\snapshotlist.txt"
#os.path.basename(path)



# with open(opened_file, 'r') as file:
#     my_file = file.read()
#     print(my_file)
#     print("let's do it again")
#     my_file = file.read()
#     print(my_file)
#     my_file.seek(0)
#     my_file = file.read()
#     print(my_file)
# print("Opening the file. ")
# my_file = open(opened_file)
# print("file has been opened")
# # type(my_file)  this doesn't work for some reason?  weird
# print("reading the file and setting it to the variable lets_read")
# lets_read = my_file.read()
# print(f"Printing lets_read \n{lets_read}")
my_file = open(opened_file)
my_file.read()  #  for some reason, this really only works in the shell
my_file.close()

