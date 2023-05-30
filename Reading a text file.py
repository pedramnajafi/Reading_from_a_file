text_file = open('inputFile.txt', 'r')
for line in text_file:
    line_split = line.split() # divide all the columns
    if line_split[2] == 'P': # if the 3rd column is P, print the whole line
        print(line)
text_file.close()


