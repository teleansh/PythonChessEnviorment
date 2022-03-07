b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")


def newBoard():
    
    b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")
        
def display(): #black side view 
    c= 1
    for i in b:
        print(i,end='')
        if c==8 : 
            c=0
            print()
        c+=1


def move(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    b[fnum], b[tnum] = '.',b[fnum]
    
    display()
    
        

def conv(s):
    num = int(s[1])
    alp = s[0]
    a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    alpn = a[alp]
    return ((num-1)*8)+alpn


def rookValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    con1,con2=False,False
    con1=False
    if abs(fnum-tnum)%8==0:
        con1=True
    rows=[range(0,8),range(8,16),range(16,24),range(24,32),range(32,40),range(40,48),range(48,56),range(56,64)]
    for k in rows:
        if fnum in k and tnum in k:
            con2=True
    if con2:
        for l in range(fnum+1,tnum):
            if b[l] != '.':
                con2=False

    mi =min(fnum,tnum)
    ma = max(fnum,tnum)
    
    if con1:
        while mi < ma:
            mi+=8
            if b[mi] !='.': con1=False

    return con1 or con2 




def kingValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    con=False
    if fnum%8!=0:
        val = [fnum+1 , fnum-1,fnum+8,fnum-8]
        if fnum in val : con=True
    return con

def pawnValid(fr,to,c):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1

    
    if c=='w':
        if fr in range(8,16): vm = [fnum+8,fnum+16] 
        else : vm= [fnum+8]
        
        if b[fnum+7].isupper(): vm.append(fnum+7)
        if b[fnum+9].isupper(): vm.append(fnum+9)

        if tnum in vm and not b[tnum].islower(): return True
        else: return False
        
    if c=='b':
        if fr in range(48,56): vm = [fnum-8,fnum-16] 
        else : vm= [fnum-8]
        
        if b[fnum-7].islower(): vm.append(fnum+7)
        if b[fnum-9].islower(): vm.append(fnum+9)

        if tnum in vm and not b[tnum].isupper(): return True
        else: return False
        
def bishopValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    con1=False
    if abs(fnum-tnum)%9==0 or abs(fnum-tnum)%7==0:
        con1 = True

    if (fnum-tnum)%9==0:
        while fnum!=tnum:
            tnum+=9
            if b[tnum]!='.' : return False

    if (fnum-tnum)%7==0:
        while fnum!=tnum:
            tnum+=7
            if b[tnum]!='.' : return False

    if (tnum-fnum)%9==0:
        while tnum!=fnum:
            fnum+=9
            if b[fnum]!='.' : return False

    if (tnum-fnum)%7==0:
        while tnum!=fnum:
            fnum+=7
            if b[fnum]!='.' : return False
    return con1

def queenValid(fr,to):
    return bishopValid(fr,to) or rookValid(fr,to)


    
        


 
