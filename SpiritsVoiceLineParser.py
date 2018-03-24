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
	#Spirits
        if 'alx' in trimmedLine[:3]:
            leadingWhitespace = line.split('alx')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Alex (Bonnie Mitchel)\n')
            outfile.write(line)
            lineCount += 1
        elif 'cae' in trimmedLine[:3]:
            leadingWhitespace = line.split('cae')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Caelum (Daniel Acosta)\n')
            outfile.write(line)
            lineCount += 1
        elif 'caex' in trimmedLine[:4]:
            leadingWhitespace = line.split('caex')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Caelum (Daniel Acosta)\n')
            outfile.write(line)
            lineCount += 1
        elif 'hmom' in trimmedLine[:4]:
            leadingWhitespace = line.split('hmom')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #House Mother "Jianmei" (Vivi)\n')
            outfile.write(line)
            lineCount += 1
        elif 'gen' in trimmedLine[:3]:
            leadingWhitespace = line.split('gen')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Genevieve (Lasli Tran)\n')
            outfile.write(line)
            lineCount += 1
        elif 'wra' in trimmedLine[:3]:
            leadingWhitespace = line.split('wra')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Wraith (Kenneth Faircloth)\n')
            outfile.write(line)
            lineCount += 1
        elif 'ama' in trimmedLine[:3]:
            leadingWhitespace = line.split('ama')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mama (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'Dad' in trimmedLine[:3]:
            leadingWhitespace = line.split('Dad')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Papa (N/A)\n')
            outfile.write(line)
            lineCount += 1
        elif 'cxx' in trimmedLine[:3]:
            leadingWhitespace = line.split('cxx')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Caelum (Daniel Acosta)\n')
            outfile.write(line)
            lineCount += 1
        elif 'gez' in trimmedLine[:3]:
            leadingWhitespace = line.split('gez')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Genevieve (Lasli Tran and Other)\n')
            outfile.write(line)
            lineCount += 1
        elif 'gex' in trimmedLine[:3]:
            leadingWhitespace = line.split('gex')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Genevieve (Lasli Tran and Other)\n')
            outfile.write(line)
            lineCount += 1
        elif 'nurse' in trimmedLine[:3]:
            leadingWhitespace = line.split('nurse')[0]
            outfile.write(leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Nurse ()\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
