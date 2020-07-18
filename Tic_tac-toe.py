def display(li):
    print("---------")
    for j in range(2,-1,-1):
        print("|",end=" ")
        for i in range(0,3):
            print(li[i][j],end=" ")
        print("|")
    print("---------")

def get_cordinates():
    global count
    cordinate=input().split()
    if(len(cordinate)==2):
        if(count%2==0):
            f=0 #even X
        else:
            f=1
        condition(li,cordinate,f)

def condition(li,s,f):
    global count
    if(s[0].isdigit() and s[1].isdigit()): #digit or symbol check
        i=int(s[0])
        j=int(s[1])
        if(i>=1 and i<=3 and j>=1 and j<=3):  #number checking bw 1 to 3
            if(li[i-1][j-1]!=" "):  #cell occupied or not
                print("This cell is occupied! Choose another one!")
                get_cordinates()
            else:
                if(f==0):
                    li[i-1][j-1]='X'
                else:
                    li[i-1][j-1]='O'
                count+=1   #count has problem
                display(li)
            state_check(li) #calling state check
        else:
            print("Coordinates should be from 1 to 3!")
            get_cordinates()
    else:       #digit checking else
        print("You should enter numbers!")
        get_cordinates()

def state_check(li):
    x_c=o_c=s_c=c=0
    for i in range(0,3):
        for j in range(0,3):
            if(li[i][j]=='X'):
                x_c+=1
            elif(li[i][j]=='O'):
                o_c+=1
            else:
                s_c+=1
    for i in range(0,3): #row check
        if(li[i][0]==li[i][1]==li[i][2] and li[i][0]!=' '):
            c+=1
            a=li[i][0]
        if(li[0][i]==li[1][i]==li[2][i] and li[0][i]!=' '):  #column check
            c+=1
            a=li[0][i]
    if((li[0][0]==li[1][1]==li[2][2] or li[0][2]==li[1][1]==li[2][0]) and li[1][1]!=' '): #corner check
            c+=1
            a=li[1][1]
    if(c==1):
        print(a+" wins")
    elif(c==0 and s_c==0):
        print("Draw")
    elif((o_c+x_c)<9 and c!=1 and abs(o_c-x_c)<=1):
        #print("Game not finished")
        get_cordinates()
    elif(o_c==1 or x_c==1):
        get_cordinates()
    else:
        print("Impossible")
        

li=[[' ' for i in range(3)] for j in range(3)] 
count=0
display(li)

get_cordinates()




