def find_missing_letter(array):
	beginning = ord(array[0])
	end = ord(array[len(array)-1]) - beginning
	missing_letter = ''
	for i in range(end):
		if (array[i] != str(chr(beginning+i))) and missing_letter == '':
			missing_letter = str(chr(beginning+i))
	return missing_letter
