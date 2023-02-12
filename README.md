# Manga Scraper

A python script that scrapes manga from a website and saves the pages as images. At last it will create a PDF file from the images collected

## Dependencies
The script requires the following libraries:
- `os`
- `urllib.request`
- `urllib.parse`
- `re`
- `argparse`
- `time`
- `BeautifulSoup`
- `WebModules`
- `MangaDict`
- `selenium`
- `PIL`

## Command Line Interface
The script can be executed from the command line with the following arguments:
- `manga`: Title of the manga you want to scrape.
- `chapter`: Chapter of the manga you want to scrape.
- `-s` / `--stopage`: Time to wait before closing the driver. This is added to allow the page to load longer and improve image quality.

```
python3 manga-scraper.py manga_title chapter_number [-s sleep_time]
```

## Setting Up Location
The script creates a directory structure to store the manga images.
- A folder named `Manga` will be created in the current working directory if it doesn't exist.
- Within the `Manga` folder, a subfolder will be created with the name `Images-<manga title>-<chapter number>`.

## Accessing the Browser & Parsing Results
The script fetches the webpage for the specified manga and chapter, and uses the BeautifulSoup library to parse the HTML content. The images are then saved to the directory created in the "Setting Up Location" section.

## Converting to PDF file
The script will use the collected images and generate one pdf file. This will create manga on your local PC. This makes it so can read it offline. 
