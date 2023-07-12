
def readFile(file_path):
    try:
        pf = open(file_path,'r')
        lines = pf.readlines()
        pf.close()
        stn = lines[0].strip(' /n')
        num = int(lines[1].strip(' /n'))
    except:
        print("Error..")
    return stn,num

def lister(st):
    lis = []
    for i in st:
        if i not in lis:
            lis.append(i)
    return ''.join(lis)

def writter(st,num):
    len_num = len(st)//num
    times,un_div_part = divmod(len(st),num)
    cn = 0
    fin_output = ""
    while cn<times:
        st_part = st[len_num*cn:len_num*(cn+1)]
        fin_st = lister(st_part)
        fin_output+=fin_st+'\n'
        cn+=1
    fin_output += lister(st[-un_div_part:])+'\n'
    print(fin_output)

    wr = open('output.txt','w')
    wr.write(fin_output)
    wr.close()

st,num = readFile('test1.txt')
writter(st,num)


