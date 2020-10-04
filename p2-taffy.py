import random
import taffy

#inputting random numbers from 1-6 (representing the 6 different taffies) into the 2D array. 
def random_array(array_2d):
    for i in range(9):
        for j in range(7):
            placement=random.randrange(1, 7)
            array_2d[i][j]=placement

# Just for just making sure the starting table will not have 3 same taffy horizontal or vertical, will stop right away when it finds a match
#check horizontally 3 same number in the array (each number 1-6 represents a different taffy)
def check_for_same_horizontal(array_2d):
    for i in range(9):
        counter_hori=1
        for j in range(6):
            if array_2d[i][j]==array_2d[i][j+1]:
                #if the number to the right of it is the same, add one to the counter
                counter_hori+=1 
            else:
                counter_hori=1
            if counter_hori>=3: #THIS STOPS RIGHT AWAY WHEN THE COUNTER HITS 3!
                #if the counter number is greater or equal to 3 means its 3 same one so return True
                return True
    return False 

#Check vertically for 3 same number in the array (1-6 each number is a different taffy)
def check_for_same_vertical(array_2d):
    #the rows need to change first before the column number changes
    for j in range(7):
        counter_vert=1
        for i in range(8):
            if array_2d[i][j]==array_2d[i+1][j]:
                #if the number below it is the same, add one to the counter
                counter_vert+=1
            else:
                counter_vert=1
            if counter_vert>=3: #THIS STOPS RIGHT AWAY WHEN THE COUNTER HITS 3!
                #if the counter is greater or equal to 3, means its 3 same taffy, return True
                return True
    return False

#changing the indexies to points 
def array_to_x_point(j):
    x=(4*j)-12
    return x
def array_to_y_point(i):
    y=(-4*i)+16
    return y

#changing the points to indexies 
def x_point_to_j(mx):
    j=int(((mx+14)/28)*7)
    return j
def y_point_to_i(my):
    i=int(((my-18)/36)*-9)
    return i
#BY THE WAY int(6.5)=6 and int(6.7)=6

#drawing the taffies onto the grid thing
def draw_taffy_on_grid(array_2d):
    for i in range(9):
        for j in range(7):
            if array_2d[i][j]==1:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic1(x, y)
            if array_2d[i][j]==2:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic2(x, y)
            if array_2d[i][j]==3:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic3(x, y)
            if array_2d[i][j]==4:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic4(x, y)
            if array_2d[i][j]==5:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic5(x, y)
            if array_2d[i][j]==6:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.pic6(x, y)
            if array_2d[i][j]==0:
                x=array_to_x_point(j)
                y=array_to_y_point(i)
                taffy.picwhite(x, y)

#check if the index is adjacent to the previous index
def adjacency(i, j, i_second, j_second):
    if i==i_second and j+1==j_second:
        return True
    if i==i_second and j-1==j_second:
        return True
    if i+1==i_second and j==j_second:
        return True
    if i-1==i_second and j==j_second:
        return True
    return False

#making sure i and j are in range
def i_j_in_valid_range(i, j):
    if 0<=i<=8 and 0<=j<=6:
        return True
    return False

#make the function so that it finds all of the matches instead of just the first one. maybe make an array that stores the i and j values?
def finding_all_horizontally(array_2d, location_array):
    #the rows need to change first before the column number changes
    for i in range(9):
        number_of_same_hori=1
        for j in range(6):
            if array_2d[i][j]==array_2d[i][j+1]:
                #if the number to the right it is the same, add one to the counter
                number_of_same_hori+=1
            else:
                number_of_same_hori=1
            if 3<=number_of_same_hori<=8:
                for w in range(number_of_same_hori): 
                    location_array[i][j-w+1]=1
                    #if the number of same is greater than 3 but less than the number of columns, go back that number of times and make it all equal to 1
    return location_array

#find all the vertical ones
def finding_all_vertically(array_2d, location_array):
    for j in range(7):
        number_of_same_vert=1
        for i in range(8):
            if array_2d[i][j]==array_2d[i+1][j]:
                #if the number below is the same, add one to the counter
                number_of_same_vert+=1
            else:
                #if not then reset it back to 1
                number_of_same_vert=1
            if 3<=number_of_same_vert<=10:
                for w in range(number_of_same_vert):
                    location_array[i-w+1][j]=1
                    #if the number of same is greated than 3 but less than the number of rows go back and make it all equal to 1
    return location_array

