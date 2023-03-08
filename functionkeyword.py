def find_cylinder_volume(radius,height) :
    print("redius ", radius)
    print("height ",height)
    return 3.14*(radius**2)*height
def pratap(x,y):  # function to return multiple values
    x=x+10
    y=y+10
    return x,y

r=5
h=10
# using argument keywords
cylender_volume=find_cylinder_volume(radius=r,height=h)
print(f"Cylendre volume is  {cylender_volume}")

m,n=pratap(10,20)
print("The value of m ",m)
print("The value of n ",n)
