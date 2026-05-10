# Build a script that:
# 1. Asks user for filename
# 2. Tries to open and read it
# 3. File not found → print error + log to errors.log with timestamp
# 4. File empty → print "File is empty"
# 5. Success → show word count and line count
# 6. Always prints "Operation complete" (use finally)

# File: safe_file_reader.py
# Commit: "feat: safe file reader with error logging"
import datetime as datetime
user_filename=input("Enter File Name: ")
try:
    with open(user_filename,"r") as file:
        content=file.read()
        print(content)
    if content=="":
        print("File is empty")
    else:
        print("success")
        with open(user_filename,"r") as file:
            # count=1
            # for line in file:
            #     print(count,line)
            #     count+=1
            print(len(content.splitlines()))
            print(len(content.split()))
            
except FileNotFoundError:
    print("File Not Found")
    with open("errors.log","a") as file:
        now = datetime.datetime.now()
        file.write(str(now), "\n")

finally:
     print("Operation complete")