#SET EVERYTHING BACK TO ZERO BEFORE YOU TEST 
def set_back_to_zero(location_array):
    for i in range(len(location_array)):
        for j in range(len(location_array[i])):
            location_array[i][j]=0
    return location_array

# if the location array has 1 then replace all the number in the arrya_2d with 0
def replace_array(location_array, array_2d):
    for i in range(len(location_array)):
        for j in range(len(location_array[i])):
            if location_array[i][j]==1:
                array_2d[i][j]=0
    return array_2d

#NOW just need to make it fall
#if the array_2d is 0,  then check above it and then it would equal to the number above it. If there is no number above it then random generate a number. 
def fall_vert_hori(array_2d, location_array):
    for i in range(9):
        for j in range(7):
            if location_array[i][j]==1:
                #this needs to replace the things above each of it not just the same taffy come down because its above it. (WORKS FOR HORIZONTAL MATCH)
                for w in range(i+1):
                    k=i-w
                    x=array_to_x_point(j)
                    y=array_to_y_point(k)
                    taffy.clear_taffy(x, y)
                    array_2d[k][j]=array_2d[k-1][j] #gets the row directly above it.
                    if k!=0:
                        draw_taffy_on_grid(array_2d)
                    if k==0: 
                        a=random.randrange(1, 7)
                        array_2d[k][j]=a
                    draw_taffy_on_grid(array_2d)
    return array_2d

#keeping track of the score:
def count_score(location_array, score):
    for i in range(len(location_array)):
        for j in range(len(location_array[i])):
            if location_array[i][j]==1:
                score+=1
    return score


#CODE STARTS HERE 
##############################

mouse=True
fall=False
x_second=0.0
y_second=0.0
j_second=0
i_second=0
moves=15
score=0
target=50

#my lovely 2D 9x7 arrays...
array_2d=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
location_array=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

random_array(array_2d)
check_for_same_horizontal(array_2d)
check_for_same_vertical(array_2d)
#keep generating a random array until there is no 3 same horizontally or vertically
if check_for_same_horizontal(array_2d)==True or check_for_same_vertical(array_2d)==True:
    while check_for_same_horizontal(array_2d)==True or check_for_same_vertical(array_2d)==True:
        if check_for_same_horizontal(array_2d)==False and check_for_same_vertical(array_2d)==False:
            break
        random_array(array_2d)
        check_for_same_horizontal(array_2d)
        check_for_same_vertical(array_2d)

taffy.player_score(score) 
taffy.moves_remaining(moves) 
taffy.need_to_reach(target)

