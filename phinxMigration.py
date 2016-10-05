o = open('phinxMigration.txt', 'w')
o.write("INSERT INTO `industry` (`name`, `parentCategory`, `sortOrder`)\nVALUES ")

'''
	This file/function takes the Industries Google Drive spreadsheet and
	converts the CSV file to a linked SQL query to be used for a Phinx
	migration.

	by Will Plucinsky 9/30/2016
'''


counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = -1
j = 1
k = 0
with open('input.csv', 'r') as f:
	for line in f:
		if i == -1:
			# main categories, 1st line of CSV
			for cnt, part in enumerate(line.rstrip().split(',')):
				if len(part) > 1:
					o.write("('"+part+"', 0, "+str(j)+"),\n")
					i+=1
					counts[cnt] = j
					j+=1
		else:
			j = 0
			for cnt, part in enumerate(line.rstrip().split(',')):
				if j % 2 == 0:
					# second category
					if len(part) > 1:
						o.write("('"+part+"', "+str(counts[cnt])+", NULL),\n")
						i+=1
					k = i
					j+=1
				else:
					# third category
					for cnt2, part2 in enumerate(part.rstrip().split(';')):
						if len(part2) > 1:
							o.write("('"+part2.lstrip().rstrip()+"', "+str(k+1)+", NULL),\n")
							i+=1
					j+=1
					

