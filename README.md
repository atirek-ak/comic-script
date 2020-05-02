# comic-script
Downloads comics from **https://readcomiconline.to** as .jpg files  

## Languages and modules
**Language:** python3  
**Modules:**  
* selenium  
* requests  
* chromedriver  

## Description  
The script downloads the comic in the following format:  
```bash
├── Comics
│   ├── <comic series name>
│   │   ├── <comic issue number>
│   │   │   ├── 001.jpg
```  
The 'Comics' folder stores all the comics downloaded. It will be created the first time the script is run.  

## To run the script  
```
python selenium-script.py <url>
```

## Author  
Atirek Kumar  
Github handle: atirek-ak
