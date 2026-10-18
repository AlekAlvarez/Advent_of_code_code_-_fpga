import math
file=open('pIn2.txt')
line=file.read()
idRanges=line.split(",")
track=0
for idRange in idRanges:
    nums=idRange.split('-')
    first=int(nums[0])
    second=int(nums[1])
    for num in range(first,second+1):
        string=str(num)
        if len(string)%2==0:
            if string[0:len(string)//2]==string[len(string)//2:]:
                track+=num
print(track)