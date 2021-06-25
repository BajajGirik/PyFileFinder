import os

# function to find file paths 
def find_files(filename, startPath):
   res = []

   # walking top-down from the startPath  
   for root, dirs, files in os.walk(startPath):

      # this is for not entering mac's read-only folder 
      dirs[:] = [d for d in dirs if d not in "System"]
      if filename in files:
         res.append(os.path.join(root, filename))

   return res


filename = input("Filename whose path you want to take out: ")
print("Path of the directory from which the search should begin")

# if user doesn't enter anything then root directory will be used
path = input("(Press Enter to start from root directory): ") or os.path.abspath(os.sep)

filePaths = find_files(filename, path)
length = len(filePaths)

if length == 0:
    print("No files found")

elif length > 1:
    print("Found multiple files.")

else:
    print("Found your file.")

for i in range(1,length+1):
    print(f"{i})  {filePaths[i-1]}")
        


