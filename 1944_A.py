t = (int)(input())

for _ in range(t):
	nums = [int(x) for x in input().split()]
	n = nums[0]
	k = nums[1]
	
	if ((n-1) > k):
		print(n)
	else:
		print(1)
		
