
li = [1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
tup = ()
for item in li:
   if item not in tup:
        tup+=(item,) 
        print item,'-',li.count(item)
       