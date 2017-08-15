with open('./input_test_file.txt') as infile:
	for line in infile:
    		freshline = line.strip()
	if freshline:
		print(freshline)
