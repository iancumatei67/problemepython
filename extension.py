#Exercitiul 1
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
