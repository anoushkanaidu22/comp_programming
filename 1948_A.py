
t = int(input())
for _ in range(t):

	n = int(input())

	if(n % 2 == 1):
		print("NO")
	
	else:
		ans = ""
		
		for i in range(n // 2):
			ans += "AAB"
		
		print(f"YES\n{ans}")
	 

