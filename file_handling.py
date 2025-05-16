# Writing data
with open("data.txt", "w") as f:
    f.write("Python is awesome!\n")
    f.write("File handling made easy.\n")

# Reading data
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
