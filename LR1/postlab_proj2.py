enterfile = input("Enter the file name: ")
file = open(enterfile, 'r')
linecount = 0

for line in file:
    linecount = linecount + 1

print("The number of lines in this txt. file is", linecount)

while True:
    linenum = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thank You for Using this Program!")
            break