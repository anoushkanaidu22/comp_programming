t = (int)(input())

def flip(coin_idx, coin_list):
	prev = coin_idx - 1
	nnext = coin_idx + 1
	if (prev < 0):
		prev = len(coin_list) - 1
	if (nnext > len(coin_list) - 1):
		nnext = 0	

	if (len(coin_list) > 2):
		if (coin_list[prev] == "U"):
			coin_list[prev] = "D"
		else:
			coin_list[prev] = "U"
		if (coin_list[nnext] == "U"):
			coin_list[nnext] = "D"
		else:
			coin_list[nnext] = "U"
		
	del coin_list[coin_idx]			

def search_lst(turn_cnt, coin_list):
	for coin_idx in range(len(coin_list)):
		if (coin_list[coin_idx] == "U"):
			turn_cnt += 1
			flip(coin_idx, coin_list)
			return search_og(turn_cnt, coin_list)
	return turn_cnt
	
def search_nxt(turn_cnt, coin_list):
	for coin_idx in range(len(coin_list)):
		prev = coin_idx - 1
		nnext = coin_idx + 1
		if (prev < 0):
			prev = len(coin_list) - 1
		if (nnext > len(coin_list) - 1):
			nnext = 0	
	
		if (coin_list[coin_idx] == "U"):
			if ((coin_list[prev] == "U") or (coin_list[nnext] == "U")):
				turn_cnt += 1
				flip(coin_idx, coin_list)
				return search_og(turn_cnt, coin_list)
	return search_lst(turn_cnt, coin_list)


def search_og(turn_cnt, coin_list):
	if(len(coin_list) == 1):
		if (coin_list[0] == "U"):
			turn_cnt += 1
		return turn_cnt
	for coin_idx in range(len(coin_list)):
		prev = coin_idx - 1
		nnext = coin_idx + 1
		if (prev < 0):
			prev = len(coin_list) - 1
		if (nnext > len(coin_list) - 1):
			nnext = 0
		if (coin_list[coin_idx] == "U"):
			if ((coin_list[prev] == "U") and (coin_list[nnext] == "U")):	
				turn_cnt += 1
				flip(coin_idx, coin_list)
				return search_og(turn_cnt, coin_list)
	return search_nxt(turn_cnt, coin_list)
	
for _ in range(t):
	num_coins = (int)(input())
	coin_string = input()
	coin_list = [x for x in coin_string]
	turn_cnt = 0
	res = search_og(turn_cnt, coin_list)
	if (res % 2 == 0):
		print("no")
	else:
		print("yes")
	
	


