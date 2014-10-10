def make_float_int(n):
	n = str(n)
	n = n.replace(".","")
	return int(n)

def calculate_coins(sum):
	sum = make_float_int(sum)

	coin_1 = 0
	coin_2 = 0
	coin_5 = 0
	coin_10 = 0
	coin_20 = 0
	coin_50 = 0
	coin_100 = 0

	while(sum > 100):
		coin_100 = sum // 100
		sum -= (sum // 100) * 100	

	while(sum > 50):
		coin_50 = sum // 50
		sum -= (sum // 50) * 50

	while(sum > 20):
		coin_20 = sum // 20
		sum -= (sum // 20) * 20

	while(sum > 10):
		coin_10 = sum // 10
		sum -= (sum // 10) * 10	

	while(sum > 5):
		coin_5 = sum // 5
		sum -= (sum // 5) * 5	

	while(sum > 2):
		coin_2 = sum // 2
		sum -= (sum // 2) * 2	

	while(sum > 1):
		coin_1 = sum // 1
		sum -= (sum // 1) * 1

	return {1: coin_1, 2: coin_2, 100: coin_100, 5: coin_5, 10: coin_10, 50: coin_50, 20: coin_20}

