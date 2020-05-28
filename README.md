# comic-script
To download and read comics at your convenience.

# Features  
* Downloads comic as .pdf file.  
Ps. - You could also download it as .jpg by cloning the jpg branch.  
* You can download a single issue or a series.

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
```  
The 'Comics' folder stores all the comics downloaded. It will be created the first time the script is run.  

## Running the script  
```
python selenium-script.py <url>
```
The url entered will be that of the issue which displays the comic or the page that displays all the issues of a series.   
Ex.- 
```
python selenium-script.py https://readcomiconline.to/Comic/Injustice-Gods-Among-Us-Year-Three
python selenium-script.py https://readcomiconline.to/Comic/Injustice-Gods-Among-Us-Year-Three/Issue-14?id=15303
```
