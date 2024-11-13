# # Approach - 1

# txt = input("Enter the name of your file: ")
# x = txt.split(".")

# y = x[1]


# if y == "gif":
#     print("image/gif")
    
# elif y == "jpg":
#     print("image/jpg")
    
# elif y == "jpeg":
#     print("image/jpeg")
    
# elif y == "png":
#     print("image/png")
    
# elif y == "pdf":
#     print("application/pdf")
    
# elif y == "txt":
#     print("text/txt")
    
# elif y == "zip":
#     print("zipfile/zip")
    
# else:
#     print("application/octet-stream")
    
    
# Approach - 2

# Define a dictionary to map file extensions to MIME types
extension_to_mime = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

# Get the file name from user input
txt = input("Enter the name of your file: ")

# Check if the input contains a dot (.)
if "." in txt:
    # Split the input into name and extension
    name, ext = txt.rsplit(".", 1)
    ext = ext.strip().lower()  # Convert to lowercase and remove spaces

    # Check if the file extension exists in the dictionary
    if ext in extension_to_mime:
        print(extension_to_mime[ext])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
