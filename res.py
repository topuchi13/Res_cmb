try:
	file = open ("./list.csv", "r")

except FileNotFoundError:
	print ("*** The file containing available resistor list doesn't exist ***")
	
	
list = file.read().split('\n')

try:
	target = int(input("\nPlease input the target resistance: "))

except ValueError:
	print("*** Wrong Value Entered!!! Please enter only one integer, describing the resistor value ***")
	
	
	
# def combiner():
    # if target in list:
        # return "You already have that kind of resistor dummy"
    # for a in range(len(list)):
        # for b in range(len(list)):
            # for c in range(len(list)):
                # if list[a]+list[b]+list[c] == target:
                    # print( "resistor 1: " + list[a] + "resistor 2: " + list[b] + "resistor 3: " + list[c])
            # if list[a]+list[b] == target:
                # return "resistor 1: " + list[a] + "resistor 2: " + list[b]

    # return "no possible combinations were found"

# print (combiner())
