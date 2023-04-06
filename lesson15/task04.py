def count_iteration(size):
    count = 0

    while size !=0 :
        size //=2
        count+=1

    return count

print(count_iteration(1000000))