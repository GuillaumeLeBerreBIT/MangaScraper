#!/usr/bin/python3
##############################################
# NOTES
##############################################
# Add different links in the extra module
# Add specific folder names 

##############################################
# IMPORTING NECASSARY MODULES
##############################################

import os, urllib.request, urllib.parse, re, argparse, time
from bs4 import BeautifulSoup
import WebModules as web            # Not yet in use
import MangaDict as dic
from selenium import webdriver
from PIL import Image

##############################################
# COMMAND LINE INTERFACE
##############################################

parser = argparse.ArgumentParser(description='Manga Scraper')                       
parser.add_argument('manga', type=str, help='Give a title of a Manga you want to read.')
parser.add_argument('chapter', type=str, help='Provide a chapter want to read/download.')
parser.add_argument('-s', '--stopage', type=int, default=0,required = False, help='Give a time to set the sleep before closing the driver.\
Is added so the page can load longer and have better quality.')                                   
args = parser.parse_args()

# Making the url links to AOT Manga. 
link = args.manga
dictManga = dic.MangaLinks(link)

##############################################
# Art
##############################################

print("▀████▄     ▄███▀\n\
  ████    ████\n\
  █ ██   ▄█ ██  ▄█▀██▄ ▀████████▄  ▄█▀█████▄█▀██▄\n\
  █  █▓  █▀ ██ ██   ██   ██    ██ ▄██  ██ ██   ██\n\
  ▓  █▓▄█▀  ██  ▄███▓█   █▓    ██ ▀▓▓███▀  ▄███▓█\n\
  ▓  ▀▓█▀   ██ █▓   ▓█   █▓    ▓█ █▓      █▓   ▓█\n\
  ▓  ▓▓▓▓▀  ▓▓  ▓▓▓▓▒▓   ▓▓    ▓▓ ▀▓▓▓▓▓▀  ▓▓▓▓▒▓\n\
  ▒  ▀▓▓▀   ▓▓ ▓▓   ▒▓   ▓▓    ▓▓ ▓▒      ▓▓   ▒▓\n\
▒ ▒▒▒ ▒   ▒ ▒▒▒▒▓▒ ▒ ▓▒▒ ▒▒▒  ▒▓▒ ▒▒ ▒▓▒ ▒▒▓▒ ▒ ▓▒\n\
                                  ▒▒     ▒▒\n\
                                  ▒▒▒▒ ▒▒\n")

##############################################
# SETTING UP LOCATION
##############################################

location = os.getcwd()

# Make a path if not exist and change to the path >> Folder containing all the mangas
if not os.path.isdir("Manga"):
    os.mkdir("Manga")
    os.chdir("Manga")
else: 
    os.chdir("Manga")

# Set the location of the head folder >> Used to have full pdf file
full_chapter_loc = os.getcwd()
folder_of_images = "Images-" + dictManga['1'] + "-" + args.chapter
# Make a path if not exist and change to the path to a subfolder >> Containing the folder of everything of one chapter
if not os.path.isdir(folder_of_images):
    os.mkdir(folder_of_images)
    os.chdir(folder_of_images)
else: 
    os.chdir(folder_of_images)

##############################################
# ACCESING THE BROWSER & PARSE RESULTS
##############################################

# Returns the number of the chapter
chapter = args.chapter
filled = chapter.zfill(3)
# Get the full formatted url
completeurl = dictManga['0'] + filled

# Fetch webpage and save in soup object
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
request = urllib.request.Request(completeurl, headers = headers)
response = urllib.request.urlopen(request)
response_data = response.read().decode('utf-8')
soup = BeautifulSoup(response_data, 'html.parser')

pages_container = soup.find("div", {"class" : "js-pages-container"})

print("\n" + "-"*40)
# Setting up the variables
counter = 1
dictChap = {}
# Loop over the img tags
for page in pages_container:
    # There are '-1' parsed as well so convert everything to a string
    image = page.find("img")
    # Want to convert each line to str to test if True
    result = str(image)

    # Parse only the lines with a <img>
    if re.search("img", result):
        # Work with the soup object >> Dictionary
        # This will provide with the link of the picture
        pagelink = image["src"]
        # Creating a name for each picture
        image_name = str(counter) + '-Chapter-' + filled + '.png'
        # Organize order by using a dictionary
        dictChap[counter] = image_name
        counter += 1
        
        print("Downloading image: {}".format(pagelink))

        # Needed to install the version of chromedriver and add it where can be easily accessed
        path = '/usr/bin/chromedriver'
        # Want to use webrowser Chrome and the Webdriver is at path
        driver = webdriver.Chrome(path)
        # Getting the website we want >> Use the image link
        driver.get(pagelink)
        # Give the page time to load (not necasssary, havent found if it has impact or not on quality)  
        time.sleep(args.stopage)
        # Takes a screenshot of the page at link
        driver.save_screenshot(image_name)
        # Does quit the browser
        driver.quit()
print("\n" + "-"*40)

# To check the order and if the capters are in the dicitonary. 
#print(dictChap)

##############################################
# CONVERT TO ONE PDF FILE
##############################################
print("\n" + "-"*40 + "\nConverting the pictures in one PDF file\n" + "-"*40 + "\n")
# We want to go out of the subfolder where the converted images will be
os.chdir(full_chapter_loc)
# Adding the image folde to the path
images_loc = full_chapter_loc + '/' + folder_of_images + '/'

# This code will convert each image to RGB mode before saving the images as a PDF. 
# The RGB mode does not have an alpha channel, so it can be saved as a PDF without any issues.
images = [Image.open(images_loc + v).convert("RGB") for v in dictChap.values()]

pdf_path = full_chapter_loc + '/' + dictManga['1'] +'-Chapter-' + filled + '.pdf'
    
images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

print("\nTask complete! Enjoy reading!")


