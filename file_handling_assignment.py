#writting file to include both strings and numbers

with open('my_file.txt', 'w') as file:
    file.write('Power Learn Project Module Specialization\n')
    file.write('Number of modules available: ' + str(6) + '\n')
    file.write('I am specializing in Python and Web technologies modules\n')
    file.write('And am currently in week: ' + str(7) + '\n')


#file appending

with open('my_file.txt','a') as file:
    file.write('Three of the six modules are compulsory\n ')
    file.write('The compulsory modules are:\n')
    file.write(str(1) + ' ' + 'Software Engineering\n')
    file.write(str(2) + ' ' + 'Database with mySQL\n')
    file.write(str(3) + ' ' + 'Entrepreneurship\n')

#Error Handling + file display

try:
    file = open("my_file.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    if 'file' in locals():
        file.close()
    print("File handling complete.")


