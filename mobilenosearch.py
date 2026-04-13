phone_book={}
n=int(input("Enter no of entries:"))
for i in range(n):
    number=input("Enter mobile no:")
    name=input("Enter person name:")
    phone_book[number]=name
search=input("Enter mobile no to search..")
if search in phone_book:
   print("Name:",phone_book[search])
else:
   print("Mobile no not found")
