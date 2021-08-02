# Scientific Python - Final Project

## ToDo:
### SCRAPPER
- [ ] Reding of the config file and creating the respective url
- [ ] Iterating trough the pages 
    - [ ] Handling min and max amount of articles to read
    - [ ] Implementing a stop criteria
- [ ] Complete the category and size ids

## VISUALIZATION
- [ ] Plotting the different attributes according to clothing type
- [ ] Comparing availability between genders 
- [ ] Plot the color diversity between genders
- ...

## ANNOTATOR
- [ ] Create the annotation page
    - [ ] DS handling
    - [ ] Ajax interactions
- ...


## Short description
This project will contain an interactive **web scrapper** with an **user intafece** based on the browser where the use will be able to filter their search and **annotate** the scrapped data. However the scrapper will only work on the webstore of Vinted.com.

## Requirements
For the scrapper to run 

Install python requirements using pip:  
```pip install -r requirements.txt```  

Create conda env using:  
```conda env create -f environment.yml ```

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

## Functionalities

### Scrapper
given the arguments the scrapper will generate a scv file containing the values specified in the articles while a second hdf5 file containing the image values will be generated to
