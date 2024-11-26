import zipfile

# with zipfile.ZipFile("toys.zip","w") as zipf:
#     zipf.write("fh1.py")
#     zipf.write("test1.txt")
#     zipf.write("test2.txt")
#     print("Files successfully compressed into a zipfile.")

with zipfile.ZipFile("toys.zip","r") as zipf:
    zipf.extractall("toys_folder")
    print("All the files successfully extracted from the folder.")