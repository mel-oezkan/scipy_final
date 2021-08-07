# Scientific Python - Final Project

## ToDo:
### SCRAPPER

#### Task 1
A function to scrap all the items given a search query. E.g. the user wants alle entries from page 1 to 10 containing male t-shirts.

- [X] Iterating trough the pages 
    - [X] Handling min and max amount of articles to read
    - [X] Implementing a stop criterion
    - [X] Fail case. What happens if there is no next page?
- [ ] Complete the category and size ids

#### Task 2
- [X] Add another function to scrap the images from the articles
- [ ] Needs a error handler
    - Page can be already deleted such that reading images will result in error

#### Task 3
- [X] Reding of the config file and creating the respective url
- [ ] Handling of the sub catrogires 
    - "Ripped Jeans" -> "Clothing"
    - "Manschenttenknöpfe" -> "Schmuck"
- [ ] Creating mappings from "Manschenttenknöpfe" to clothing sizes

### VISUALIZATION
- [ ] Plotting the different attributes according to clothing type
- [ ] Comparing availability between genders 
- [ ] Plot the color diversity between genders
- [X] Sampling 4 rows from the dataset and ploting the images of those articles
    - (implemented in ```src/utils/visualizer.py```)
    - amount can be changed by modifiying the range it iterates trough
- ...

### ANNOTATOR
- [ ] Create the annotation page
    - [ ] Handling the dataset
        - [ ] Save the images in a seperate folder when the user tags them as either like or dislike
        - [ ] Save all images from one article
        - [ ] (Include relabeling of unseen images)
    - [ ] Ajax interactions
- ...


## Short description
This project will contain an interactive **web scrapper** with an **user interface** based on the browser where the use will be able to filter their search and **annotate** the scrapped data. However the scrapper will only work on the webstore of Vinted.com.

## Requirements
For the scrapper to run 

Install python requirements using pip:  
```pip install -r requirements.txt```  

Create conda env using:  
```conda env create -f scrapper.yml ```

## Instructions
Each of the modules has a seperate argument. If you want to run the scrapper just type:  
```python run.py --mode scrapper --page_range [1-15] --config_file main.yaml```

When running the scrapper you have to create or modifiy a config file. In this case this fill will be ```config.yaml```. Within this file you can specify which kind of clothes you want and also define some other parameters such as size, color, brands ect.. When creating the config file the entries should follow this pattern
**config.yaml**
```
args = [
        {"gender": "femal", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
        {"gender": "male", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
        {"gender": "male", "category": pants", "size": ["M", "L"]}
    ]
```

or using the yaml type description:
```
args:
    - {"gender": "femal", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
    - {"gender": "male", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
    - {"gender": "male", "category": pants", "size": ["M", "L"]}
```

resulting urls should look something like:
``` https://www.vinted.de/vetements?color_id[]=1&color_id[]=12&catalog[]=76&catalog[]=1904&time=1628187997&page=500 ```

## File structure
- data
    - contains the generated csv files with information about the seller, price, color, clothing type
- scripts
    - to eas the handling of the multiple modules we created seperate scripts file for each of the module which are called by using the respective argument when running the main file
- src
    - the code modules for the different functionalities

├── data     
│   └── run0.csv  
│   └── run1.csv  
├── scripts  
│   └── annotator.py  
│   └── scrapper.py  
│   └── trainer.py  
