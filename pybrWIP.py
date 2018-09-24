#-*-coding: utf-8-*-
from sys import argv
def echo(*strs):
	for arg in strs:
		print(arg)

def ret(i=1,*nums):
	t = nums[0]
	for n in nums[1:]:
		t += n*i
	return t

def substract(*nums):
	r = ret(-1, *nums)
	return r
	
def plus(*nums):
	r = ret(1, *nums)
	return r


def printvars():
	print(dv)

def vars(l):
	count = 0

	for char in l:
		if char == "=":
			mn = count
			mx = count + 1
			break
		else:
			count += 1
	return (mn, mx)

if __name__ == '__main__':
	dv = {}
	try:
		file = open(argv[1], "r")
	except Exception as e1:
		print(e1)
		exit()
	else:
		code = file.readlines()
		for line in code:
			if "=" in code:
				mm = vars(line)
				dv[str(line[:mm[0]])] = line[mm[1]:]
			else: 
				try:
					exec(line)
				except Exception as e2:
					print(e2)
					exit()
				 




