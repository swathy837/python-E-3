employees=()
n=int(input("enter no of employees: "))
for i in range(n):
    id=int(input("enter employee id: "))
    name=input("enter employee name: ")
    salary=int(input("enter employee salary: "))
    employees=employees+((id,name,salary),)
print("\nemployee detials:")
for e in employees:
    print(e)
s=int(input("enter id to search: "))
for e in employees:
    if e[0]==s:
        print("employee found :",e)
max_emp=employees[0]
for e in employees:
    if e[2]>max_emp[2]:
        max_emp=e[2]
print("employee with highest salary: ",max_emp)
print("\nemployee with  salary > 50000: ")
for e in employees:
    if e[2]>50000:
        print(e)
