# -*- coding = utf-8 -*-
# coding: utf-8
# @Time:20022/09/22
# @Author:王彤
# @Function:Quick Sort and Binary Search


def exception_handler(function): #专门用于没有查找值的情况
    def wrapper(target,arr,num):
        try:
            return function(target,arr,num)
        except IndexError:
            return -100
    return wrapper


@exception_handler
def binary_search(target,arr,num):
    location = False
    left,right = 0,len(arr) - 1
    middle = int((left + right)/2)   
    if target == arr[middle]:   
        location = middle
    elif target < arr[middle]:
        location = binary_search(target,arr[:middle],left)
    else:
        location = binary_search(target,arr[middle+1:],middle + 1)
    return location + num
    
def creat_arr():
    arr = []
    num = int(input("请输入待查找数组的个数:"))
    print("请输入待查找数组的每个元素:")
    for i in range(num):
        arr.append(int(input()))
    return arr                

def menu():
    print("二分查找")
    creat_arr()
    target = int(input("请输入您要查找的值:"))


    
if __name__=="__main__":
    #unordered_arr = [6,1,12,35,7,3,4,2,3,11,34]
    #ordered_arr = quick_sort(unordered_arr)
    #print(ordered_arr)
    print("二分查找:\n")
    flag = True
    while(flag):
        target = int(input("请输入您要查找的值:"))
        arr = creat_arr()
        location = binary_search(target,arr,0)
        if location == -100:
            print(f'数组{arr}中没有{target}!')
        else:
            print(f'待查找数组:{arr},查找目标:{target},位置:在第{location + 1}个(起始位置1)')

                                                                                                                                                   
