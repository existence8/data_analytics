#留言資料分析練習
data= []
count=0
with open ('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 10000 == 0:
			print(count)
	print('留言數一共', len(data), '筆')

import random
pick= random.randint(0, 1000000)
print(data[pick])

#計算平均留言長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #也可以寫成 sum_len +=len(d)

print('留言的平均長度為:', sum_len/len(data))
