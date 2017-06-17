from textblob import TextBlob
import re
import string
s = "some\x00string. with\x15 funny characters"
import string


'somestring. with funny characters'

def getSentiment(book):
	with open(book, 'r') as content_file:
	    content = content_file.read()
	
	printable = set(string.printable)
	newContent = filter(lambda x: x in printable, content)

	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', newContent)

	numPolarity = 0
	numSubjectivity = 0
	totalPolarity = 0
	totalSubjectivity = 0
	for sentence in sentences:
		analysis = TextBlob(sentence)
		if analysis.sentiment.polarity != 0:
			#print(sentence)
			#print(analysis.sentiment.polarity)
			#print(analysis.sentiment.subjectivity)
			numSubjectivity += 1
			numPolarity += 1
			totalPolarity += analysis.sentiment.polarity
			totalSubjectivity += analysis.sentiment.subjectivity
			

	polarity = totalPolarity / numPolarity
	subjectivity = totalSubjectivity / numSubjectivity
	print("Total Polarity: " + str(polarity))
	print("Total Subjectivity: " + str(subjectivity))


print("Hemingway Sentiment")
getSentiment("hemingway.txt")
print("\n\nWordsworth Sentiment")
getSentiment("wordsworth.txt")
print("\n\nCamus Sentiment")
getSentiment("camus.txt")