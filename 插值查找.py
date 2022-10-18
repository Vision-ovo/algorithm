def interpolation_search(arr,left,right,target):
    if left > right or target < arr[0] or target > arr[-1]: #如果数组中没有待查找值返回False
        return False
    middle = left + int((right - left) * (target - arr[left]) / (arr[right] - arr[left])) 
    if target > arr[middle]: #右递归
        return interpolation_search(arr,middle + 1,right,target)
    elif target < arr[middle]:  #左递归
        return interpolation_search(arr,left,middle - 1,target)
    else:
        return middle
def creat_arr():
    arr = []
    num = int(input("请输入待查找数组的个数:"))
    print("请输入待查找数组的每个元素:")
    for i in range(num):
        arr.append(int(input()))
    return arr      
if __name__ == '__main__':
    arr = creat_arr()
    num = int(input("请输入待查找值:"))
    flag = interpolation_search(arr,0,len(arr)-1,num)
    if flag:
        print(f'数组:{arr},待查找值:{num},位置:{flag}')
    else:
        print(f'数组{arr}中没有值{num}')
