# 2) Depreciation table

rate = 4000
eoy = 28000
counter = 1

print("Year\tDepreciation\tEOY Value\tAcc. Dep.")
print("----\t-----------\t---------\t--------")

while eoy > 0:
    eoy = eoy - rate
    print(counter,"\t",rate,"\t\t",eoy,"\t\t",rate*counter)
    counter = counter + 1
