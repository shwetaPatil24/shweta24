class Path:
    def __init__(self, path):
        self.new_path = path
        new=path[:-1]
    
    def cd(self, second_path):
        i=0;
        second_pathList=second_path.split('/')
        pathLength=len(second_pathList)
        pathList=self.new_path.split('/')
        while(i<pathLength):
            j=len(pathList)-1
            if second_pathList[i]=='..':
                #parent directory
                pathList.pop(j)
            else:
                pathList.append(second_pathList[i])
            i=i+1
        self.new_path="/".join(pathList)

        
path = Path('/a/b/c/d')
path.cd('../x')

print(path.new_path)#/a/b/c/x
