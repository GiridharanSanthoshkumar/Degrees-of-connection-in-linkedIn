
from collections import deque 

social_graph= {
    'Giri': ['Sri', 'Thoufeeq', 'Bala'],
    'Sri': ['Giri', 'Mega', 'Karthi'],
    'Thoufeeq': ['Giri', 'Iyap', 'Aravinth'],
    'Bala': ['Giri', 'Vijay', 'Aadhi'],
    'Mega': ['Sri'],
    'Karthi': ['Sri', 'Vijay'],
    'Iyap': ['Thoufeeq'],
    'Aravinth': ['Thoufeeq', 'Aadhi'],
    'Vijay': ['Bala', 'Karthi', 'Aadhi'],
    'Aadhi': ['Bala', 'Aravinth', 'Vijay']
}

          
def bidir_search(source,target):
    if source == target:
        return 0  
    visited1=set()
    visited2=set()
    queue1=deque()
    queue2=deque()
    
    queue1.append(source)
    queue2.append(target)
    levelcount1=0
    levelcount2=0

    while len(queue1)>0 or len(queue2)>0:

        
        for i in range(len(queue1)):
            cur_node=queue1.popleft()

            if(cur_node in visited2):
                    return  (levelcount1 + levelcount2)
            if(cur_node not in visited1):
                    visited1.add(cur_node)
                    for node in social_graph[cur_node]:
                        if(node not in visited1):
                            queue1.append(node)
        
        levelcount1+=1
        
        for i in range(len(queue2)):
            cur_node=queue2.popleft()
            if(cur_node in visited1):
                return levelcount1+levelcount2
            if(cur_node not in visited2):
                    visited2.add(cur_node) 
                    for node in social_graph[cur_node]:
                        if(node not in visited2):  
                            queue2.append(node)
        
        levelcount2+=1
    

    return -1
    
 
test_cases = [
    ("Giri", "Sri"),  # 1 hop
    ("Sri", "Mega"),  # 1 hop
    ("Bala", "Aadhi"),  # 1 hop
    ("Giri", "Mega"),  # 2 hops
    ("Bala", "Karthi"),  # 2 hops
    ("Aravinth", "Giri"),  # 2 hops
    ("Iyap", "Mega"),  # 3 hops
    ("Bala", "Iyap"),  # 3 hops
    ("Karthi", "Aravinth"),  # 3 hops
    ("Mega", "Iyap"),  # 4 hops
    ("Aadhi", "Mega"),  # 4 hops
    ("Sri", "Sri"),  # 0 hops
    ("Thoufeeq", "Thoufeeq")  # 0 hops
]

for user1, user2 in test_cases:
    no_of_hops = bidir_search(user1, user2)
    if(no_of_hops==-1):
         print("They are not in the same graph")
    print(f"No of hops to reach from {user1} to {user2}: {no_of_hops-1}")
  
                    


            

    

