def candy(a,n):
    max = 0
    F = [0] * len(a)
    
    for i in range(1,len(a)+1):
        for j in range(2,len(a)+1):
            sum = i
            k=j
            F[k-1] = a[i-1]
            while sum < n:
                sum += k
                F[k-1] += a[k-1]
                k += 1
            
            if sum == n and F[k-1] > max:
                max = F[k-1]
            
    print("maximum obtainable value: ", max)
    
candy([1, 5, 8, 9, 10, 17, 17, 20],8)