# Angel Chaple
# 10/03/2023
# Project_01

'''
CODE IS AFTER INSTRUCTION SET!! 

Step 1:
Ask the user to enter the length of their room (in feet).
Step 2:
Ask the user to enter the width of their room (in feet).
Step 3:
Calculate the area (in square feet) of the room by multiplying the length and the width of the room.
For example, if a room is 20 feet wide by 24 feet long, then its area is 20 * 24 = 480 square feet
Step 4:
Display a menu that asks the user how much shade the room gets.  The menu should have the following options:
Little Shade
Moderate Shade
Abundant Shade
Step 5:
Determine the capacity of the air conditioning unit that is needed for a moderately shaded room by using the information in the table below.
Room Size (sq. ft)
AC capacity (BTUs/hr)
Less than 250
5,500
250 to 500
10,000
501 to 1,000
17,500
Over 1,000
24,000
If the room has little shade, then the BTU capacity should be increased by 15% since the air conditioning unit must be able to produce extra cooling. 
If the room has abundant shade, then the BTU capacity should be decreased by 10% since the air conditioning unit does not need to work as hard to cool a shaded room.
Step 6:
Create a String object in memory to hold the text “Air Conditioning Window Unit Cooling Capacity”.  Display that text at the top of the output.
Step 7:
Display the following output:
The area of the room (in square feet)
The amount of shade that the room gets
The number of BTUs per Hour that are needed to cool that room (rounded to the nearest whole number)
Sample Input and Output (user input is in bold) - The output of your program should match the formatting and spacing exactly as shown
Please enter the length of the room (in feet): 15.5 
Please enter the width of the room (in feet): 10 
What is the amount of shade that this room receives? 
Little Shade
Moderate Shade
Abundant Shade
Please select from the options above: 3

Air Conditioning Window Unit Cooling Capacity

Room Area (in square feet): 155.0

Amount of Shade: Abundant

BTUs Per Hour needed: 4,950 
'''
# --------------------------------------------------------------------------------

# Step 1: Ask for room length
room_length = float(input("Enter the length of the room (in feet): "))

# Step 2: Ask for room width
room_width = float(input("Enter the width of the room (in feet): "))

# Step 3: Calculate room area
room_area = room_length * room_width

# Step 4: Ask for shade level
print("Select the shade level of the room:")
print("1. Little Shade\n2. Moderate Shade\n3. Abundant Shade")
shade_selection = int(input("Please select from the options above (1, 2, or 3): "))

# Step 5: Determine AC capacity based on room size and shade level
if room_area < 250:
    btu = 5500
elif 250 <= room_area <= 500:
    btu = 10000
elif 501 <= room_area <= 1000:
    btu = 17500
else:
    btu = 24000

# Adjust BTU based on shade level
if shade_selection == 1:
    btu += btu * 0.15  # Increase by 15% for little shade
elif shade_selection == 3:
    btu -= btu * 0.10  # Decrease by 10% for abundant shade

# Step 6: Display the header
print("Air Conditioning Window Unit Cooling Capacity")

# Step 7: Display the output
print(f"Room Area (in square feet): {room_area}")
print("Amount of Shade: ", end="")
if shade_selection == 1:
    print("Little Shade")
elif shade_selection == 2:
    print("Moderate Shade")
elif shade_selection == 3:
    print("Abundant Shade")
print(f"BTUs per Hour needed: {round(btu)}")