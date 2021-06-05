import random
import time
import sys

def paractice():
	"""幼儿园加法练习"""
	i, r, w = [1, 1, 1]
	while True:
		time.sleep(0.1)
		first = random.randint(0, 100)
		second = random.randint(0, 100)
		if first < 3 or second < 5:
			continue
		try:
			op = random.choice('-+')
			if op == '-':
				if first < second:
					continue
			answer = int(input(f"【{i}】请输入第{i}题{first}{op}{second}=").strip())
		except ValueError:
			continue
		i += 1
		if op == '+':
			right = first + second
		else:
			right = first - second
		if right == answer:
			print(f"【√】恭喜您，回答正确【{r}】题")
			r += 1
		else:
			print(f"【×】很遗憾您答错误了【{w}】题")
			w += 1
		if i == 60:
			print("时间到。。。")
			print(f'一共做对{r}道题!')
			sys.exit(0)
		

paractice()

