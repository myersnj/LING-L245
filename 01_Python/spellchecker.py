import sys
freq = []
fd = open('freq.txt', 'r')
for line in fd.readlines():
        line = line.strip('\n')
        (f, w) = line.split('\t')
        freq.append(w)
fd.close()

vocab = {}
text = sys.stdin.read()
text = text.split(' ')
for i in range(len(text)):
        text[i] = text[i].strip()
outText = []
for i in range(len(text)):
        if text[i].strip('.,?!') in freq:
                outText.append('%s' % text[i])
        else:
                outText.append('*%s' % text[i])
for i in range(len(outText)):
        sys.stdout.write('%s ' % outText[i])
print()
