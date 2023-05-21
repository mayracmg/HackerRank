def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    ocurrences = 0

    for i in range(n - m + 1):
        if (sub_string == string[i: i + m]):
            ocurrences += 1
    return ocurrences
