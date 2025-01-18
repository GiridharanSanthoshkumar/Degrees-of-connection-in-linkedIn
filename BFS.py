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
            visited.add(node)
            
            if(node==user2):
                return count
            else:
                #add current user connections to the queue
                for i in range(len(social_graph[node])):
                    queue.append(social_graph[node][i])
        count=count+1
    return -1


user1="Thoufeeq"
user2="Mega"
result=distance_between_two_users(user1,user2)
if result!=-1:
    print(f"number of hops between {user1} and {user2}:{result}")
else:
    print("they are in different graphs")


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
    no_of_hops = distance_between_two_users(user1, user2)
    if(no_of_hops==-1):
         print("They are not in the same graph")
         continue
    print(f"No of hops to reach from {user1} to {user2}: {no_of_hops}")
    
    

        
            






    





    




