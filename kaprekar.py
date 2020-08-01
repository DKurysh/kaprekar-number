def numerics(n):        #convert 4-digit number in a list of 4 digits
    s = str(n)
    l = len(s)
    if l < 4:
        s = '0'*(4-l) + s
    return [int(i) for i in s]


def kaprekar_step(l):
    
    def union(l):
        return int(''.join(map(str, l)))
    
    l = sorted(l)
    return union(l[::-1]) - union(l) 

def input_check(n):
    if n <= 1000:
        print("\nError! Number should be >= 1000\n")
        return False
    if n >= 10000:
        print("\nError! Number should be < 10000\n")
        return False
    if len(set(numerics(n))) == 1:
        print("\nError! Enter is {}, but it should be at least 2 different figures\n".format(n))
        return False
    return True

def kaprekar_loop(initial_n):
    n = initial_n
    i = 0
    while n != 6174:
        L = numerics(n)
        n = kaprekar_step(L)
        i += 1
        print('step {}: {}'.format(i, n))
    print ('{} converges to Kaprekar constant in {} steps'.format(initial_n, i))
        
if __name__ == '__main__':
    done = False
    while not done:
        n = int(input('Enter 4-digit number (> 1000): '))
        if input_check(n):
            kaprekar_loop(n)
            done = True
