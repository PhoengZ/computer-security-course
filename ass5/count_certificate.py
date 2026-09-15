with open("ca-certificates.crt", "r") as f:
    lines = f.readlines()

count = 0

for line in lines:
    if "END CERTIFICATE" in line:
        count+=1
print(count)