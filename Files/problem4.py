# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def ispal(num):
	num = str(num)
	# if the given number has even digits we break it in the middle and compare
	# if the given number has odd number of digits we break excluding the middle digit
	if not len(num)%2:
		if num[:int(len(num)/2)]==num[int(len(num)/2):][::-1]:
			return True
		return False
	elif len(num)%2:
		if num[:int((len(num)-1)/2)]==num[int((len(num)-1)/2)+1:][::-1]:
			return True
		return False
	else:
		return False
	

def largestpal(num):
	high = int((10**num)-1)
	low = int((10**(num-1))-1)
	lis = []
	for i in range(high, low, -1):
		for j in range(i, low, -1):
			p = i*j
			if ispal(p):
				lis.append(p)
	lis.sort(reverse=True)
	return lis[0]

print(largestpal(3))
