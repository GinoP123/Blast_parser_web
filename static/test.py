def solve(tup):
	result = []
	stack = []

	for val in tup:
		if not stack or val < stack[-1]:
			stack.append(val)
		else:
			while stack and val >= stack[-1]:
				result.append(stack.pop())
			stack.append(val)

	while stack:
		result.append(stack.pop())

	return result


def print_out(tup):
	print(f"input: {tup}")
	print(f"output: {solve(tup)}")


print_out([1, 2, 3, 5, 4])
# MUST BE IN CLUSTERS OF FORWARD AND REVERSED SORTED



# can't solve cycles of length 5



# can break down into sub-parts

# 		Stuff After must be in order
# (5, (1, 2, 3, 4))


#	Can break down into positions and num of bottom of stack
# 	5, 1, 2, 6, 3, 4,



# n=2
# 1 2
# f f

# 2 1
# r r

# n=3
# 1 2 3
# f f f == f f r


# 3 1 2
# r f f

# 2 1 3
# r r f

# 3 2 1
# r r r

# 1 3 2
# f r r

# NOT
# 2 3 1
# f f r //////

# No cycles with length > 2

# 4 3 2 1



# Only reverse sorted or normal sorted

# when nothing after, r == f are interchangable


# n==4

# 1       2        3        4
# (1,4)   (2, 4)   (3, 4)   (4)

# 4       1        2        3
# (1,4)   (2, 4)   (3, 4)   (4)

# 2 ^ (n-1) choices
# 



