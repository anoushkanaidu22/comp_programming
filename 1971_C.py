t = (int)(input())

for _ in range(t):
	position = input().split(" ")
	a1 = (int)(position[0])
	b1 = (int)(position[1])
	c1 = (int)(position[2])
	d1 = (int)(position[3])

	a = min(a1, b1)
	b = max(a1, b1)

	if (((c1 > a and c1 < b) and (d1 < a or d1 > b)) or ((d1 > a and d1 < b) and (c1 < a or c1 > b))):
		print("yes")
	else:
		print("no")

		

		
