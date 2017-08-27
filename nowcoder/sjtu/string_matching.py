line = input()
while line:
	line_list = line.split()
	text = line_list[0]
	pattern = line_list[1]
	count = 0
	len_t = len(text)
	len_p = len(pattern)
	for i in range(len_t - len_p + 1):
		flag = True
		for j in range(len_p):
			if text[i+j] != pattern[j]:
				flag = False
				break
		if flag:
			count = count + 1
	print(count)
	line = input()