A = int(input('vvedite celoe 4islo A: '))
B = int(input('vvedite celoe 4islo B >= 4islu A: '))
if A > B: 
    print('4islo B dolzno byt bolwe ili ravna 4islu A')
else:
    count = [str(i) for i in range(A, B) if i % 2 == 0]
    print(' '.join(count))