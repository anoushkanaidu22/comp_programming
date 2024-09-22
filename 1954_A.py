t = (int)(input())

for _ in range(t):
	vals = input().split(" ")
	n = (int)(vals[0])
	m = (int)(vals[1])
	k = (int)(vals[2])

	if ((m > k) and (n <= m)):
		print("yes")
	elif ((n-m) >k):
		print("yes")
	else:
		print("no")
