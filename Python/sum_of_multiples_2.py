def sum_mul(n,m):
    
    if n <= 0 or m <= 0:
        return 'INVALID'
        
    mul = 0
    sumMuls = 0
    
    while mul < m:
        mul = mul + n
        if mul >= m:
            break
            
        sumMuls = sumMuls + mul
        
    return sumMuls