sname=[]
sid=[]
spar=[]
sfee=[]
sclass=[]
def enter():
    c='y'
    while(c=='y'):
        
        sname.append(input("enter student name\t"))
        sid.append(input("enter student id\t"))
        sclass.append(input("enter class of student\t"))
        spar.append(input("enter parents name\t"))
        sfee.append(int(input("enter total fee of student\t")))
        c=input("cont??\t")
def display():
    for i in range(len(sname)):
        print("Name :{}\nClass:{}\nID:{}\nParent_Name:{}\nFEE:{}".format(sname[i],sclass[i],sid[i],spar[i],sfee[i]))
def search(sname,sid,sfee,sclass,spar):
    s_name=input("enter name to search\t")
    a=0
    for i in sname:
        if (i==s_name):
            print("name:{}\nsid:{}".format(i,sid[a],sfee[a]))
      
            choice=input("want to deduct fee??\n")
            if (choice=='y'):
                amt=int(input("enter amount..\n"))
                sfee[a]=sfee[a]-amt
                print("After paid")
                print("name:{}\nsid:{}\nclass:{}\nparent`s name:{}\nfee:{}\n".format(i,sid[a],sclass[a],spar[a],sfee[a]))
            a+=1
        else:
            print("\n\tNo record found for {}\t".format(s_name))
print("welcome !!!\n")
print("what you want to do??\n\n")
x=0
while (x!=4):
    print("\n1.To enter\n2.TO search Name\n3.TO display Record\n4.To exit")
    x=int(input("enter your choice...\n"))
    if(x==1):
        enter()
    elif (x==2):
        search(sname,sid,spar,sclass,sfee)
    elif(x==3):
        display()
    elif(x==4):
        exit
    else:
        print("invalid input")
