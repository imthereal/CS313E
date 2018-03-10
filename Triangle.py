#  File: Triangle.py

#  Description:

#  Student's Name: Audrey McNay

#  Student's UT EID: alm5735

#  Partner's Name: Juan Zambrano

#  Partner's UT EID: jez346

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created: 3/4/18

#  Date Last Modified: 3/9/18

import time

# returns the greatest path sum using exhaustive search
def exhaustive_search(grid,i,idx,sol,sum_n):
  if(idx == len(grid)):
    sol.append(sum_n)   
  else:
    sum_n += grid[idx][i]
    exhaustive_search(grid,i ,idx +1,sol,sum_n) 
    exhaustive_search(grid,i+1,idx+1,sol,sum_n)
  return sol

# returns the greatest path sum using greedy approach ME
def greedy (grid):
  total = 0
  prev_col = 0
  for row in range(len(grid)):
    if len(grid[row]) > 1:
      if grid[row][prev_col] > grid[row][prev_col + 1]:
        total += grid[row][prev_col]
      else:
        total += grid[row][prev_col + 1]
        prev_col += 1
    else:
      total += grid[row][0]
  return total

# returns the greatest path sum using divide and conquer (recursive) approach ME
def rec_search (grid, row, index):
  #base case
  if row == (len(grid)-1):
    return grid[row][index]
  #recursive case
  else:
    return grid[row][index] + max((rec_search(grid, row+1, index)), rec_search(grid, row+1, index+1))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  for i in range(len(grid)-1,0,-1):
    for j in range(i):
      if grid[i][j] > grid[i][j+1]:
        grid[i-1][j] += grid[i][j]
      else:
        grid[i-1][j] += grid[i][j+1]
  return (grid[0][0])

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  #open file for reading
  in_file = open ('triangle.txt')

  #read number of lines
  line = in_file.readline()
  line = line.strip()
  line = int(line)

  triangle = []
  #read triangle lines from file 
  for i in range(line):
    triline = in_file.readline()
    triline = triline.strip()
    triline = triline.split()
    triangle.append(list(map(int,triline)))

  return triangle

def main ():
  # read triangular grid from file
  grid = read_file()

  # print time taken using exhaustive search
  ti = time.time()
  exhaust = max(exhaustive_search(grid,0,0,[],0))
  tf = time.time()
  del_t = round((tf - ti),3)
  print('The greatest path sum through exhaustive search is ' + str(exhaust)+'.')
  print('The time taken for exhaustive search is', str(del_t), 'seconds.')
  print()

  # print time taken using greedy search
  ti = time.time()
  greed = greedy(grid)
  tf = time.time()
  del_t = round((tf - ti),3)
  print('The greatest path sum through greedy search is ' + str(greed)+'.')
  print('The time taken for greedy search is', str(del_t), 'seconds.')
  print()

  # output greates path from divide-and-conquer approach
  ti = time.time()
  rec = rec_search(grid,0,0)
  tf = time.time()
  del_t = round((tf - ti),3)
  print('The greatest path sum through recursive search is ' + str(rec)+'.')
  print('The time taken for recursive search is', str(del_t), 'seconds.')
  print()

  # output greates path from dynamic programming 
  ti = time.time()
  dyn = dynamic_prog(grid)
  tf = time.time()
  del_t = round((tf - ti),3)
  print('The greatest path sum through dynamic programming is ' + str(dyn)+'.')
  print('The time taken for dynamic programming is', str(del_t), 'seconds.')
  print()

if __name__ == "__main__":
  main()
