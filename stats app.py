c = open("proteas_runs(2020-).txt", "r")
oil=c.readline()

def inputval():
    nom= 0
    
    while nom<=0:
        i=str(input("player   "))

        p=i.title()
    
        print ("Did you mean", p, "?")
    
        y=str(input("y/n?   "))
        if y == "y":
            nom= nom +1
    
    p=p.strip()
    return (p)
def formatc():
    m=0
    
    while m==0:
        form= str(input("Format     "))
        if form== "odi":
            return 2
        elif form =="test":
            return 1
        elif form== "t20i":
            return 3

p=inputval()
form= formatc()

o=""
to=0
co=0
check=""
kl=''

for line in c:
    o=line.strip()
    co=co+1
    if o==p:
        to= co
        check="1"

    if co==(to+1) and form==1 :
        print(1)
        print(line, end="")
    elif co== (to+2) and form== 2:
        
        print(line, end="")
        
    elif co ==(to+3) and form ==3:
        
        print (line, end="")

        

if check == "":
    print ("player does not exist")        

        
    
    
        
    

    
 