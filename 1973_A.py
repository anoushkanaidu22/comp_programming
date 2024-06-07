t = (int)(input())

for _ in range(t):

	scores = [int(x) for x in input().split()]
	p1 = scores[0]
	p2 = scores[1]
	p3 = scores[2]
	
	#the total score can only inrease by 2 at a time
	if ((p1 + p2 + p3) % 2 == 1):
		print(-1)

	elif ((p1 + p2) >= p3):
		x = (p1 + p2) - p3
		y = (x // 2) + p3
		print(y)
	else:
		print(p1 + p2)
	
		
	


