import random
my_list=list(range(65,91))
my_list.extend(range(97,123))

chr_list=[]
for item in my_list:
    chr_list.append (chr (item))
for num in range(0,10):
  chr_list.append(str(num))
print (chr_list)
print(len (chr_list))
my=''

for num in range (10):
  my=my+random.choice(chr_list)
print (my)
