def no_boring_zeros(n):
    
    i = 1
    
    while i < 10:
        
        counter = 10
        i = i + 1

        if counter <= 10000:

            if n % counter == 0:

                n = n // counter


            if n % counter != 0:            
                return n

            counter = counter * 10
            
    if n == 0:
        return 0 
    
    if n % 10 != 0:
        return "Not boring"
            