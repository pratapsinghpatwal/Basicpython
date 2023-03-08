indian=['samosa','daal', 'naan']
chinese=['egg role','pot sticker', 'fried rice']
italian=['pizza',"pasta",'risotto']

dish=input("Enter the dish name")

if dish in indian :
    print(f'{dish} is indian food ')
elif dish in chinese :
    print(f'{dish} is chinese food')
elif dish in italian :
    print(f'{dish} is italian food')
else :
    print("Your choose wrong item choose the correct item")
