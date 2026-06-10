tasks=[]
while(True):
    print("1.addtask\n2.viewtask\n3.deletetask\n4.exit")
    n=int(input("hey user choose a task"))
    if(n==1):
        print("give the task")
        p=input("entered task!")
        tasks.append(p)
        print("Adding task succesfuly;")
    elif(n==2):
        j=len(tasks)
        for i in range(0,j):
            print(i+1,tasks[i])
    elif(n==3):
        if(j==0):
            print("list is empty")
            continue
        print("what!delete task")
        p=int(input("entered number"))
        if(p-1<0 or p-1>=j):
            print(" you want delete  invalid task")
        else:
            tasks.pop(p-1)
            print("deleted succesfully")
    elif(n==4):
        print("good bye")
        break