#while the game has not been won....
while True: 
    while fall:
        draw_taffy_on_grid(array_2d)
        taffy.show_stuff(50.0) 
        fall_vert_hori(array_2d, location_array) #each time it falls it needs to erase the previous taffies...
        hori=check_for_same_horizontal(array_2d)
        vert=check_for_same_vertical(array_2d) 
        fall=False
        if check_for_same_horizontal(array_2d) or check_for_same_vertical(array_2d):
            set_back_to_zero(location_array)
            finding_all_horizontally(array_2d, location_array)
            #finding all the vertical matches
            finding_all_vertically(array_2d, location_array)
            replace_array(location_array, array_2d)
            score=count_score(location_array, score)
            taffy.clear_message(-14.0, 18.0)
            taffy.player_score(score)
            fall=True
            #FIND THEM AND REPALCE WITH 0
            #THE FALL=TRUE AS TO MAKE IT FALL AGAIn
    if (moves==0 and score<target) or (moves!=-1 and score>=target):
        break
    #for every number (1, 2, 3, etc), change the index of the number to x, y coordinate and then draw out the picture. 
    draw_taffy_on_grid(array_2d)
        
    if mouse:
    #first mouse press
        if taffy.mouse_pressed():
            mx=taffy.mouse_coordinates()[0]
            my=taffy.mouse_coordinates()[1]
            j=x_point_to_j(mx)
            i=y_point_to_i(my)
            #if the mouse press is not adjacent to the first one (above, below, left, right) forbib the move i.e. the selection box moves to the other one
            if adjacency(i, j, i_second, j_second)==False:
                #the index must be between 8/ 6 other wise it will draw beyond the pictures
                if i_j_in_valid_range(i, j):
                    x=array_to_x_point(j)
                    y=array_to_y_point(i) 
                    #clear the previous one
                    #draw the box
                    taffy.clear_box(x_second, y_second)
                    taffy.draw_box(x, y)
                    #draw this once
                    mouse=False 
            else:
                if i_j_in_valid_range(i, j):
                    x=array_to_x_point(j)
                    y=array_to_y_point(i)
                    #clear the previous one
                    taffy.clear_box(x_second, y_second)
                    #draw the box
                    taffy.draw_box(x, y)
                    #draw this once
                    mouse=False 
    else:
        #if there is a second mouse press
        if taffy.mouse_pressed():
            mx_second=taffy.mouse_coordinates()[0]
            my_second=taffy.mouse_coordinates()[1]
            j_second=x_point_to_j(mx_second)
            i_second=y_point_to_i(my_second)
            #if the mouse press is not adjacent to the first one (above, below, left, right) forbib the move i.e. the selection box moves to the other one
            if adjacency(i, j, i_second, j_second)==False:
                # if the second click index is between 8/ 6 range then draw the thing
                if i_j_in_valid_range(i_second, j_second):
                    if i==i_second and j==j_second:
                        #getting it to clear the indication box if its clicked twice
                        taffy.clear_box(x, y)
                        mouse=True
                    else:
                        x_second=array_to_x_point(j_second)
                        y_second=array_to_y_point(i_second)
                        #clear the previous one and draw again. 
                        taffy.clear_box(x, y)
                        #draw the new box
                        taffy.draw_box(x_second, y_second)
                        mouse=True
            else:
                #if the stuff i click on the second time is the same taffy compared to the position first time click and will make at least a 3 same taffy, then swap the thing.
                #aka if the stuff i clicked is adjacent to the first click
                if i_j_in_valid_range(i_second, j_second):
                    x_second=array_to_x_point(j_second)
                    y_second=array_to_y_point(i_second)
                    taffy.clear_box(x, y)
                    #RIGHT NOW IS JUST SIMPLY SWAPPING THE TAFFY AND NUMBER IN THE ARRAY
                    first_number=array_2d[i][j]
                    second_number=array_2d[i_second][j_second]
                    array_2d[i][j]=second_number
                    array_2d[i_second][j_second]=first_number
                    taffy.show_stuff(50.0)
                    #forbid a move if it does not make a match of at least 3 horizontally or vertically
                    horizontal=check_for_same_horizontal(array_2d)
                    vertical=check_for_same_vertical(array_2d)
                    if check_for_same_horizontal(array_2d)==False and check_for_same_vertical(array_2d)==False:
                        #reswap things back
                        array_2d[i][j]=first_number
                        array_2d[i_second][j_second]=second_number
                        taffy.draw_box(x_second, y_second)
                        taffy.show_stuff(50.0)
                    else:
                        
                        taffy.clear_taffy(x, y)
                        taffy.clear_taffy(x_second, y_second)
                        #got to make the swap appear and thennnn do the delete on the second time...
                        draw_taffy_on_grid(array_2d)
                        taffy.show_stuff(50.0)
                        set_back_to_zero(location_array)
                        #finding the horizontal matches
                        finding_all_horizontally(array_2d, location_array)
                        #finding all the vertical matches
                        finding_all_vertically(array_2d, location_array)
                        score=count_score(location_array, score)
                        taffy.clear_message(-14.0, 18.0)
                        taffy.player_score(score)
                        replace_array(location_array, array_2d)
                        moves-=1 #used one move to make a match
                        taffy.clear_message(-1.0, 18.0)
                        taffy.moves_remaining(moves)
                        fall=True
                        #delete the all same one in a row...(or ust make it =0 in the array)
                        #IT NEED TO SWAF FIRST LIKE VISUALLY AND THEN IT delete
                    mouse=True

taffy.show_stuff(1400.0)

if moves==0 and score<target:
    taffy.lose_message()

if moves!=-1 and score>=target:
    taffy.win_message()

taffy.show_forever()
