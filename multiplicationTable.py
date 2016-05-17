min = int(raw_input("Where would you like to start your multiplication table? "))
max = int(raw_input("Where would you like to end your table? "))
l1 = range(min, max + 1)
l2 = range(min, max + 1)

def multiply_list(l1,l2):
	'''Multiplies each item in a list by each item in another'''
	answers = []
	for x in l1:
		rowAnswers = []
		for y in l2:
			rowAnswers.append(x * y)
		answers.append(rowAnswers)

	return answers

def print_table(l1, l2, answers):
	'''Prints multiplication table neatly'''
	output = ' '
	for item in l1:
		if len(str(item)) == 1:
			output += '|   {}'.format(item)
		elif len(str(item)) == 2:
			output += '|  {}'.format(item)
		elif len(str(item)) == 3:
			output += '| {}'.format(item)
	print output 
	output = ''
	print("----------------")
	x = 0
	for list in answers:
		y = 0
		output = ''
		for item in list:
			if len(str(item)) == 1:
				if y == 0:
					output += ("{}|   {}".format(l2[x], answers[x][y]))
				else:
					output += ("|   {}".format(answers[x][y]))
			elif len(str(item)) == 2:
				if y == 0:
					output += ("{}|  {}".format(l2[x], answers[x][y]))
				else:
					output += ("|  {}".format(answers[x][y]))
			elif len(str(item)) == 3:
				if y == 0:
					output += ("{}| {}".format(l2[x], answers[x][y]))
				else:
					output += ("| {}".format(answers[x][y]))
			y += 1
		print output
		x += 1
		
answers = multiply_list(l1, l2)
print_table(l1, l2, answers)
		
	
		
	

		