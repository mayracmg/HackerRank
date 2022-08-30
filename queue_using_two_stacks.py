n = int(input())
queue = []

for i in range(n):
    input_query = input()
    query_parts = input_query.split(' ')
    
    if (query_parts[0] == "1"):
        queue.append(query_parts[1])
    elif (query_parts[0] == "2"):
        queue.pop(0)
    else:
        print(queue[0])
