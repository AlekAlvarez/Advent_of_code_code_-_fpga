position=50
track=0
with open('problem1In.txt','r') as file:
    for line in file:
        prev=position
        if(line[0]=='L'):
            position-=int(line[1:])
        else:
            position+=int(line[1:])
        if position==0:
            track+=1
        elif position<0:
            track+=1+abs(position)//100
            if prev==0:
                track-=1
            position+=(1+(-position)//100)*100
            position=position%100
        elif position>=100:
            track+=position//100
            position=position%100
        
print(track)