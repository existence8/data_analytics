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

#隨機抽選列印(抽選復習)
import random
pick= random.randint(0, 1000000)
print(data[pick])

#計算平均留言長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #也可以寫成 sum_len +=len(d)

print('留言的平均長度為:', sum_len/len(data))

#篩選功能(一)：計算小於100字的留言數
short = []
for d in data:
	if len(d) < 100:
		short.append(d)
print('小於100字的留言共有', len(short), '筆')
print('例如', short[0])

#篩選功能(二): 找出含有bad的留言
bad = []
for d in data:
	if 'bad' in d:
		bad.append(d)
print('含有bad的留言一共有', len(bad), '筆')
print('例如', bad[0])
