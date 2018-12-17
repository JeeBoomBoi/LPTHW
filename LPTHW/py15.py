from sys import argv                       #imports artgv

script,filename = argv              #declare variable

txt = open(filename)                 #opens file

print(f"Here's your file {filename}:")  #prints
print(txt.read())   #reads the file
txt.close()
print("Type the filename again:")   #prints string
file_again = input('> ')    #prompting

txt_again = open(file_again)    #opens file again

print(txt_again.read())     #reads the file
