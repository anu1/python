with open('./input_test_file.txt') as infile:
	for line in infile:
		len_line = len(line)
		if len_line > 1:
			print(line,end="")
