position=50
track=0
with open('problem1In.txt','r') as file:
    for line in file:
        if(line[0]=='L'):
            position-=int(line[1:])
        else:
            position+=int(line[1:])
        if position<0:
            position+=100
        position=position%100
        if position==0:
            track+=1
print(track)