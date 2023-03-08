def find_total(expen) :
    total=0
    for e in expen :
        total=total + e
    return total

exp_raju= [20,40,50,60,50]
exp_bhanu=[30,40,40,30,80]

total=find_total(exp_raju)
print(f'Raju total exp {total}')

total=find_total(exp_bhanu)
print(f'Bhanu total exp {total}')