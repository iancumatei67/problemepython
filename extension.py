#Exercitiul 1
#Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.

def get_file_extension(file_name):
    base_name, extension = file_name.split(".")
    print(f"The file extension is {extension}")


while True:
    try:
        file_name = input("Enter a filename: ")
        get_file_extension(file_name)
        break
    except:
        ValueError
        print("This is not a valid file")
