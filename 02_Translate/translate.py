import sys
#creates the translation dict
translation = {}
#reads the tsv probability dictionary file
fd = open(sys.argv[1], 'r')
text = fd.readline()
#variable to keep track of which translation is most likely
highestProbability = 0.0
while text:
        #separates the values in the tsv into a list
        text = text.strip('\n')
        text = text.split('\t')
        #if the word in language 1 is not in the dict yet add it and set the probability to the highest
        if text[1] not in translation:
                translation[text[1]] = text[2]
                highestProbability = float(text[0])
        #if the word is in the dict then check if the probability is higher than the current highest probability
        elif float(text[0]) > highestProbability:
                #sets the highest probability to the new value and switches the translation
                highestProbability = float(text[0])
                translation[text[1]] = text[2]
        text = fd.readline()
#reads the user input to translate
userInput = sys.stdin.readline()
userInput = userInput.split()
outputString = ''
#iterate through each word
for i in range(len(userInput)):
        #checks if the word without various punctuation is in the dictionary
        if userInput[i].strip('.?!¿¡:,\'"()\'-·;&') in translation:
                #if it is add the translation to the ouput string and add a space
                outputString += translation[userInput[i]] + ' '
        else:
                #if it is not place an asterisk before the user's input and add a space
                outputString += '*' + userInput[i] + ' '
#print the output translation
print(outputString)
