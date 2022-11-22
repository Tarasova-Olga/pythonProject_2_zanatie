import zipfile

jungle_zip = zipfile.ZipFile('D:/work file.zip', 'w')
jungle_zip.write('D:/preza.pdf',
                  compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
