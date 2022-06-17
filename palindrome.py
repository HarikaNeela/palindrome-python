def palindrome(s):
    n=len(s)
    l=[]
    m=[]
    
    p=list(s)
   #print(p)
   
    if n%2==0:
        for x in p:
            l.append(x)
        p.reverse()
        for y in p:
            m.append(y)
        if(l==m):
            print("True")
        else:
            print("False")
    else:
        print("False")
 palindrome('helleh')