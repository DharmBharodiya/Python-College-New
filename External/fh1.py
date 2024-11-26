import os.sys


# to write to the file
# file = open("test1.txt", 'w')
# str = input("Enter string")
# file.write(str)
# file.close()

# to read from the file
# file = open("test1.txt", 'r')
# str = file.read()
# print(str)
# file.close()

# f = open("test2.txt", 'w')
# print("Enter the string and use @ at the end")
# while str != '@':
#     str = input()
#     if(str!='@'):
#         f.write(str + "\n")
# f.close()

# f=open("Myfile.txt","a+")
# #enter strings from keyboard
# print("Enter text to append(@ at end): ")
# while str != '@':
#     str=input()
#     if(str!='@'):
#         f.write(str + "\n")
# f.seek(0,0)
# print("The file contents are: ")
# str=f.read()
# print(str)
# f.close()


# f = input("Enter the file name")
# if os.path.isfile(f):
#     file = open(f, 'r')
# else:
#     print("No such file exists that can be opened")

# word = file.read()
# print(word)
# file.close()

fname=input("Enter the filename: ")
if os.path.isfile(fname):
    f=open(fname,"r")
else:
    print(fname+ " does not exist")
sys.exit()
cl=cw=cc=0
for line in f:
    words = line.split()
    cl += 1
    cw = len(words)
    cc = len(len)

print(f"lines: {cl} Words: {cw} Characters: {cc}")

