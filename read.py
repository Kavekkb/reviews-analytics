data=[]
count=0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 ==0:
            print(len(data))

#print(len(data))

sum_len=0
for d in data:
    sum_len= sum_len + len(d)
    print(sum_len)

print('留言的平均長度:',sum_len/len(data))

new=[]

for d in data:
    if len(d) <100:
        new.append(d)

print('共有',len(new),'筆留言長度小於100')

print(new[0])
print(new[1])


good = []

for d in data:
    if 'good' in d:
        good.append(d)

#精簡寫法
#good=[d for d in data if 'good' in d]

bad =['bad' in d for d in data]

print('一共有',len(good),'留言提到good')
print(good[0])