import sys
#read file for language 1
fdLanguage1 = open(sys.argv[1], 'r')
#read file for language 2
fdLanguage2 = open(sys.argv[2], 'r')
#creates 2 strings for the first line of each corpus
textLanguage1 = fdLanguage1.readline()
textLanguage2 = fdLanguage2.readline()
text1 = []
text2 = []
textMatrix = {}

while textLanguage1:
        #takes the lines of text and creates a list of words for each
        text1 = textLanguage1.split(' ')
        text2 = textLanguage2.split(' ')
        #removes various punctuation
        for i in range (len(text1)):
                text1[i] = text1[i].strip()
                text1[i] = text1[i].strip('.?!¿¡:,\'"()-·;&')
        for i in range (len(text2)):
                text2[i] = text2[i].strip()
                text2[i] = text2[i].strip('.?!¿¡:,\'"()-·;&')
        #Checks if a word is not in the matrix if it's not it adds it
        #Checks if each word in the same line of the second language is not in the first word's dict
        #if it is not it adds it to it and sets the value to 1
        #if it is it increments the value by 1
        for i in range (len(text1)):
                for j in range(len(text2)):
                        if text1[i] not in textMatrix:
                                textMatrix[text1[i]] = {}
                        if text2[j] not in textMatrix[text1[i]]:
                                textMatrix[text1[i]][text2[j]] = 1
                        else:
                                textMatrix[text1[i]][text2[j]] += 1
        #changes strings to next line
        textLanguage1 = fdLanguage1.readline()
        textLanguage2 = fdLanguage2.readline()
for w1 in textMatrix:
        #counter to find how many words each entry contains
        counter = 0.0
        #loop to increment the counter
        for w2 in textMatrix[w1]:
                counter += textMatrix[w1][w2]
        #averages the values and prints it, the word in language 1, and the word in language 2
        for w2 in textMatrix[w1]:
                print('%f\t%s\t%s' % (textMatrix[w1][w2] / counter, w1, w2))

