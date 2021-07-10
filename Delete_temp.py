import os, subprocess
clean_folder = r'c:\windows\temp'
pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % clean_folder, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
rTup = pObj.communicate()
rCod = pObj.returncode
if rCod == 0:
    print 'Deleted Temp files'
else:
    print 'Unable to delete temp files'
