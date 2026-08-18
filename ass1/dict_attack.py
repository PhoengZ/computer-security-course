import hashlib

file_name = '10k-most-common.txt'
target = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"

num_to_char = {
    'o':['0','O','o'],
    '0':['o','0'],
    '1':['i','I','1'],
    'i':['1','I','i'],
    'I':['1','i','I']
}

def recursive(word, start, stop):
    if start == stop:
        result_str = "".join(word)
        hash_val = hashlib.sha1(result_str.encode('utf-8')).hexdigest()
        if hash_val == target:
            return result_str
        else:
            # print(f"{result_str}:   {hash_val}")
            return ""
    org = word[start]
    low = org.lower()
    l = []
    if low in num_to_char:
        l = num_to_char[low]
    elif low.isalpha():
        l = [org.lower(), org.upper()]
    else:
        l = [org.lower()]
    for c in l:
        word[start] = c
        result = recursive(word, start+1, stop)
        if result != "":
            return result
    word[start] = org
    return ""


found = False
with open(file_name, 'r') as f:
    lines = f.readlines()
for w in lines:
    word = w.strip()
    end = len(word)
    word = list(word)
    result = recursive(word,0,end)
    if result != "":
        print(f"found: {result}")
        found=True
        break
if not found:
    print("Not found")
