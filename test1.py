def fibonacci(i):
    if i < 1:
    	return 1
    if i == 1 or i == 2:
    	return i
    return fibonacci(i-1) + fibonacci(i-2)

if __name__ == '__main__':
	print fibonacci(10)
