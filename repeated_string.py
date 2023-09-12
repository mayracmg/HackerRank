def repeatedString(s, n):
    len_s = len(s)
    times_to_repeat = n // len_s
    remaining_chars = n % len_s
    
    frequency  = s.count('a') * times_to_repeat
    frequency += s[:remaining_chars].count('a')
    
    return frequency 
