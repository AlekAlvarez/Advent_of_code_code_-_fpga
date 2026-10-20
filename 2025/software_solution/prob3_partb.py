jolt_total=0
with open("pIn3.txt") as file:
    for line in file:
        temp=0
        digs=[0,0,0,0,0,0,0,0,0,0,0,0]
        m_index=0
        t_index=0
        for index,j in enumerate((line.strip())[0:len(line.strip())-11]):
            if int(j)>digs[0]:
                digs[0]=int(j)
                m_index=index
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-10]):
            if int(j)>digs[1]:
                digs[1]=int(j)
                t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-9]):
                if int(j)>digs[2]:
                    digs[2]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-8]):
                if int(j)>digs[3]:
                    digs[3]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-7]):
                if int(j)>digs[4]:
                    digs[4]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-6]):
                if int(j)>digs[5]:
                    digs[5]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-5]):
                if int(j)>digs[6]:
                    digs[6]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-4]):
                if int(j)>digs[7]:
                    digs[7]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-3]):
                if int(j)>digs[8]:
                    digs[8]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-2]):
                if int(j)>digs[9]:
                    digs[9]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:len(line.strip())-1]):
                if int(j)>digs[10]:
                    digs[10]=int(j)
                    t_index=index
        m_index+=t_index+1
        for index,j in enumerate((line.strip())[m_index+1:]):
                if int(j)>digs[11]:
                    digs[11]=int(j)
        for i in digs:
            temp*=10
            temp+=i
        jolt_total+=temp
print(jolt_total)