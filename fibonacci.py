def fibonacci(x):
	if x > 1:
		return (fibonacci(x-1)) + (fibonacci(x-2))
	else:
		return 1

print(fibonacci(15))