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
        for i in range(2,len(string)+1):
            if len(string)%i==0:
                check=True
                start=0
                word_len=len(string)//i
                second_start=word_len
                for j in range(i-1):
                    if string[start:second_start]!=string[second_start:second_start+word_len]:
                        check=False
                        break
                    start+=word_len
                    second_start+=word_len
                if check:
                    track+=num
                    break        
print(track)