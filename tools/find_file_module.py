import re
from datetime import datetime
import os
from pathlib import Path

# ustawienie czasu 20210714
timeToday = datetime.today().strftime("%Y%m%d")

# znajduje sciezke do downloads, lista plikow w tym folderze
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
files = os.listdir(path_to_download_folder)  # lista plikow w folderze download

#znalezienie pliku z data na dzis
for step in files:
    if timeToday in step:
        fileNumRegex = re.compile(r"pko_trans_details_\d\d\d\d\d\d\d\d_\d\d\d\d\d\d.pdf")
        mo = fileNumRegex.search(step)
        filename = mo.group()
        path = "C:\\Users\\adamp\\Downloads\\"
        file_path = path + filename

