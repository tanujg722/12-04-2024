#f = open("fileone.txt", 'w+')
#f.write("One file")
#f.close()

#f = open("filetwo.txt", 'w+')
#f.write("Two file")
#f.close()

import zipfile

comp_file = zipfile.ZipFile("comp_file.zip",'w')

comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
zip_obj = zipfile.ZipFile("comp_file.zip","r")
zip_obj.extractall("extracted_content")