import os 
# Create variables to store the following AI model configuration:
modal_name="gemini-2.5-pro "
temperature="10 "
maximum_tokens="1000 "
API_version="v1"

# Create a dictionary to store student information:
Student={
    "name":"sagil",
    "cource":"PGDCA",
    "semester":"1",
    "marks":"70"
}

# Display all AI model configuration values using formatted output (f-strings).
print(f"Modal Name {modal_name}")
print(f"temperature {temperature}")
print(f"maximum_tokens {maximum_tokens}")
print(f"Modal Name {API_version}")

#Display all keys and values of the student dictionary.
for value in Student.items():
    print (value[0],value[1])

#Update the student's marks based on user input and display the updated dictionary.
updated=int(input("Updeting marks :"))
Student["marks"]=updated
print(Student)

# Accept the name of a text file from the user and:
file_name=input("Enter your file name:")
# Check whether the file exists.
if os.path.exists(file_name):
    print("file Exists")

    #Display its size in bytes.
    size= os.path.getsize(file_name)
    print(f"File Size:{size} bytes")
    
    # Display whether the file is Empty (0 bytes) or Non-Empty.
    if size == 0:
            print("File Status:Empty")
    else:
            print("File Status:Non-Empty")
else:
    print("Error: File does not exist.")

