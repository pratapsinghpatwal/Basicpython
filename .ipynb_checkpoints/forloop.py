expenses = [1234,553,3354,444]

total = expenses[0] +expenses [1] + expenses[2]
print(f' Total expenses  {total}')

# for t in expenses :
#     print(t)
total=0
for i in range(len(expenses)) :
    print("Month " , i+1,"  " ,end="")
    total = total + expenses[i]
    print(expenses[i])
print(f"Total exepenses  {total}")

 