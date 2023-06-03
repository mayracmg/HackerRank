from itertools import product

def find_max(m, k_list):
    combinations = list(product(*k_list))
    max_total = 0
    
    for combination in combinations:
        total = sum(i**2 for i in combination) % m
        if (total > max_total):
            max_total = total
            
    return max_total

if __name__ == '__main__':
    parameters = input().split(' ')
    k, m = int(parameters[0]), int(parameters[1])
    k_list = []

    for _ in range(k):
        numbers = input().split(' ')
        n = int(numbers[0])

        i_list = [int(numbers[i]) for i in range(1, n + 1)]
        k_list.append(i_list)

    max_total = find_max(m, k_list)
    print(max_total)
