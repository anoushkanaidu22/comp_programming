t = (int)(input())

for _ in range(t):

	people = [int(x) for x in input().split()]

	intro = people[0]
	extro = people[1]
	uni = people[2]

	tents = intro
	
	leftover = extro % 3
	if ((leftover != 0) and (leftover + uni < 3)):
		print(-1)
	else:
		if (leftover != 0): 
			tents += 1
			unis_left = uni - (3 - leftover)
		else:
			unis_left = uni
		extro_tents = extro // 3
		unis_tents = unis_left // 3
		unis_remaining = unis_left % 3
		if (unis_remaining != 0):
			tents += 1
		tents += extro_tents + unis_tents
		print(tents)
	
	
