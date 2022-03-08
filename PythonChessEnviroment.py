b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")


def newBoard():
    
    b = "r n b q k b n r p p p p p p p p".split(" ") + ['.']*32 + "p p p p p p p p r n b q k b n r".upper().split(" ")
        
def display(): #white side view 
    c , k= 1 ,0
    ap = range(1,9)[::-1]
    row,col=[],[]
    for i in b:
        row.append(i)
        if c==8 : 
            c=0
            col.append(row)
            row=[]
        c+=1

    for j in col[::-1]:
        print(ap[k] , " |" ,end=" ")
        for i in j:
            print(i,end=' ')
        print()
        k+=1
    print("   ",end="")
    print("-"*18,"     A B C D E F G H",sep="\n")


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
    num=(conv(pos))-1                   #num is index
    if b[num].isupper() : c='b'
    elif b[num].islower() : c='w'
    else: return "Block is empty"
    vm=[]
    col=(num+1)%8
    if col==0: col=8
    
    row=int(pos[1])
    
    if c=='w':
        block=num+8
        while row<=8:
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block+=8
            row+=1

        row=int(pos[1])

        
        block=num-8
        while row>0:
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block-=8
            row-=1

        tcol=col+1                      #col is from 1 to 8 , row is from 1 to 8
       
 
        block =num+1
        while tcol<=8:
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            
            block+=1
            tcol+=1

        block =num-1
        tcol=col
        while tcol>1:
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block-=1
            tcol-=1

        tcol=col
        row=int(pos[1])
        

    if c=='b':
        block=num+8
        while row<=8:
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            block+=8
            row+=1

        row=int(pos[1])

        
        block=num-8
        while row>1:
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            block-=8
            row-=1

        tcol=col+1                      #col is from 1 to 8 , row is from 1 to 8
       
 
        block =num+1
        while tcol<=8:
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            
            block+=1
            tcol+=1

        block =num-1
        tcol=col
        while tcol>1:
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            block-=1
            tcol-=1

    
    move=[]
    for l in vm:
        move.append(numToAlg(l))

    return move

def bishopMoves(pos):
    num=(conv(pos))-1
    if b[num].isupper() : c='b'
    elif b[num].islower() : c='w'
    else: return "Block is empty"
    vm=[]
    col=(num+1)%8
    if col==0: col=8
    
    row=int(pos[1])+1
    
    if c=='w':

        tcol=col+1
        row=int(pos[1])+1
        block=num+9
        
        while row<=8 and col<=8 :                  #goes top right
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block+=9
            row+=1
            tcol+=1

        row=int(pos[1])-1
        tcol=col-1
        
        block=num-9
        
        while row>0 and tcol>1:                 #goes below left
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block-=9
            row-=1
            tcol-=1

        row=int(pos[1])-1
        tcol=col+1                      
       
 
        block =num-7
        while tcol<=8 and row>1:                              #goes below right
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            
            block-=7
            tcol+=1
            row-=1

        block =num+7
        tcol=col-1
        row=int(pos[1])+1

        while tcol>0 and row<=8:                                   #goes top left
            if b[block] == '.' : vm.append(block)
            if b[block].isupper() :
                vm.append(block)
                break
            if b[block].islower():
                break
            block+=7
            tcol-=1
            row+=1


    if c=='b':

        tcol=col+1
        row=int(pos[1])+1
        block=num+9
        
        while row<=8 and col<=8 :                  #goes top right
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            block+=9
            row+=1
            tcol+=1

        row=int(pos[1])-1
        tcol=col-1
        
        block=num-9
        
        while row>0 and tcol>1:                 #goes below left
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            block-=9
            row-=1
            tcol-=1

        row=int(pos[1])-1
        tcol=col+1                      
       
 
        block =num-7
        while tcol<=8 and row>1:                              #goes below right
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].isupper():
                break
            
            block-=7
            tcol+=1
            row-=1

        block =num+7
        tcol=col-1
        row=int(pos[1])+1

        while tcol>0 and row<=8:                                   #goes top left
            if b[block] == '.' : vm.append(block)
            if b[block].islower() :
                vm.append(block)
                break
            if b[block].upper():
                break
            block+=7
            tcol-=1
            row+=1
        

    

    
    move=[]
    for l in vm:
        move.append(numToAlg(l))

    return move


def queenMoves(pos):
    return rookMoves(pos) + bishopMoves(pos)


def knightMoves(pos):
    num = conv(pos)-1   #num is index
    vm = [num-17,num-15,num-10,num-6,num+6,num+10,num+15,num+17]

    if vm[3]%8 in [0,1]:
        vm.pop(3)
        vm.pop(5)
    if vm[4]%8 in [6,7]:
        vm.pop(4)
        vm.pop(2)
    
    tvm=[]
    
    for i in vm:
        if (i>=0 and i<=63) and not ((b[num].isupper and b[i].isupper()) or (b[num].islower and b[i].islower())) : tvm.append(i)
    move=[]
    for l in tvm:
        move.append(numToAlg(l))
    return move

def kingMoves(pos):
    num = conv(pos)-1   #num is index
    vm = [num+8,num-8,num+9,num-9,num+7,num-7,num+1,num-1]

    if vm[2]%8==0:
        vm.pop(2)
        vm.pop(6)
        vm.pop(5)
    if vm[3]%8 ==7:
        vm.pop(3)
        vm.pop(-1)
        vm.pop(4)
    
    tvm=[]
    
    for i in vm:
        if (i>=0 and i<=63) and not ((b[num].isupper and b[i].isupper()) or (b[num].islower and b[i].islower())) : tvm.append(i)
    move=[]
    for l in tvm:
        move.append(numToAlg(l))
    return move

def pawnMoves(pos):
    #to be worked upon
    return True


        
def numToAlg(ind):
    alp=(ind+1)%8
    n=((ind+1)//8) + 1
    if alp==0:
        n-=1
    a = {0:'h',1 : 'a' , 2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
    return str(a[alp]) + str(n)
    
