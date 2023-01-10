def repeat_to_length(string, n):
	r = (string * (n//len(string) + 1))[:n]
	return r.count('a')


result = repeat_to_length('aba', 10)
print(result)