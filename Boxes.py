#  File: Boxes.py

#  Description:

#  Student Name: Audrey McNay

#  Student UT EID: alm5735

#  Partner Name: Juan Zambrano

#  Partner UT EID: jez346

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 2/22/18

#  Date Last Modified: 2/24/18


def does_fit (box1, box2):
    return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def does_fit_4_all(subset):
    for i in range(len(subset) - 1):
        if not does_fit(subset[i],subset[i + 1]):
            return False
    return True

def subsets (a, b, lo, li):
    if lo == len(a):
      if does_fit_4_all(b):
        li.append(b)
        return
    else:
        c = b[:]
        b.append (a[lo])
        subsets (a, b, lo + 1, li)
        subsets (a, c, lo + 1, li)
        
def main():
    # open file for reading
    in_file = open ('boxes.txt', 'r')
    # read the number of boxes
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)
    # create empty list of boxes
    box_list = []
    li = []
    # read the list of boxes from file
    for i in range (num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for i in range(len(box)):
            box[i] = int(box[i])
        box.sort()
        box_list.append(box)
    # close the file
    in_file.close()
    # sort the box list
    box_list.sort()
    subsets(box_list,[],0,li)
    print("Largest Subset of Nesting Boxes")
    for i in [x for x in li if (len(x) == (len(max(li,key = len))))]:
        for j in i:
            print(j)
        print() 
main()