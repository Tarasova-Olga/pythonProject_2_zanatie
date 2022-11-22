import zipfile

jungle_zip = zipfile.ZipFile('D:/work file.zip')
jungle_zip.extractall('D:/pasp')

jungle_zip.close()
