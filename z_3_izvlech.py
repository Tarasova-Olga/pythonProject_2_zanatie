import zipfile

jungle_zip = zipfile.ZipFile('D:/work file.zip')
for file in jungle_zip.namelist():
    if jungle_zip.getinfo(file).file_size > 1024 * 1024:
        jungle_zip.extract(file, 'D:/')

jungle_zip.close()
