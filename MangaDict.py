#!/usr/bin/python3
##############################################
# DIFFERENT MANGAS
##############################################
# File containing the different links of the Mangas

def MangaLinks(link):

    if link == "AOT" or link == "AttackOnTitan":
        url = 'https://ww8.readsnk.com/chapter/shingeki-no-kyojin-chapter-'
        name = "AOT"
    # This will return the variables in a dictionary, can call for them in the main code. 
    return {'0': url, '1': name}