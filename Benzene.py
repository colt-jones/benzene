import numpy as np
#Generates Hamiltonian matrix
def gen_ham(dim, eps, coup):
    ham=[]
    for i in range (dim):
        ham.append([])
        for j in range(dim):
            if i==j:
                ham[i].append(eps)
            elif j==i+1 or j==i-1: 
                ham[i].append(coup)
            elif (i==0 and j==dim-1) or (i==dim-1 and j==0):
                ham[i].append(coup)
            else: 
                ham[i].append(0.0)     
    np_ham = np.asarray(ham)
    return np_ham
#Enter parameters
dim = 6
eps = 0
coup = -2.7
#Generate Hamiltonian matrix
np_ham = gen_ham(dim, eps, coup)
print("Hamiltonian Matrix: ")
print(np_ham)
print()
#Eigenvalues
Eigenvalues = np.reshape(np.linalg.eigvals(np_ham), (1,dim))
print("Hamiltonian Eigenvalues: ")
print(Eigenvalues)
print()
#Eigenvectors
Eigenfunctions = np.linalg.eigh(np_ham)[1]
print("Hamiltonian Eigenvectors: ")
print(Eigenfunctions)
print()
#Eigenfunctions
print("Hamiltonian Eigenfunctions: ")
for i in range(Eigenfunctions.shape[1]):
    print(i+1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




