#Create soduku table
import math
import random
from itertools import cycle

def main():

    rows = int(input("How many rows do you want your Soduku game to have?"))
    if not math.sqrt(rows).is_integer():
        print("Please try again, Soduku only works with square numbers. Eg. 4,9,16,25,36,49,64,81,100,121")
        return None

    total_boxes = rows * rows
    licycle = cycle(range(total_boxes))
    possible_numbers = range(1, rows + 1)



'''
    print ("Generating Table")
    table = []
    available_numbers = list(range(1,rows+1))
    print ('original available numbers %d', available_numbers)
    used_number = random.choice(available_numbers)
    print ('used number %d' %used_number)

    if used_number in available_numbers:
        available_numbers.remove(used_number)

    print (available_numbers)

    used_number = random.choice(available_numbers)
    print('used number %d' % used_number)

    if used_number in available_numbers:
        available_numbers.remove(used_number)

    print(available_numbers)
    '''

    available_numbers = list(range(1, rows + 1))

    for x in range(rows):



        table.append(
                        random.choice(available_numbers) for x in range(rows)


                     )


    print ("Generating Choices")
    box_choices = []
    for i in range(total_boxes):
        box_choices.append(list(possible_numbers))

    print (table)
    print (box_choices)






'''
    for row, rowvalue in enumerate(table):
        rowvalue[i]

        if rowvalue[0] == 0:
            print ("Unknown Number")

        for column, colvalue in enumerate(rowvalue):
            #print("Row: %d" % row)
            #print("Column: %d" % column)
            #print("Value: %d" % colvalue)
            pass
        break

'''
'''
    total_boxes = rows * rows
    print ('Total Boxes:' + str(total_boxes))
    possible_numbers = range(1,rows+1)
    print (list(possible_numbers))
    box_choices = []
    table = {}

    licycle = cycle(possible_numbers)



    print(box_choices)

    for i in range(total_boxes+1):
        table[i] = next(licycle)

    #print (box_choices)


    table[1] = 0
    print (table)

    row_number = 4
    column_number = 4

    #rownumbers = range(row_number*rows-rows-1,row_number*rows+1)
    #columnnumbers = range(column_number+1,total_boxes,rows)


    boxrow = math.ceil(row_number/math.sqrt(rows))
    boxcolumn = math.ceil(column_number/math.sqrt(rows))
    print (boxrow, boxcolumn)

    #if value == 0:
'''


if __name__ =='__main__':
    main()