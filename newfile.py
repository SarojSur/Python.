#file name newtext.txt
with open("newtext.txt","w") as file :
    file.write("Once a man can became Lion...")

with open("newtext.txt","a") as file :
    file.write("This is Hasan Jamil...")

with open("newtext.txt","a") as file :
    file.write("Next line story is very dengerious for human beings...")

with open("newtext.txt","a") as file:
    file.write("Is there any lines l")


file = open("newtext.txt","r")
print(file.readlines())
