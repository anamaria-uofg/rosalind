from pdst import getFastaSeqs
import numpy as np

# Levenshtein Matrix
# ||replace ||  delete  ||   
# ||insert  ||  dm[i][j]||   


def getLevenshteinDistance(s,t):
    #  calculates the number of operations (insert/delete/replace) needed to convert one string (s) to another (t)
    rows = len(s)
    columns = len(t)
    dm = np.empty((rows+1, columns+1))


    # base case for columns = 0 (deletions)
    for r in range(rows+1):
        dm[r][0] = r
    # base case for rows = 0 (insertions)
    for c in range(columns+1):
        dm[0][c] = c
    # transitions
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if s[i-1] == t[j-1]:
                dm[i][j] = dm[i-1][j-1]
                
            else:
                dm[i][j] = 1 + np.min([dm[i-1][j], dm[i-1][j-1], dm[i][j-1]])

   
    return dm, dm[rows][columns]
                


if __name__=='__main__':
    file = input('Insert file path:').rstrip()
    fasta  = getFastaSeqs('rosalind_edit_sample.txt')
    fasta_s = fasta[list(fasta.keys())[0]]
    fasta_t = fasta[list(fasta.keys())[1]]


    print(getLevenshteinDistance(fasta_s, fasta_t))