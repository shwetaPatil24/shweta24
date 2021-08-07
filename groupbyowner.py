files_list = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
       
    }  
from collections import defaultdict
   
d = defaultdict(list)

def group_by_owners(files_list):
    for k,v in files_list.items():
        d[v].append(k)
    return dict(d.items())

 
print(group_by_owners(files_list))
