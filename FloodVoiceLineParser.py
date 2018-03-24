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
	#Flood
        if 'oph' in trimmedLine[:3]:
            leadingWhitespace = line.split('oph')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Ophelia (Cospcaptor)\n')
            outfile.write(line)
            lineCount += 1
        elif 'oli' in trimmedLine[:3]:
            leadingWhitespace = line.split('oli')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Oliver (Matt Armstrong)\n')
            outfile.write(line)
            lineCount += 1
        elif 'dai' in trimmedLine[:3]:
            leadingWhitespace = line.split('dai')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Daisy (Haley C. McCarthy)\n')
            outfile.write(line)
            lineCount += 1
        elif 'hop' in trimmedLine[:3]:
            leadingWhitespace = line.split('hop')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hope (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        elif 'dsy' in trimmedLine[:3]:
            leadingWhitespace = line.split('dsy')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Daisy (Haley C. McCarthy)\n')
            outfile.write(line)
            lineCount += 1
        elif 'wai' in trimmedLine[:3]:
            leadingWhitespace = line.split('wai')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Waitress (Allison Seils)\n')
            outfile.write(line)
            lineCount += 1
        elif 'grl' in trimmedLine[:3]:
            leadingWhitespace = line.split('grl')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hope (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        elif 'per' in trimmedLine[:3]:
            leadingWhitespace = line.split('per')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Daisy (Haley C. McCarthy)\n')
            outfile.write(line)
            lineCount += 1
        elif 'old' in trimmedLine[:3]:
            leadingWhitespace = line.split('old')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Oliver (Matt Armstrong)\n')
            outfile.write(line)
            lineCount += 1
        elif 'vce' in trimmedLine[:3]:
            leadingWhitespace = line.split('vce')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hopes Dad (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'dad' in trimmedLine[:3]:
            leadingWhitespace = line.split('dad')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Dad (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'mom' in trimmedLine[:3]:
            leadingWhitespace = line.split('mom')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mom (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'ogl' in trimmedLine[:3]:
            leadingWhitespace = line.split('ogl')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Sister (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'mgr' in trimmedLine[:3]:
            leadingWhitespace = line.split('mgr')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Manager (N/A)\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
