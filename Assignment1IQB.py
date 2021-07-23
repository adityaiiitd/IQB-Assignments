import math


def align(a, b):
    if a == b:
        return match
    else:
        return mismatch


mystring1 = ""
mystring2 = ""

match = 2
mismatch = -1
gap = -1


def printmat(mat):
    for i in mat:
        for j in i:
            if (j < 0):
                print(str(j), end=' ')
            else:
                print(str(j) + " ", end=' ')
        print()
    print()


def printHelper(a, b):
    a = a[::-1]
    b = b[::-1]
    val = 0
    for i in range(len(a)):
        print(a[i], end=' ')
    print()
    for i in range(len(a)):
        if (a[i] == b[i]):
            print("|", end=' ')
            val = val + match
        elif a[i]=='_' or b[i]=='_':
            print(" ", end=' ')
            val = val + gap
        else:
            print(" ", end=' ')
            val = val + mismatch
    print()
    for i in range(len(b)):
        print(b[i], end=' ')
    print()
    print("Score = " + str(val))
    print()


# recursive function to find global alignment
def findOptAlign(mat, startx, starty, endx, endy, store, mystring1, mystring2):
    if endx < 0 or endy < 0:
        return 0
    if startx == endx and starty == endy:
        print()
        printHelper(mystring1, mystring2)
        print()
        return 1
    else:
        if mat[endx][endy] == mat[endx - 1][endy - 1] + match and b[endx - 1] == a[endy - 1] and endx > 0 and endy > 0:
            store.append("match case")
            findOptAlign(mat, startx, starty, endx - 1, endy - 1, store, mystring1 + a[endy - 1],
                         mystring2 + b[endx - 1])
        if mat[endx][endy] == mat[endx - 1][endy] + gap and endx > 0:
            store.append("gap case1")
            findOptAlign(mat, startx, starty, endx - 1, endy, store, mystring1 + '_', mystring2 + b[endx - 1])
        if mat[endx][endy] == mat[endx][endy - 1] + gap and endy > 0:
            store.append("gap case2")
            findOptAlign(mat, startx, starty, endx, endy - 1, store, mystring1 + a[endy - 1], mystring2 + '_')
        if mat[endx][endy] == mat[endx - 1][endy - 1] + mismatch and endx > 0 and endy > 0:
            store.append("mismatch case")
            findOptAlign(mat, startx, starty, endx - 1, endy - 1, store, mystring1 + a[endy - 1],
                         mystring2 + b[endx - 1])


a = "ATCAGAGTA"
b = "TTCAGTA"

m = len(a) + 1
n = len(b) + 1

# code for making empty global alignment matrix
globalmat = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(0)
    globalmat.append(col)

# filling 0th row and column with gap penalty
for i in range(1, n):
    globalmat[i][0] = -i

for i in range(1, m):
    globalmat[0][i] = -i

# code for making global alignment matrix where a and b are the strings
for i in range(1, n):
    for j in range(1, m):
        myalign = align(a[j - 1], b[i - 1])
        globalmat[i][j] = max(globalmat[i - 1][j - 1] + myalign, globalmat[i - 1][j] + gap, globalmat[i][j - 1] + gap)

# making empty local alignment matrix
localmat = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(0)
    localmat.append(col)

# making the local alignment matrix here
for i in range(1, n):
    for j in range(1, m):
        myalign = align(a[j - 1], b[i - 1])
        localmat[i][j] = max(localmat[i - 1][j - 1] + myalign, localmat[i - 1][j] + gap, localmat[i][j - 1] + gap, 0)

# printMatrix(localmat, n)

store = []

print("1->a Here is Global alignment matrix")
printmat(globalmat)
print("1->b Yes there is a possibility of aligning the sequence in multiple ways and obtain max score and opt soln ")
print("This is because of multiple paths in our matrix so our sequence can be aligned in different ways and still "
      "have max score")
print("1->c Here Possible global alignments, after here there is a function call")
findOptAlign(globalmat, 0, 0, n - 1, m - 1, store, mystring1, mystring2)
print("2->a Local alignment matrix, was already computed earlier in code, here I print it")
printmat(localmat)


