b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")


def newBoard():
    
    b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")
        
def display(): #black side view 
    c= 1
    for i in b[::-1]:
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
    con1,con2,con3=False,False,False
    if abs(fnum-tnum)%8==0:
        con1=True
    rows=[range(0,8),range(8,16),range(16,24),range(24,32),range(32,40),range(40,48),range(48,56),range(56,64)]
    for k in rows:
        if fnum in k and tnum in k:
            con2=True   
    if con2:                        #verifies if path is clear if fr and to are in same row
        for l in range(fnum+1,tnum):
            if b[l] != '.':
                con2=False

    mi =min(fnum,tnum)
    ma = max(fnum,tnum)
    
    if con1:
        while mi < ma:
            mi+=8
            if b[mi] !='.':
                con1=False

    if (b[fnum].isupper() and not b[tnum].isupper()) or (b[fnum].islower() and not b[tnum].islower()) : con3 = True
    return (con1 or con2) and con3




def kingValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    if not addressValid(fnum,tnum): return False
    
    con1,con2=False,False
    if fnum%8!=0 and fnum%9!=0:
        val = [fnum+1 , fnum-1,fnum+8,fnum-8]
    elif fnum%8==0: val =[fnum+8 , fnum-8,fnum-1]
    else: val =[fnum+8 , fnum-8,fnum+1]
    if fnum in val : con=True

    if (b[fnum].isupper() and not b[tnum].isupper()) or (b[fnum].islower() and not b[tnum].islower()) : con2 = True
        
    return con1 and con2

def pawnValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    if not addressValid(fnum,tnum): return False

    if fr.isupper() : c='b'
    if fr.islower() : c='w'
    
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
    if not addressValid(fnum,tnum): return False
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
            
    if (b[fnum].isupper() and not b[tnum].isupper()) or (b[fnum].islower() and not b[tnum].islower()) : con2 = True
    
    return con1 and con2

def queenValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    if not addressValid(fnum,tnum): return False
    return bishopValid(fr,to) or rookValid(fr,to)

def knightValid(fr,to):
    fnum = (conv(fr))-1
    tnum = (conv(to))-1
    if not addressValid(fnum,tnum): return False
    if tnum in [fnum+17,fnum-17,fnum+15,fnum-15,fnum+10,fnum-6,fnum+6,fnum-10]: con1=True
    if (b[fnum].isupper() and not b[tnum].isupper()) or (b[fnum].islower() and not b[tnum].islower()) : con2=True
    return con1 and con2

def addressValid(fnum,tnum):
    return 0<=fnum<64 and 0<=tnum<64

def rookMoves(pos):
    #code goes here
    print()
