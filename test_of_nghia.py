def findMax(array):
	findOfMax = 0
	for i in array:
		if findOfMax < i: findOfMax = i
	return findOfMax

def findMin(array):
	findOfMin = 0
	for i in array:
		if findOfMin > i: findOfMin = i
	return findOfMin

def countAverage(array):
		score = 0
		for i in array:
			score = score + i
		return score

def areaCount():
	isLoop = True
	while isLoop:
		try:
			longs = float(input('Nhập chiều dài: '))
			width = float(input('Nhập chiều rộng: '))
			area = longs * width
			isLoop = False
			print(isLoop)
		except:
			print('Vui lòng nhập số')
	return area

def areaCount():
	try:
		longs = float(input('Nhập chiều dài: '))
		width = float(input('Nhập chiều rộng: '))
		area = longs * width
		return area
	except:
		while True:
			print('Vui lòng nhập số')
			print(areaCount())

print(areaCount())

	
			

def total(a, b):
	return a + b

# array  = [1,3,4,-1]

	