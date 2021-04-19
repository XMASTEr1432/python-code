import os
with open('urls.txt') as f:
    for line in f:
        os.system("python -m youtube_dl "+"--write-thumbnail "+"--skip-download "+line)