import requests, re, lxml, os
from pathlib import Path
import urllib

img_files = os.listdir("./static")
img_file_slugs = []
slugs = []

# Get slugs from img files
for img in img_files:
	img = img[:-5] #remove .jpeg
	img = img.lower()
	img_file_slugs.append(img)

cid_file = open("CIDs.txt", 'r')

for line in cid_file:
	slugs.append(line.strip())

print("testing if image slugs exist in db")
for slug in img_file_slugs:
	if not slug in slugs:
		print(slug)

print("testing if db slugs exist in image files")
for slug in slugs:
	if not slug in img_file_slugs:
		print(slug)