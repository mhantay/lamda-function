

des=input("Enter a Designation: ")
des.upper()
res=lambda pm,tm,dev,other: pm if (des=='pm') else(tm if des =='tm' else(dev if des=='dev' else '13%' ))
print(res('20%Hike','18%Hike','16%Hike','13% Hike'))


# des = input("Enter a Designation: ")
# des.upper()
# if des=="pm":
#     print("20% Hike")
# elif des=="tm":
#     print("18% Hike")
# elif des =="dev":
#     print("16% Hike")
# else:
#     print('13% Hike')


# print("Hello World")
a = (input("Enter a marks: "))
e=list(a.split(" "))
print((e))
a=int(e[0])
b=int(e[1])
c=int(e[2])
print(a)
print(b)
print(c)

res=[lambda x,y,z : x+y+z,      # Total Marks
     lambda x,y,z: (x+y+z)/3,   # Total Avg
     lambda x,y,z,m,n,p: m if 100>= (x+y+z)/3 > 90  else (n if 60<(x+y+z)/3 <=89 else p)  # Grad
    ] 
print(res[0](a,b,c))
print(res[1](a,b,c))
print(res[2](a,b,c,"A+","B+","C+"))














