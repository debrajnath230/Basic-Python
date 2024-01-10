file1 = open('C://Users//nath.debraj//Desktop//Python Codes//Python_training_tutordude//FILES, EXCEPTIONS AND ERRORS//my_file.txt','w') 
writing_file=file1.write('Hello')
print(writing_file)
file1.close()

file1=open('C://Users//nath.debraj//Desktop//Python Codes//Python_training_tutordude//FILES, EXCEPTIONS AND ERRORS//my_file.txt','r')
reading_file=file1.read()
print(reading_file)
file1.close()