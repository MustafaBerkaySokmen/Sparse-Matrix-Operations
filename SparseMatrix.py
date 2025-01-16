import random
import math

################################################################ 
### Below are the functions you need to implement in the HW. ###
### Feel free to create your own helper functions.           ###
################################################################ 
    
def dense_to_sparse(matrix):
    sp_matrix = {}
    N=len(matrix)
    M=len(matrix[1])
    sp_matrix[-1]=[N,M]
    for i in range(N):
        for j in range(M):
            if matrix[i][j]!= 0:
                sp_matrix[(i,j)]= matrix[i][j]
            
    return sp_matrix
    
    

def sparse_transpose(sp_matrix):
    
    sp_transpose={}
    for key in sp_matrix.keys():
          if key!=-1:
               sp_transpose[(key[1],key[0])]=sp_matrix[(key[0],key[1])]
            
            
        
        
    
    return sp_transpose    


def sparse_add(sp_matrix1, sp_matrix2):
    
    empty=[[0 for x in range(sp_matrix2[-1][1])] for y in range(sp_matrix1[-1][0])]
    
    
    sp_res= dense_to_sparse(empty)
     
    for i in sp_matrix1.keys():
        for j in sp_matrix2.keys():
            if i==j and not i==-1:
                sp_res[i]= sp_matrix1[i]+sp_matrix2[j]
            if i not in sp_matrix2.keys() and not i==-1:
                sp_res[i]= sp_matrix1[i] 
            if j not in sp_matrix1.keys() and not j==-1:
                sp_res[j]= sp_matrix2[j]
            if not sp_matrix1[-1] ==sp_matrix2[-1]:
                return -1
    return sp_res           
                
            
            
        
        

def sparse_multiply(sp_matrix1, sp_matrix2):
    
    
    sp_matrix_res = {}
    sp_matrix_res[-1]=[sp_matrix1[-1][0],sp_matrix2[-1][0]]
    
    if sp_matrix1[-1][1] != sp_matrix2[-1][0]:
        return -1
    
    elif sp_matrix1[-1][1] == sp_matrix2[-1][0]:
        
        for i in range(sp_matrix1[-1][0]):
            for j in range(sp_matrix1[-1][1]):
                if (i,j) not in sp_matrix1.keys():
                    sp_matrix1[(i,j)]=0
                    
        for i in range(sp_matrix2[-1][0]):
            for j in range(sp_matrix2[-1][1]):
                if (i,j) not in sp_matrix2.keys():
                    sp_matrix2[(i,j)]=0
                    
        for i in range(sp_matrix1[-1][0]):
            for j in range(sp_matrix2[-1][1]):
                summ=0
                for k in range(sp_matrix1[-1][1]):
                    summ+=sp_matrix1[(i,k)]*sp_matrix2[(k,j)]

                sp_matrix_res[(i,j)]=summ
    return sp_matrix_res


################################################################ 
### Below are some functions we are providing you to help    ###
### you test your solutions. They won't be graded.           ###
################################################################ 

def generate_random_sparse_matrix(nrow, ncol, sparsity=0.6):
    """
    This function generates a random matrix as a list of lists
    with a given sparsity.
    """    
    row = [0]*ncol
    res=[]
    for i in range(nrow):
        res.append(row[:])

    nr = int((1.-sparsity)*nrow*ncol)
    pos = random.sample(range(nrow*ncol), nr)
    for ind in pos:
        n_ind = math.floor(ind/ncol)
        m_ind = ind-n_ind*ncol
        res[n_ind][m_ind]=random.randint(1,20)
    return res


def main():
    """ 
    This function contains some test cases for you to test your solutions.
    We recommend that you create additional test cases for yourself. 
    """
    ll_sp_m1 = generate_random_sparse_matrix(3, 5)
    ll_sp_m2 = generate_random_sparse_matrix(5, 2)
    ll_sp_m3 = generate_random_sparse_matrix(3, 5)
    print(ll_sp_m1)
    print(ll_sp_m2)
    sp_m1 = dense_to_sparse(ll_sp_m1)
    sp_m2 = dense_to_sparse(ll_sp_m2)
    sp_m3 = dense_to_sparse(ll_sp_m3)
    print(sp_m1)
    print(sp_m2)
    sp_m1_transpose = sparse_transpose(sp_m1)
    sp_m2_transpose = sparse_transpose(sp_m2)
    print(sp_m1_transpose)
    print(sp_m2_transpose)
    
    add1 = sparse_add(sp_m1, sp_m3)
    add2 = sparse_add(sp_m1, sp_m2)
    print(add1)
    print(add2)
    mult1 = sparse_multiply(sp_m1, sp_m2)
    mult2 = sparse_multiply(sp_m1, sp_m3)
    print(mult1)
    print(mult2)
    

main()