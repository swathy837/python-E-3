list=[]
n=int(input("enter number of elements:"))
for i in range(n):
    list.append(int(input("enter element:")))
while True:
    print("\n MENU")
    print("1. Add Element at specified position")
    print("2. add Element at end of list")
    print("3. compare two lists")
    print("4. print id of all elements")
    print("5. first occurance of all elements")
    print("6.exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        pos=int(input("enter position:"))
        val=int(input("enter value:"))
        list.append(val)
        list=list[:pos]+[val]+list[pos:-1]
        print("updated list...",list)
    elif choice==2:
        val=int(input("enter value:"))
        list.append(val)
        print("updated list...",list)
    elif choice==3:
        list2=[]
        n2=int(input("enter number of elements:"))
        for i in range(n2):
            x=int(input("enter element:"))
            list2.append(x)
        if list==list2:
            print("lists are equal...")
        else:
            print("lists are not equal...")
    elif choice==4:
        for i in list:
            print("Element:",i,"ID",id(i))
    elif choice==5:
        item=int(input("enter item:"))
        if item in list:
            print("first occurance at index:",list.index(item))
        else:
            print("item not exist")
    elif choice==6:
        break
    else:
        print("Invalid choice")
[25bcs167@mepcolinux ex3py]$python3 ex3e.py
enter number of elements:1
enter element:1
