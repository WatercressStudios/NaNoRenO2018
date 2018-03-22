#Voice Parser 1.0.1
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
        if '    ow' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Old Woman (Ashe Thurman)\n')
            outfile.write(line)
            lineCount += 1
        elif '    om' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Old Man (Adam Warren)\n')
            outfile.write(line)
            lineCount += 1
        elif '    may' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Maya (shiena)\n')
            outfile.write(line)
            lineCount += 1
        elif '    eli' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Elijah (Michael Potok)\n')
            outfile.write(line)
            lineCount += 1
        elif '    oph' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Ophelia (Cospcaptor)\n')
            outfile.write(line)
            lineCount += 1
        elif '    oli' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Oliver (Matt Armstrong)\n')
            outfile.write(line)
            lineCount += 1
        elif '    hop' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hope (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        elif '    dsy' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Daisy (Haley C. McCarthy)\n')
            outfile.write(line)
            lineCount += 1
        elif '    wai' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Waitress (Allison Seils)\n')
            outfile.write(line)
            lineCount += 1
        elif '    grl' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hope (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        elif '    per' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Daisy (Haley C. McCarthy)\n')
            outfile.write(line)
            lineCount += 1
        elif '    old' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Oliver (Matt Armstrong)\n')
            outfile.write(line)
            lineCount += 1
        elif '    alx' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Alex (Bonnie Mitchel)\n')
            outfile.write(line)
            lineCount += 1
        elif '    cae' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Caelum (Daniel Acosta)\n')
            outfile.write(line)
            lineCount += 1
        elif '    caex' in line[:8]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Caelum (Daniel Acosta)\n')
            outfile.write(line)
            lineCount += 1
        elif '    hmom' in line[:8]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #House Mother "Jianmei" (Vivi)\n')
            outfile.write(line)
            lineCount += 1
        elif '    gen' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Genevieve (Lasli Tran)\n')
            outfile.write(line)
            lineCount += 1
        elif '    wra' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Wraith (Kenneth Faircloth)\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
