with open("text.txt","r")as fileHandler:
    content = fileHandler.read()

new_content = content.replace("Bo","Ta bo")
with open("text.txt",'w') as fileHandler:
    print(new_content, file = fileHandler)

with open("text.txt","r") as fileHandler:
    print(fileHandler.readlines(27))


