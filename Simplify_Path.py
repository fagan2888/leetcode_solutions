## https://leetcode.com/problems/simplify-path/

## this one is pretty straightforward too -- just want to turn an absolute 
## path into a...simpler absolute path

## run time probably dominated by the directory loop (though in certain
## cases could be dominated by the '//' replacement), so complexity is 
## O(number of single slashes in path)

## results in 92nd percentile runtime and 21st percentile in memory

class Solution:
    def simplifyPath(self, path: str) -> str:

        ## replace any '//' with a single '/' 
        ## (two consecutive slashes are always redundant)
        while '//' in path:
            path = path.replace('//', '/')
        
        ## split into a list of directories to process
        dirs = path.split('/')[1:]

        output_directories = []
        for d in dirs:
            ## if we hit a '..', we pop the prevoius directory
            if d == '..':
                if not len(output_directories):
                    continue
                output_directories.pop()

            ## if we hit a single '.', we ignore it
            elif d == '.':
                continue

            ## otherwise, we step into the directory
            else:
                output_directories.append(d)

        ## then we join everything back together and make sure the start and end are correct
        out = '/' + '/'.join(output_directories)
        if out.endswith('/') and len(out) > 1:
            out = out[:-1]
        return out