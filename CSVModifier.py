import csv

new_columns = []
file_to_open = raw_input("What file would you like to open? ") # Save filename in file_to_open
userinput = raw_input("What string would you like to modify? ") #Save string to be removed in userinput

changes = { #Set key and value in dictionary
    userinput : '',
    }

   

with open(file_to_open, 'rb') as f:
    reader = csv.reader(f)
    for column in reader:
        new_column = column
        for key, value in changes.items():
            new_column = [x.replace(key, value) for x in new_column]
        new_columns.append(new_column)

with open(("modified" + file_to_open), 'wb') as f: #Save modified file as new CSV
    writer = csv.writer(f)
    writer.writerows(new_columns)

print("Done!")
    
