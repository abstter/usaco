'''
ID: Abhiram Avasarala
LANG: PYTHON3
TASK: beads
'''
with open('beads.in', 'r') as fin:
    num_beads = int(fin.readline()) # Reads lines of the input file, which contains a string representing the colors of the beads and number in the necklace. The strip() method removes leading and trailing whitespaces.
    beads = fin.readline().strip() # reads lines 
    if num_beads != len(beads): # checks if number of beads in input are equal to length of beads - if not, print there is an error in input and exit
        print("Error in input: Number of beads specified is not equal to the length of the bead arrangement.")
        exit()

previous_color = prev_previous_color = '' # Initializes variables to keep track of previous colors encountered while going through the beads.
index = 0 # index(current position)
count_same_color = count_white = 0 # counters for consecutive beads of same color and number
max_beads = left_count = 0 # keeps track of maximum number kept so far and beads collected on left side
is_second = False # second pass through the necklace

while True:                                 # code iterates through each bead
    if beads[index] != previous_color:      # checks if current bead is diff from previous bead
        if beads[index] == 'w':             # if true, then it updates the counter
            count_white = 1                 # if white, then increments white counter
        else:
            if beads[index] == prev_previous_color: # checks if previous colors are same - update same color
                count_same_color = count_same_color + count_white + 1 # updates same color counter
                count_white = 0 # remains at 0 otherwise
            else:
                prev_previous_color = beads[index] 
                if left_count + count_same_color + count_white > max_beads: # updates counters and checks if left count, same color count and white count
                    max_beads = left_count + count_same_color + count_white # are greater than max beads. updates maximum beads
                if is_second:
                    break # checks if it is in second pass - then break from code

                left_count = count_same_color # assigning left count to the count of same color

                if previous_color == 'w':
                    count_same_color = count_white + 1 # same color increased if previous is white
                    count_white = 0
                else:
                    count_same_color = 1 

        previous_color = beads[index]
    else:
        if beads[index] == 'w': # shows if the bead is white then add to white counter
            count_white += 1
        else:
            count_same_color += 1 # same color is added

    index += 1 # increments index
    if index == num_beads: # checks if the end of necklace is reached
        if (count_same_color + count_white) == (num_beads * 2): # checks if all beads are same color or white
            max_beads = num_beads # entire necklace collected if true
            break # breaks then
        index = 0 # if not, prepares for second pass through necklace
        is_second = True

with open('beads.out', 'w') as fout:
    fout.write(f"{max_beads}\n")

# second pass needed - circular necklace(many breaking points and beads can be collected from both ends). there can be alternative starting points as well
# it will consider different segments of the necklace that may not have been considered in the first pass.
# Finds more possible solutions to getting max beads.