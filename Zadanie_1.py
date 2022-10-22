def calc_x (V,M,a,t):
    #liczymy x
    x = [1] * (V+1)
    for n in range(1, V+1):
        sum = 0
        for i in range(0, M):
            if n >= t[i] :
                sum += a[i] * t[i] * x[n-t[i]]
        x[n] = sum/n
    return x
            
def calc_po(x):
    #liczymy p(0)
    sum = 0
    for i in x :
        sum += i
    return 1/sum
        
def calc_pn(x,V,M,a,t):
    #liczymy P
    P= [1] * (V+1)
    P[0] = calc_po(x)
    for n in range (1, V+1) :
        sum = 0
        for i in range (0, M) :
            if n >= t[i] :
                sum += a[i] * t[i] * P[n-t[i]]
        P[n] = sum/n
    return P
def calc_bn (P,V,t,i=1):
    #liczymy b1 i b2
    sum=0
    for n in range(V-t[i-1]+1,V+1):
        sum+=P[n]
    return sum
def calc_all(V,t,a,M):
    #funkcja zliczająca wszystko
    x=calc_x(V,M,a,t)
    print(x)
    #po=calc_po()
    P=calc_pn(x,V,M,a,t)
    print(P)
    b1=calc_bn(P,V,t)
    b2=calc_bn(P,V,t,i=2)
    print('x = {} P = {} b1 = {} b2 = {}'.format(x, P, b1, b2))


V=3 #pojemność wiązki
t=[1,2] #liczba żądanych jednostek przetwarzania
a=[0.4,1] #ruch oferowany
M=2 #strumienie ruchu

calc_all(V,t,a,M)
