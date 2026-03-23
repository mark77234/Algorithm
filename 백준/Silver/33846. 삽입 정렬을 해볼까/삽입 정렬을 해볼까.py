import sys
input = sys.stdin.readline

def merge(left,right):
    i,j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i < len(left):
        sorted_list.append(left[i])
        i+=1
    while j < len(right):
        sorted_list.append(right[j])
        j+=1
    
    return sorted_list
            

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    left_  = merge_sort(left)
    right_ = merge_sort(right)
    
    return merge(left_,right_)


n,t = map(int,input().split())

unsorted_list = [int(x) for x in input().split()]

need_sorted_list = unsorted_list[:t]
rest_list = unsorted_list[t:]


sorted_list = merge_sort(need_sorted_list)

answer = sorted_list+rest_list

for i in answer:
    print(i,end=" ")
