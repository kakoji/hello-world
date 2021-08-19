def ascii_pyramid(width, char='*'):
	for i in range(1, width+1):
		for j in range(i):
			print(char, end='')
		print()

if __name__ == '__main__':
	ascii_pyramid(10)
