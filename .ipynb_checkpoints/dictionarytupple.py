exp=[1233,4455,3544,222]
point=(5,6,9,10,67)
print(point[0])
print(point[3])
# can not be assign value tupple are immutable
# point[2]=33

def find(price,eps,bookvalue) :
    pe=price*eps
    pb=price/bookvalue
    return pe,pb

per,pbr=find(100,2,4)
print(" per ratio ",per)
print("pb ration ",pbr)

  