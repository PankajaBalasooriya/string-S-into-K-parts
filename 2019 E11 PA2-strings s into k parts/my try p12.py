def getText(file_name):
    global string,k
    f=open(file_name,'r')
    string,str_k=f.read().strip().split('\n')
    k=int(str_k)
    f.close()
    return

def split(string):
    global u_list,k
    u_list=[]
    n=len(string)
    if n%k==0:
        b=0
        while b<=n:
            t=string[b:b+k]
            lst=[]
            u=''
            for x in t:
                if x not in lst:
                    u+=x
                    lst.append(x)
            u_list.append(u)
            b+=k
    else:
        u_list.append('Invalid Input.')
    return

def showResult(file_name):
    global u_list
    string='\n'.join(u_list)
    print(string)
    f=open(file_name,'w')
    f.write(string)
    f.close()
    return

input_file=input()
try:
    getText(input_file)
    split(string)
    showResult('Output.txt')
except FileNotFoundError:
    u_list=['Input file is not to be found.']
    showResult('Output.txt')
'''except ValueError:
    u_list=['Invalid input.']
    showResult('Output.txt')'''
