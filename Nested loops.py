

for i in range(2,10):
    prime=True
    print('-----------------------------------------------------')
    print('Finding out if',i,'is prime')
    for j in range(2,i):
        print('Checking divisibility with', j)
        if i%j==0:
            prime=False
            print('...remainder is 0,break loop.',i,' is not prime.')
            break
    if prime:
        print(i,"is a prime number.")
    #input()
