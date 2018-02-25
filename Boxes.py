#  File: Boxes.py

#  Description:

#  Student Name: Audrey McNay

#  Student UT EID: alm5735

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created:

#  Date Last Modified:

'''
def checkFit(box_list):
	if len(box_list) <= 1:
		return box_list
	elif (box_list[0][0] < box_list[1][0]) and (box_list[0][1] < box_list[1][1]) and (box_list[0][2] < box_list[1][2]):
		return box_list[0] + box_list[1] + checkFit(box_list[2:])
	else:
		return box_list[0] + checkFit(box_list[2:])

def main():
	#open file
	f = open("Boxes.txt")
	num_boxes = int(f.readline())

	box_list = []
	for i in range(num_boxes):
		line = f.readline().split(" ")
		if len(line) > 3:
			line.pop()
		box_list.append(sorted(map(int , line)))

	box_list.sort()

	print(box_list)
	print(checkFit(box_list))

main()
'''

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def subsets (a, b, lo, li):
  hi = len(a)
  if (lo == hi):
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

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()

  # create a list that will hold the nested boxes
  nested_boxes = []

  # get all subsets of boxes
  b = []
  li = []
  subsets(box_list, b, 0, li)

  # for each subset check if they all fit
  for combo in li:
    for boxx in range(len(combo) - 1):
      if not does_fit(combo[boxx], combo[boxx + 1]):
        break
      elif boxx == (len(combo)-2):
        nested_boxes.append(combo)
      else:
        continue

  # add to list
  li2 = []
  longest = len(max(nested_boxes,key=len))
  for i in nested_boxes:
    if len(i) == longest:
      li2.append(i)
    else:
      continue

  # print
  print("Largest Subset of Nesting Boxes")

  for i in li2:
    for j in range(len(i)):
      print(i[j])
    print()

main()