#
# This script reads vCard (.vcf) file, extracts contacts which
# have phone number and saves them to another vCard file.
#
# Mikk
# 2015-01-03
#

import codecs

# Use other file names if you like
inFileName = 'ContactList.vcf'
outFileName = 'FilteredContactList.vcf'

print('Trying to open vCard file "' + inFileName + '".')
print('Saving filtered contacts to "' + inFileName + '".')

inFile = codecs.open(inFileName, 'r', encoding='utf8')
outFile = codecs.open(outFileName, 'w', encoding='utf8')
totalCount = 0
numbersCount = 0
waitEnd = False
hasNumber = False
contactLines = []

# Just read all lines and check BEGIN and END pairs.
# If there's a TEL in between then consider this as phone number
for line in inFile:
    if not waitEnd:
        if line == 'BEGIN:VCARD\r\n':
            hasNumber = False
            waitEnd = True
            contactLines.clear()
            contactLines.append(line)
    else:
        contactLines.append(line)
        if line.startswith('TEL'):
            hasNumber = True
        if line == 'END:VCARD\r\n':
            waitEnd = False
            totalCount += 1
            if hasNumber:
                numbersCount += 1
                for bufLine in contactLines:
                    outFile.write(bufLine)

inFile.close()
outFile.close()

print('Found ' + str(totalCount) + ' contacts.')
print('Saved ' + str(numbersCount) + ' contacts which had phone number.')
