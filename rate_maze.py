import random

def generate(n):
    data = []
    for i in range(n):
        temp = []
        for j in range(n):
            chance = random.random()
            if chance <= .20:
                temp.append("✅")
            else:
                temp.append("❌")
        data.append(temp)
    data[0][0] = "𝗦"
    data[-1][-1] = "𝗘"
    return data

def maze_print(data):
    n = len(data)
    for i in range(n):
        print("\033[0;31;40m\n",end='')
        print("+-----------"*n,"+",sep='',end='')
        print("\033[0;37;40m\n",end='')

        temp = data[i]
        for j in temp:
            print("\033[0;31;40m| ",sep='',end='')
            if j == "✅":
                print("\033[0;33;40m",j,' ',sep='',end='')
            elif j == "❌":
                print("\033[0;34;40m",j,' ',sep='',end='')
            else:
                print("\033[0;37;40m",j,' ',sep='',end='')

        print("\033[1;31;40m| ",sep='',end='')

   
    print("\033[0;31;40m\n",end='')
    print("+--------- "*n,"+",sep='')
    print("\033[0;37;40m",end='')
   

def highlight(s):
    print()
    print("\033[0;31;40m ---------",sep='',end='')
    print("\033[1;33;40m ",s,sep='',end='')
    print("\033[0;31;40m ---------",sep='',end='')
    print("\033[0;37;40m",sep='')

def solve(i = 0,j=0):
    global solved_data
    global flag
    n = len(solved_data)

    if flag or (i == n-1 and j == n-1):
        flag = True
        return
    
    if i < n-1 and solved_data[i+1][j] not in "✅⭕":
        solved_data[i+1][j] = "⭕"
      
        solve(i+1,j)
        if flag == False:
            solved_data[i+1][j] = "❌"
    
    if flag == False and j < n-1 and solved_data[i][j+1] not in "✅⭕":
        solved_data[i][j+1] = "⭕"
       
        solve(i,j+1)
        if flag == False:
            solved_data[i][j+1] = "❌"

def maze(i = 0,j=0):
    global solved_data
    global flag
    n = len(solved_data)

    if flag or (i == n-1 and j == n-1):
        flag = True
        return
    
    if flag == False and i < n-1 and solved_data[i+1][j] not in "✅⭕":
        solved_data[i+1][j] = "⭕"
      
        maze(i+1,j)
        if flag == False:
            solved_data[i+1][j] = "❌"

    if flag == False and j < n-1 and solved_data[i][j+1] not in "✅⭕":
        solved_data[i][j+1] = "⭕"
      
        maze(i,j+1)
        if flag == False:
            solved_data[i][j+1] = "❌"
    
    if flag == False and i>0 and solved_data[i-1][j] not in "✅⭕":
        solved_data[i-1][j] = "⭕"
      
        maze(i-1,j)
        if flag == False:
            solved_data[i-1][j] = "❌"

    if flag == False and j>0 and solved_data[i][j-1] not in "✅⭕":
        solved_data[i][j-1] = "⭕"
       
        maze(i,j-1)
        if flag == False:
            solved_data[i][j-1] = "❌"

def int_input(place_holder ="",minimum = float('-inf'),maximum= float('inf')):
    n = 0
    while not n:
        try:
            n = int(input(place_holder))
            while n< minimum or n > maximum:
                print()
                print("Enter Number Between",minimum, "to",maximum)
                n = int(input(place_holder))
        except:
            n = 0
            print()
            print("Entering  only number")
    return n


            
highlight("Well Come ")
highlight("Rat in Maze")
print()

choice = 2
while choice != 3:

    if choice == 2:
        n = int_input("Maze of Size?: ",3,15)
        data = generate(n)
        maze_print(data)

    elif choice == 1:
        flag = False
        solved_data = data.copy()

        solve()
        if flag == False:
            maze()
        if flag:
            solved_data[-1][-1] = "𝗘"
            
            highlight("Solve the Maze")
            maze_print(solved_data)
        else:
            highlight("Rat cant not cross the maze")
            print()
        
        flag = False
        solved_data = data.copy()


    if choice != 1:
        print()
        print("1. Print the Path")
        print("2. Generate another Maze")
        print("3. Exit the Game")

        choice = int_input("Enter your choice (1 or 2 or 3): ",1,3)
    else:
        print()
        print("1.⚪⚪⚪⚪⚪⚪⚪⚪⚪")
        print("2. Generate another Maze")
        print("3. Exit the Game")

        choice = int_input("Enter your choice (1 Or 2 Or 3): ",2,3)