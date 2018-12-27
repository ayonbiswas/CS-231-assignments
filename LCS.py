


def LCS(a,b):
    


    x = len(a)
    y = len(b)
    lcs_matrix = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    

    for i in range(x):
            for j in range(y):
                if a[i] == b[j]:
                    lcs_matrix[i+1][j+1] = lcs_matrix[i][j] + 1
                else:
                    lcs_matrix[i+1][j+1] = max(lcs_matrix[i+1][j], lcs_matrix[i][j+1])
    i= len(a)
    j = len(b)

    lst = ""
    
 
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lst = a[i-1] + lst
            i -= 1
            j -= 1
        elif lcs_matrix[i][j] == lcs_matrix[i][j-1]:
            j -= 1
        
        elif lcs_matrix[i][j] ==lcs_matrix[i-1][j]:
            i -= 1
    print  lst

    
a = input("first sequence : ")
b = input("second sequence : ")

LCS(a,b)




    
