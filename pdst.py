import numpy as np

def getHamming(string1, string2):
    hd = 0
    assert len(string1) == len(string2)
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            hd += 1
    return hd/len(string1)


def getDistMatrix(fasta):
    rows = len(fasta)
    mat = np.empty((rows, rows))
    for i in range(rows):
        for j in range(rows):
            mat[i][j] = getHamming(fasta[list(fasta.keys())[i]], fasta[list(fasta.keys())[j]])
    return mat    

def getFastaSeqs(file):
    fasta = {}
    seq = ''

    with open(file, 'r') as f:
        for line in f:

            line = line.strip()
            if line[0] == '>':
                name = line
                fasta[name] = seq
                seq = ''
            else:
                seq += line

            if name in fasta:
                fasta[name] = seq
    return fasta


if __name__ == '__main__':

    file = input('Insert file path:').rstrip()
    fasta = getFastaSeqs(file)
    print(getDistMatrix(fasta))