import math

def decimal_chromosome(bin_chromosome):
    dec_chromosome = []
    dec = 0
    for i in range(50):
        x = i%10
        dec = dec + bin_chromosome[i]*math.pow(2, 9 - x)
        
        if x == 9:
            dec_chromosome.append(dec)
            dec = 0
    return dec_chromosome

def is_valid(member): 
    dec_sum  = 0
    dec_member = decimal_chromosome(member)
    for item in dec_member:
        dec_sum = dec_sum + item

    return dec_sum == 1023

def cover():
     
    member = [0 for i in range(50)]
    
    while(not is_valid(member)):
        member 
    
    return member
        
        