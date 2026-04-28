def count_frequency(string):
    freq = {}
    for ch in string:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch] = 1
    return freq            
    