
"""
dai o que preciso fazer:
1. tirar os timestamps (ja fiz!)
2. tirar os simbolos (ja fiz)
3. selecionar so as linhas que tem C: no comeco
4. dessas linhas, contar as palavras de cada linha
5. fazer isso pra todos os textos numa pasta
"""

import nltk
from nltk.tokenize import word_tokenize
import string
import re

nltk.download('punkt')

files_to_read = [
	"input.txt",
	"input2.txt"
]

output = []
for filename in files_to_read:
	# Open the file
	with open(filename, "r") as file:
		# Saves the current filename in the output
		output.append(filename)
		# Creates as list with all lines of the file
		lines = file.readlines()
		# Read each line of lines
		for line in lines:
			# Read line just if it contains 'C:'
			if 'E:' in line:
				# Removes 'C:'
				headless = line.replace('E:', '')
				# Remove numbers
				numberless = re.sub(r"\d", "", headless)
				# Remove timestamp
				timeless = re.sub(r'(\[::.])+', "", numberless)
				# Creates cleaner token
				table = str.maketrans(
					'', '', 
					string.punctuation
				)
				# Removing punctuation
				cleaned = timeless.translate(table)
				# Separate works
				words = word_tokenize(cleaned)
				# Count words
				number_of_words = str(len(words))

				output.append(number_of_words)

# Write output
outputfile = open("output.txt","w+")
text = '\n'.join(output)
outputfile.write(text)

outputfile.close()
file.close()