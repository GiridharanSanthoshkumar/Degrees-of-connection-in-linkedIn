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
def distance_between_two_users(user1,user2):
   
    visited=set()
    queue = deque()
    queue.append(user1)
    count=0
    while(len(queue)>0):
        for i in range(len(queue)):
            node=queue.popleft()
            print(node)
            if(node in visited):
                continue 
            if(node==user2):
                return count
            else:
                #add current user connections to the queue

                visited.add(node)
                for i in range(len(social_graph[node])):
                    queue.append(social_graph[node][i])
        count=count+1
    return -1


user1="Aravinth"
user2="Karthi"
result=distance_between_two_users(user1,user2)
if result!=-1:
    print(f"number of hops between {user1} and {user2}:{result}")
else:
    print("they are in different graphs")

    
    

        
            






    





    




