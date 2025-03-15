def create_and_write_file():

    file_name = ("Speech.txt")
    content = input("Enter the content you want to write to the file: ")

    with open(file_name, "w") as file:
        file.write(content)
    
    print(f"File '{file_name}' has been created and content written successfully.")
    return file_name

if __name__ == "__main__":
    create_and_write_file()
