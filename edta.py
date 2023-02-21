from edit import getLevenshteinDistance
from pdst import getFastaSeqs

def getMin(a,b,c):
    minimum = min([a,b,c])
    if a == minimum:
        return('insert')
    elif b == minimum:
        return('replace')
    elif c == minimum:
        return('delete')

def getString(seq1, seq2):

    if len(seq1) < len(seq2):
        seq = seq1
        seq1 = seq2
        seq2 = seq
    print(seq1, seq2)
    
    new_seq1 = ''
    new_seq2 = ''
   
    dm  = getLevenshteinDistance(seq1, seq2)[0]
    # print(dm)

    i,j = len(seq1), len(seq2)
    new_seq1, new_seq2 = '',''

    while i>0 and j>0:

        trans = getMin(dm[i-1][j], dm[i-1][j-1], dm[i][j-1])
    
        if trans == 'replace':
            
            new_seq1 = seq1[i-1] + new_seq1
            new_seq2 = seq2[j-1] + new_seq2
            i -= 1
            j -= 1

        elif trans == 'insert':
            new_seq1 = seq1[i-1] + new_seq1 
            new_seq2 = '-' + new_seq2
            i -= 1
            
        elif trans == 'delete':
            new_seq1 = '-' + new_seq1
            new_seq2 = seq2[j-1] + new_seq2
            j -= 1

    return new_seq1, new_seq2
                        
 

if __name__ == '__main__':

    # file = input('Insert file path:').rstrip()
    # seq1, seq2 = getFastaSeqs(file).items()
    

    seq1 = 'pretty'
    seq2 = 'prttein'

    print(getLevenshteinDistance(seq1, seq2)[1])
    print(getString(seq1, seq2))



