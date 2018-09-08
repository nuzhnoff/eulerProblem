###1мой вариант
"""lst0=[]
lst1=[3,5]
for val0 in range(100000):
    for x in range(len(lst1)):
        val1=val0%lst1[x]
        if val1==0:
            val2=len(lst0)
            if val2==0:
                lst0.append(val0)
            else:
                val3=lst0.count(val0)
                if val3==0:
                    lst0.append(val0)


print(sum(lst0))"""
#не мой вариант
v=0
for i in range(100000):
     if i%5==0 or i%3==0:
          v=v+i
print(v)


        
