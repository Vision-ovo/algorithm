from unittest import result

def verification(arr):
#用于验证数组是否还需要继续递归操作
    for i in range(len(arr) - 2):
        if arr[i] > arr[i+1]:  
            return True
    return False

def quick_sort(arr):
#快速排序
    try:
        reference_number = arr[0]
        right_pointer = len(arr) - 1
        left_pointer = 0
        while(left_pointer < right_pointer):
            if arr[right_pointer] < reference_number:
                for i in range(left_pointer-1,right_pointer):
                    left_pointer += 1   
                    if arr[left_pointer] > reference_number:
                        arr[right_pointer],arr[left_pointer] = arr[left_pointer],arr[right_pointer]
                        break
                    elif left_pointer == right_pointer:
                        arr[0],arr[left_pointer] = arr[left_pointer],arr[0]
                        break
            right_pointer -= 1
        if left_pointer == right_pointer:
            arr[0],arr[left_pointer] = arr[left_pointer],arr[0]
        while(verification(arr)):
            arr[:left_pointer] = quick_sort(arr[:left_pointer])
            arr[left_pointer + 1:] = quick_sort(arr[left_pointer + 1:])
        return arr
    except IndexError:
        return arr

def bubble_sort(arr):
#冒泡排序
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def menu():
    print("1.冒泡排序")
    print("2.快速排序")
    print("输入其他任意数字退出本程序！")

def creat_arr():
    arr = []
    num = int(input("请输入待排序数组的个数:"))
    print("请输入待排序数组的每个元素:")
    for i in range(num):
        arr.append(int(input()))
    return arr

    

if __name__ == "__main__":
    flag = True
    menu()
    while(flag):
        choose = int(input("请选择要实现的算法:"))
        if choose == 1:
            print("快速排序")
            arr = creat_arr()
            print(f'排序前：{arr}')
            print(f'排序后：{quick_sort(arr)}')
        elif choose == 2:
            print("冒泡排序")
            arr = creat_arr()
            print(f'排序前：{arr}')
            print(f'排序后：{bubble_sort(arr)}')
        else:
            flag = False
        

        
    
    


