import time
import random 
import statistics
import hashlib
import bcrypt

file_name = '10k-most-common.txt'
with open(file_name, 'r') as f:
    lines = f.readlines()
lis = []
for w in lines:
    word = w.strip()
    lis.append(word)

sample_sha1 = []
sample_md5 = []
sample_bcrypt = []
sample_list = random.sample(lis, 100)
salt = bcrypt.gensalt()

for word in sample_list:
    start = time.perf_counter()
    hash_val = hashlib.sha1(word.encode('utf-8')).hexdigest()
    end = time.perf_counter()
    sample_sha1.append(end-start)

    start = time.perf_counter()
    hash_val = hashlib.md5(word.encode('utf-8')).hexdigest()
    end = time.perf_counter()
    sample_md5.append(end-start)

    start = time.perf_counter()
    hash_val = bcrypt.hashpw(word.encode('utf-8'),salt).hex()
    end = time.perf_counter()
    sample_bcrypt.append(end-start)

q1, q2, q3 = statistics.quantiles(sample_sha1, n=4)
iqr = q3-q1
filter_time = [t for t in sample_sha1 if t >= q1-1.5*iqr and t <= q3+1.5*iqr]
print(round(sum(filter_time) / len(filter_time), 6))

q1, q2, q3 = statistics.quantiles(sample_md5, n=4)
iqr = q3-q1
filter_time = [t for t in sample_md5 if t >= q1-1.5*iqr and t <= q3+1.5*iqr]
print(round(sum(filter_time) / len(filter_time), 6))

q1, q2, q3 = statistics.quantiles(sample_bcrypt,n=4)
iqr = q3-q1
filter_time = [t for t in sample_bcrypt if t >= q1-1.5*iqr and t <= q3 + 1.5*iqr]
print(round(sum(filter_time) / len(filter_time), 6))




