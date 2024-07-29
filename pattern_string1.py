even1=[]
odd=[]
def even():
    for num in range(1,50+1):
        if num % 2 == 0:
            #even += 1
            # e1=num
            even1.append(num)
        else:
            odd.append(num)
 
    print("Even numbers in the list: ", even1)
    print("Odd numbers in the list: ", odd)
even()