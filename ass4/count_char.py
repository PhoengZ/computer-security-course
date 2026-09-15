TARGET="PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."

d = dict()

for t in TARGET:
    if t == " ":continue
    if t not in d.keys():
        d[t] = 1
    else:
        d[t]+=1
sol = [(v,k) for k,v in d.items()]
sol.sort(reverse=True)
print(sol)
