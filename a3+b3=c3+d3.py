'''
find integer under 1000 to make a3+b3=c3+d3
'''
def add():
    total = {}
    global sorted_list, add_list
    add_list=[]
    for i in range(1001):
        for j in range(i+1,1001):
            sum = i ** 3 + j ** 3
            if sum in total:
                total[sum] +=1
                add_list.append(sum)  # save at least have 2 pair integer into this list
            else:
                total[sum] = 1
    sorted_list = sorted(total.items(),key=lambda kv:kv[1])

add()
print(add_list)