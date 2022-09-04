Q = int(input())
S = ""
q_status = []

for _ in range(Q):
    current_operation = input()
    current_operation = current_operation.split(" ")
    operation_type = current_operation[0]
    
    if (operation_type == "1"):
        q_status.append(S)
        text_to_add = current_operation[1]
        S += text_to_add
    elif (operation_type == "2"):
        q_status.append(S)
        k = int(current_operation[1])
        S = S[: -k]
    elif (operation_type == "3"):
        k = int(current_operation[1]) - 1
        text_to_print = S[k]
        print(text_to_print)
    else:
        previous_status = q_status.pop()
        S = previous_status
