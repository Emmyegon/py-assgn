# # Create a program that reads a file and writes a modified version to a new file.

# from inspect import getfile


# open('input.txt' , 'w').close()  # Create an empty file
# file=open('input.txt', 'w')
# file.write('mode in creating files include write, read, append and binary modes\n')

# # read
# file=open('input.txt', 'r')
# data=file.read() 
# print(data)

# file=open('second.txt', 'w')
# file.write('you can also use try except for error handling\n')
# file.write('you can also use with statement to open and close files automatically\n')
# file.close()
# file=open('second.txt', 'r')
# data=file.read()    
# print(data)
# file.close()

# try:
#     file=open('input.txt', 'r') # Open the input file in read mode
#     content=file.read() # Read the content of the file  
#     modified_content=content.replace('a', '@') # Replace all occurrences of 'a' with '@'
#     file.close() # Close the input file
#     print("File processed successfully. Check 'output.txt' for the modified content.")
# except FileNotFoundError:
#     print("Error: The input file was not found.")
    
    # Create input file
input_file = open('input.txt', 'w')
input_file.write('mode in creating files include write, read, append and binary modes\n')
input_file.close()


try:
    # Read from input file
    infile = open('input.txt', 'r')
    data = infile.read()
    infile.close()
    
    # Modify the content (convert to uppercase and add header)
    modified_data = "MODIFIED VERSION:\n" + data.upper()
    
    # Write modified content to new output file
    outfile = open('output.txt', 'w')
    outfile.write(modified_data)
    outfile.close()
    
    print("Successfully created modified version in output.txt")
    
    # Read and display the new file content
    result_file = open('output.txt', 'r')
    print("Modified content:")
    print(result_file.read())
    result_file.close()
        
except FileNotFoundError:
    print("Error: Input file not found")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
    # error handling for file operations

try:
    # Ask user for filename
    filename = input("Enter filename to read: ")
    
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # If successful, display content
    print(f"\nFile content:")
    print(content)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")

except PermissionError:
    print(f"Error: No permission to read '{filename}'!")

except Exception as e:
    print(f"An error occurred: {e}")