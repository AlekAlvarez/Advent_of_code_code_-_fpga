jolt_total=0
with open("pIn3.txt") as file:
    for line in file:
        m=0
        m_index=0
        for index,j in enumerate((line.strip())[0:len(line.strip())-1]):
            if int(j)>m:
                m=int(j)
                m_index=index
        s=0
        for j in (line[m_index+1:]).strip():
            if int(j)>s:
                s=int(j)
        jolt_total+=m*10+s
print(jolt_total)