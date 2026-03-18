name = input("Enter name :")

if len(name)%2==0:
    print(name)

else:
    mid = len(name)//2

    print(name[mid-1]+name[mid]+name[mid+1])     

    
            


