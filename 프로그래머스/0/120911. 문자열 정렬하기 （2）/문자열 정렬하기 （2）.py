def solution(my_string):
    my_string = my_string.lower()
    li = []
    
    for i in my_string:
        li.append(i)
    
    li.sort()
    
    result = ''
    
    for i in li:
        result += i
        
    return result
    