d={}
n=int(input("Enter no of contacts:"))
for i in range(n):
   name=input("name:")
   num=input("phone number:")
   d[name]=num
print("Telephone Directory")
for i in d:
    print(i,":",d[i])
s=input("Enter name to search...")
if s in d:
   print("phone number is:",d[s])
else:
   print("contact not found!!!")
