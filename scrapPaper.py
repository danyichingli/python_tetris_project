pos =   {
        0 : [(1,0),(1,1),(0,1),(0,2)],
        1 : [(2,2),(1,2),(1,1),(0,1)],
        2 : [(2,0),(2,1),(1,1),(1,2)],
        3 : [(2,1),(1,1),(1,0),(0,0)]
        }
curr_points = pos[1]
next_points = pos[2]
diff = []
for i in range(4):
    curr_row = curr_points[i][0]
    curr_col = curr_points[i][1]
    next_row = next_points[i][0]
    next_col = next_points[i][1]
    diff.append((next_row-curr_row,next_col-curr_col))
print(diff)
