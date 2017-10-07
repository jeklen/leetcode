# 按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
while True:
	try:
		num = int(input())
	except:
		break
	order = int(input())
	name = []
	grade = []
	for i in range(num):
		tmp = list(input().split())
		name.append(tmp[0])
		grade.append(tmp[1])
	for i in range(1, len(grade)):
		tmp_value = grade[i]
		tmp_name = name[i]
		j = i - 1
		while j >= 0 and grade[j] > tmp_value:
			grade[j+1] = grade[j]
			name[j+1] = name[j]
			j = j - 1
		grade[j+1] = tmp_value
		name[j+1] = tmp_name
	if order == 1:
		# print(len(grade))
		for i in range(len(grade)):
			print(name[i], grade[i], sep=' ', end=' ')
			print('ok', end=' ')
	if order == 0:
		for i in range(len(grade)-1, -1, -1):
			print(name[i], grade[i], sep=' ', end=' ')
			print('ok', end = ' ')