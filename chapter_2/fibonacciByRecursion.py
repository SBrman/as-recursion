def fib(n):
	print(f"fib(n) is called.")
	if n in {0, 1}:
		print(f"Call fib({n}) is returning 1.")
		return 1
	else:
		print(f"Calling fib({n}) and fib({n-1})")
		res = fib(n-1) + fib(n-2)
		print(f"Call to fib({n}) returning ")
		return res

if __name__ == "__main__":
	print(fib(10))