def findMaxElement(mat, n, m):
    max = 0
    a = 0
    b = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] > max:
                max = mat[i][j]
                a = i
                b = j
    return a, b


def findOptLocalAlign(mat, endx, endy, mystring1, mystring2):
    if endx < 0 or endy < 0:
        return 0
    if mat[endx][endy] == 0:
        print()
        printHelper(mystring1, mystring2)
        print()
        return 1
    else:
        if mat[endx][endy] == mat[endx - 1][endy - 1] + match and b[endx - 1] == a[endy - 1] and endx > 0 and endy > 0:
            findOptLocalAlign(mat, endx - 1, endy - 1, mystring1 + a[endy - 1],
                              mystring2 + b[endx - 1])
        elif mat[endx][endy] == mat[endx - 1][endy] + gap and endx > 0:
            findOptLocalAlign(mat, endx - 1, endy, mystring1 + '_', mystring2 + b[endx - 1])
        elif mat[endx][endy] == mat[endx][endy - 1] + gap and endy > 0:
            findOptLocalAlign(mat, endx, endy - 1, mystring1 + a[endy - 1], mystring2 + '_')
        elif mat[endx][endy] == mat[endx - 1][endy - 1] + mismatch and endx > 0 and endy > 0:
            findOptLocalAlign(mat, endx - 1, endy - 1, mystring1 + a[endy - 1],
                              mystring2 + b[endx - 1])


print("2->b Here is a local alignment with its score, there is a function call after this line")
# first find the end point store it in p,q then find opt alignment, then find alignment using the function
p, q = findMaxElement(localmat, n, m)
findOptLocalAlign(localmat, p, q, "", "")

print("3-> The difference are as follows:")
print("1) In global alignment matrix the first row and first column is initialized with gap penalties whereas in "
      "local alignment \n  they assigned to zero. ")
print("2) For any element M(i,j) in local alignment it could never be negative so in the DP recurrence \n will "
      "now become "
      "max(M(i-i,j-1)+sigma(i,j) , M(i-1,j)+gap penalty , M(i,j-1)+gap penalty, cuz it can never be negative as in "
      "case of global alignment")
print("3)In the case of local alignment you first find the max entry in the matrix and then you align the sequences "
      "using backtracking\n "
      "from that particular point whereas in global sequence alignment you start from the last cell in the matrix\n"
      "4)Also you stop after you have encountered the zero in the case of local alignment whereas you don't in the "
      "case "
      "of global\n ")

print("4->Lets modify match, mismatch and gap")

match = 2
mismatch = -1
gap = -2

# code for making empty global alignment matrix
globalmat = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(0)
    globalmat.append(col)

# filling 0th row and column with gap penalty
for i in range(1, n):
    globalmat[i][0] = -i+gap+1

for i in range(1, m):
    globalmat[0][i] = -i+gap+1

# code for making global alignment matrix where a and b are the strings
for i in range(1, n):
    for j in range(1, m):
        myalign = align(a[j - 1], b[i - 1])
        globalmat[i][j] = max(globalmat[i - 1][j - 1] + myalign, globalmat[i - 1][j] + gap, globalmat[i][j - 1] + gap)

print("new global matrix is created and printed now")
printmat(globalmat)
print("here are the alignment sequences")
findOptAlign(globalmat, 0, 0, n - 1, m - 1, store, mystring1, mystring2)

# making empty local alignment matrix
localmat = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(0)
    localmat.append(col)

# making the local alignment matrix here
for i in range(1, n):
    for j in range(1, m):
        myalign = align(a[j - 1], b[i - 1])
        localmat[i][j] = max(localmat[i - 1][j - 1] + myalign, localmat[i - 1][j] + gap, localmat[i][j - 1] + gap, 0)

print("new local matrix is created and printed now")
printmat(localmat)
print("printing the alignment here now")
p, q = findMaxElement(localmat, n, m)
findOptLocalAlign(localmat, p, q, "", "")

print("Here are the observations in Global with modified gap,mismatch and match: \n"
      "the matrix which was made dynamically has changed, score has changed but the alignment sequences have remained "
      "the same \n"
      "Whereas in local alignment matrix aswell as the score and the alignment sequences have changed.")