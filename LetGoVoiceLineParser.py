#Voice Parser 1.0.2
print('Please enter the file to be parsed. Include the file path.')
inputFilePath = input()

inputFileName = inputFilePath.rsplit('\\', 1)[1]
filePath = inputFilePath.rsplit('\\', 1)[0]

outputFileName = '\\parsed_' + inputFileName
outputFilePath = filePath + outputFileName

print('Please enter the scene\'s route tag.')
routeTag = input()

print('Please enter the scene number.')
sceneNumber = input()

lineCount = 1

with open(inputFilePath, 'r', encoding="utf8") as infile, open(outputFilePath, 'w', encoding="utf8") as outfile:
    for line in infile:
        trimmedLine = line.replace(" ", "")
	#Let Go
        if 'ow' in trimmedLine[:2]:
            leadingWhitespace = line.split('ow')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Old Woman (Ashe Thurman)\n')
            outfile.write(line)
            lineCount += 1
        elif 'om' in trimmedLine[:2]:
            leadingWhitespace = line.split('om')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Old Man (Adam Warren)\n')
            outfile.write(line)
            lineCount += 1
        elif 'may' in trimmedLine[:3]:
            leadingWhitespace = line.split('may')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Maya (shiena)\n')
            outfile.write(line)
            lineCount += 1
        elif 'eli' in trimmedLine[:3]:
            leadingWhitespace = line.split('eli')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Elijah (Michael Potok)\n')
            outfile.write(line)
            lineCount += 1
        elif 'mom' in trimmedLine[:3]:
            leadingWhitespace = line.split('mom')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mom (N/A)\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
