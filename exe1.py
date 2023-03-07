#!/usr/bin/python3

def pesquisarFibonacci(n):
    fn1 = 0
    fn2 = 1
    aux = 0
    for i in range(n):
        aux = fn1
        fn1 += fn2
        fn2 = aux 
    print(fn1)


    


            

