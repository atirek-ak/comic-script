# comic-script
Downloads comics from **https://readcomiconline.to** as .jpg files and converts them to a .pdf file(optional)

# Features  
* Downloads comic as .jpg files  
* Converts them to a .pdf file(optional)

## Modules used  
* selenium  
* requests  
* chromedriver  
* pillow  

## Description  
The script downloads the comic in the following format:  
```bash

├── Comics
│   ├── <comic series name>
│       ├── <comic pdf file>
│   │   ├── <comic folder containing images>
│   │   │   ├── 001.jpg
```  
The 'Comics' folder stores all the comics downloaded. It will be created the first time the script is run.  

## Running the script  
```
python selenium-script.py <url>
```
The url entered will be that of the page which displays the comic. After running the above command you will be asked if you wish to download your comic as a .pdf file also.  

## Author  
Atirek Kumar  
Github handle: atirek-ak
