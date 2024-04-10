t = int(input())

for _ in range(t):
	length = int(input())

	num_arr = [int(x) for x in input().split()]
	num_arr.sort()
	
	if (length % 2 == 1):
		loop_num = length // 2
		median = num_arr[loop_num]
	else:
		loop_num = length // 2 - 1
		median = num_arr[loop_num]

	count = 0
	for i in range(loop_num, length):
		if(num_arr[i] == median):
			count += 1
	
	print(count)

	

	
	

