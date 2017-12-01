x = input("Enter the thickness of a paper in millimeters: ")
x = float(x)
x = x/1000000


number_of_times_multiplied = 0 
while x < 384472:
    x = x*2
    number_of_times_multiplied = number_of_times_multiplied+1

print("You would fold the paper " + str(number_of_times_multiplied) + " times to get from the earth to the moon.")
    
    
