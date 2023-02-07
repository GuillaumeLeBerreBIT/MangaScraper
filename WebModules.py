#/usr/bin/python3
##############################################
# IMPORTING NECASSARY MODULES
##############################################
import urllib.request, urllib.parse

##############################################
# FUNCTIONS
##############################################
# This makes it that it can download a link from a image providing
# The link of image, location to save, name of the image how to be saved
def downloadImage(pagelink, location, image_name):
    save_path = location + '/' + image_name + '.jpg'
    urllib.request.urlretrieve(pagelink, save_path)

