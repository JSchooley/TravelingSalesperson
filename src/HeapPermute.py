'''
Created on Oct 28, 2016

@author: Joshua
'''

def permute(letters, n):
    if n == 1:
        print "Write:", letters
    else:
        for i in range(n):
            permute(letters, n-1)
            if n%2 != 0:
                temp0 = letters[1]
                letters[1] = letters[n-1]
                letters[n-1] = temp0
            else:
                temp1 = letters[i]
                letters[i] = letters[n-1]
                letters[n-1] = temp1

if __name__ == "__main__":
    
    startingList = ['a', 'b', 'c']

    result = permute(startingList, len(startingList))