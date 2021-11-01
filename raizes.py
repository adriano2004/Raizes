n = int(input('Digite um número: '))
q = n ** (1/2)   # Ou pow (n,(1/2))
c = n ** (1/3)   # Ou pow (n,(1/3))
qua = n ** (1/4) # Ou pow (n,(1/4))
qui = n ** (1/5) # Ou pow (n,(1/5))

print(' A raizes de {}:\n A raiz quadrada é {:.2f} \n A raiz cúbica é {:.2f} \n A raiz quarta é {:.2f} \n A raiz quinta é {:.2f}'.format(n,q,c,qua,qui))