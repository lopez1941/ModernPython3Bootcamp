# using 'with open' the file is automatically closed when the code completes


# with open("C:\\temp\snapshotlist.txt", 'r') as file:
#
#     for n in range(0,3):
#         my_line = file.readline()
#         print(my_line)


# writing to files
with open("C:\\temp\\my_write_file.txt", "w") as file:
    file.write("Here is a line of text\n")
    file.write("Here is another line of text.\n")
    file.write("Let's see if this works.")
# using .write with the 'w' flag- the original contents of the file are overwritten

with open("C:\\temp\\lol.txt", "w") as file:
    file.write("Haha" * 1000)