# do BFS from the source node and target node

#two queue and two visited list

#initially ,put the start node to the visited1 and expand its neighbors into the queue1,do the same for 
#target as well.


#do a level traversal for source and do a level traversal for target node

#at the time of visiting a node(pop out from the queue),we ll expand
#to expand->the current node should not be in visited list(to avoid the cycle in the graph)

#check the current node already in the opposite visited list,if so then here is the intersection and stop

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
                    return levelcount1+levelcount2
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
    
    
    
user1="Aravinth"
user2="Karthi"
no_of_hops=bidir_search(user1,user2)    
if(no_of_hops==-1):
    print("Two users are not having any connections,they are in the different graphs")
else:
    print(f"No of hops to reach the {user1} to {user2} is: {no_of_hops-1}")

        
                    


            

    

