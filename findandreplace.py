import os
texttofind = 'Europe'
texttoreplace = 'India'
sourcepath = os.listdir('InputFiles/')
for file in sourcepath:
    inputfile = 'InputFiles/'+ file
    print('Conversion is ongoingfor:' +inputfile)
    with open(inputfile,'r') as inputfile:
        filedata = inputfile.read()
        freq =0
        freq =filedata.count(texttofind)
        destinationpath = 'OutputFile/' + file
        filedata = filedata.replace(texttofind,texttoreplace)
        with open(destinationpath,'w') as file:
            file.write(filedata)
            print('Total %d Record replace' %freq)
