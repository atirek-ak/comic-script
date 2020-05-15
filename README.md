# comic-script
Because you want to enjoy Batman beating up the scum of Gotham in full screen and whenever you wish.  

# Features  
* Downloads comic as .jpg & .pdf files(can be chosen).  

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
The url entered will be that of the page which displays the comic.   
After that input a number from 0 to 2 on prompt:  
0 - to download comic in .jpg format  
1 - to download comic in .pdf format  
2 - to download comic in both .jpg & .pdf format  

## Author  
Atirek Kumar  
Github handle: atirek-ak
