## https://leetcode.com/problems/compare-version-numbers

## not totally sure why this is a medium to be hoenst; it's 
## not that hard.  just split into a list of ints, pad out
## to be the same length, then iterate over those two lists.

## comes in at 98th percentile for runtime and between 68th 
## and 94th percentile for memory.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ## turn the strings into a list of integers 
        ## (automatically takes care of ignoring leading zeros)
        version1 = [int(k) for k in version1.split('.')]
        version2 = [int(k) for k in version2.split('.')]       
        
        ## pad out the shorter string with .0 (which is implied)
        length = max(len(version1), len(version2))
        while len(version1) < length:
            version1.append(0)
        while len(version2) < length:
            version2.append(0)
            
        
        ## now copare equal subversion levels until i find one that's different
        for index in range(min(len(version1), len(version2))):
            if version1[index] > version2[index]:
                return 1
            elif version1[index] < version2[index]:
                return -1
        
        ## if we get here, then all were equal
        return 0