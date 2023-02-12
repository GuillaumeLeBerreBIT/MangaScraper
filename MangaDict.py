#!/usr/bin/python3
##############################################
# DIFFERENT MANGAS
##############################################
# File containing the different links of the Mangas

def MangaLinks(link):

    if link == "AOT" or link == "AttackOnTitan":
        url = 'https://ww8.readsnk.com/chapter/shingeki-no-kyojin-chapter-'
        name = "AOT" 
    
    if link == "OP" or link == "OnePiece":
        url = 'https://ww9.readonepiece.com/chapter/one-piece-chapter-'
        name = "OP"
    
    if link == "Naruto":
        url = 'https://ww8.readnaruto.com/chapter/naruto-chapter-'
        name = "Naruto"
    
    if link == "Boruto":
        url = 'https://ww8.readnaruto.com/chapter/boruto-naruto-next-generations-chapter-'
        name = "Boruto"
    
    if link == "BC" or link == "BlackClover":
        url = 'https://ww7.readblackclover.com/chapter/black-clover-chapter-'
        name = "BC"
    
    if link == "TR" or link == "TokyoRevengers":
        url = 'https://readtokyorevengers.net/chapter/tokyo-revengers-chapter-'
        name = "TR"
    
    if link == "MHA" or link == "MyHeroAcademia":
        url = 'https://ww7.readmha.com/chapter/boku-no-hero-academia-chapter-'
        name = "MHA"
    
    if link == "DS" or link == "DemonSlayer":
        url = 'https://ww6.demonslayermanga.com/chapter/demon-slayer-kimetsu-no-yaiba-chapter-'
        name = "DS"
    
    if link == "VS" or link == "VinlandSaga":
        url = 'https://ww2.readvinlandsaga.com/chapter/vinland-saga-chapter-'
        name = "VS"
    
    if link == "JJK" or link == "JujutsuKaisen":
        url = 'https://ww2.readjujutsukaisen.com/chapter/jujutsu-kaisen-chapter-'
        name = "JJK"
    
    if link == "CSM" or link == "ChainsawMan":
        url = 'https://ww2.readchainsawman.com/chapter/chainsaw-man-chapter-'
        name = "CSM"

    # This will return the variables in a dictionary, can call for them in the main code.
    return {'0': url, '1': name}