import re
from datetime import datetime
import os
from pathlib import Path

def find_attachment():
    timeToday = datetime.today().strftime("%Y%m%d")
    download_path = str(os.path.join(Path.home(), "Downloads"))
    files = os.listdir(download_path)
    fileNumRegex = re.compile(r'pko_trans_details_\d\d\d\d\d\d\d\d_\d\d\d\d\d\d.pdf')

    file_path = ''
    filename = ''
    for step in files:
        if timeToday in step:
            mo = fileNumRegex.search(step)
            filename = mo.group()
            file_path = download_path + "\\" + filename

    return filename, file_path


