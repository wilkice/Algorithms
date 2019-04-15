'''
find integer under 1000 to make a3+b3=c3+d3
'''
all_result = {}
pairs_result = []
def add(num):
    for i in range(1,num+1):
        for j in range(i, num+1):
            result = i ** 3 + j ** 3
            # 不在字典里就添加
            if result not in all_result.keys():
                all_result[result]=[(i,j)] 
            else:
            # 添加新的数字队到字典的值， 且把这个值加到新列表，此表是有2个数字队的result组成的，后面直接从这里取值
                all_result[result].append((i, j))
                pairs_result.append(result)
    print('all been added')

    for result in pairs_result:
        print(result, all_result[result])

add(1000)