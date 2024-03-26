#zip files
import zipfile

zip_obj = zipfile.ZipFile('C:/Github/test/unzip_me_for_instructions.zip','r')
zip_obj.extractall('intructions extracted')
