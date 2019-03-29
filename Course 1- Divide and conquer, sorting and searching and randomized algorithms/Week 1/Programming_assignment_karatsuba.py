def pad(x, pad_length):
    pad_str = ''
    while(len(pad_str)<pad_length):
        pad_str += '0'
    return pad_str+x

def equalize(x,y):
    if len(x)<len(y):
        x = pad(x,len(y)-len(x))
    elif len(y)<len(x):
        y = pad(y,len(x)-len(y))
    return x,y

def karatsuba(x,y):
    x , y = equalize(x,y)
    length = int(len(x))
    half_length = int((length/2))
    if length == 1:
        res = int(x)*int(y)
        return res
    
    else:
        if (length % 2) != 0:
            x = pad(x,1)
            y = pad(y,1)
            length += 1
            half_length = int(length/2)
        a = x[:half_length]
        b = x[half_length:]
        c = y[:half_length]
        d = y[half_length:]
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        e_1 = karatsuba( str( int(a)+int(b) ) , str( int(c)+int(d) ) )
        e_2 = e_1 - ac - bd
        ac *= int(pow(10,length))
        e_2 *= int(pow(10,half_length))
        res = ac + bd + e_2
        return res

x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'

karatsuba_val = karatsuba(x,y)
print(karatsuba_val)
