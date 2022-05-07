<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __Animalia__ #
Irene Rengifo - Final Project - Data Analytics Part-Time Bootcamp - Nov 2021 - Ironhack Madrid

## **Goal** ##
My goal was to be able to provide information about animals regarding their habitat, red list category, location regions and threats that could put their survival at risk. For this project my main question was to know within an specific group of animals which are in a more vulnerable position. 

I decided to use [phylum Chordata](https://es.wikipedia.org/wiki/Chordata) 

The animals of the phylum Chordata consists of animals with a flexible rod supporting their dorsal or back sides. The phylum name derives from the Greek root word chord- meaning string. Most species within the phylum Chordata are vertebrates, or animals with backbones (subphylum Vertebrata).

*Animals classes within the Chordata phylum*:  
- Mammalia (mamíferos)
- Aves
- Actinopterygii (peces óseos)  
- Amphibia (anfibios)  
- Cephalaspidomorphi (peces sin mandibula)  
- Chondrichthyes (peces vertebranos cartilaginosos)  
- Myxini (peces agnatos)  
- Reptilia (reptiles)  
- Sarcopterygii (peces de aletas carnosas)

![image](https://www.carlsonstockart.com/images/xl/Chordate-Famly-Tree.jpg)

## **Overview** ##
### **Data Exploration and Preparation.** ### 

My goal was to be able to  is to perform an exploratory analysis in order to gain initial insight on the animal database and prepare the data to try to answer my question and create a simple visualization.

#### **Data Collection** ####
The website [IUCN Red List](https://www.iucnredlist.org) was the based for my project. I had several challenges to collect the data as I was not granted API access and the data is not easily identifiable. I finally ended up downloading the information in zip format directly from the page by making several searches with parameters and then manually extracting the csv files and manipulating them in order to identify each one. 
I used approximately 50 or more csv for this project.

For me the data collection phase was the most challenging one in this project.

![image](https://i.gifer.com/embedded/download/9nLP.gif)

#### **Exploratory Analysis** ####
I did my data analysis using jupyter notebook. I decided to work with several dataframes in order to be able to analyze in more detail all the information available, as some animals are located in more than one region or live in several habitats, so in order to avoid duplicates, I worked with information separately.  

I cleaned the datasets to ensure the data was named equally in all and then created a new column "Total_id" joining the value of two existing columns in order to create a unique value for each animal, by doing this I then proceeded to merge each dataset (Habitats, Land_Regions, Marine_Regions & Threats) with the complete list of animals available.  

By doing this, the user is able to make a very detailed search with several option that he has at hand. 

### **Dashboard and Reporting** ### 

I created a dashboard prototype that is intended to be user friendly, and simple enough that the user can understand easily the most important information.

Animalia will return either:
1. CSV with detailed information based on your selection. 
2. Displaying the information in the terminal and in some cases it will a web browser tab with more information about the selected animal.

![image](https://raw.githubusercontent.com/Irene9R/ih_datamadpt1121_final_project/main/imagenes/tableau_statistics.jpg)


## **Project Main Stack**

 
- [Tableau Public](https://public.tableau.com/en-us/s/) 
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
- [Time](https://docs.python.org/3/library/time.html)
- [warnings](https://docs.python.org/es/3/library/warnings.html)
- [webbrowser](https://docs.python.org/es/3/library/webbrowser.html)
- [Argparse](https://docs.python.org/3/library/argparse.html)



## **How to access Animalia and Tableu Public Visualizations**  

Enter your terminal and access the directory in which you saved the app.
You are all set to run Animalia.py. Please read the --help option in order to get displayed all possible options. You can access this option by typing in your terminal the following command:

python Animalia.py -h

 -n {several class choices available}              returns information of species scientific name and red list by category class.  
  -c {several red list category choices available}             returns information of species name and red list category by class.   
  -l, --list            displays a list of all species available in the data.  
  -s, --specific_species
                        displays red list category, habitat, land region and/or marine region,threats and more information regarding a selected single species.  
  -a {several habitat choices available}       displays species in selected habitat.  
  -r {several land region choices}
                        displays species in selected land region.  
  -m {several marine_regions choices available} 
                        displays species in selected marine region.  
  -t {several threat choices available} 
                        displays species affected by selected threat.  
 
Using arsparse was the most challenging part of the coding and I have learned how to used it:

![image](https://github.com/Irene9R/ih_datamadpt1121_final_project/blob/main/imagenes/argparse.jpg?raw=true)

After some seconds, you will be provided with the information  and the following message on your terminal:
"This information has also been saved as a CSV document in 'data/report_output' folder."

[Tableau Public - Visualization Story](https://public.tableau.com/app/profile/irene1690/viz/RedlistCategoryandAnimaliaChordataStatistics/REDLISTCATEGORYANDANIMALIACHORDATASTATISTICS?publish=yes)



## **Conclusions** #

Some Insights: 
1.	Around 23% of the species that are part on the Chordata Physlum are at risk. 
2.	40% of the already extint species were Birds(Aves).
3.	From today's critically endangered species around 29% are Amphibia (anfibios) and 28% are Actinopterygii (peces vertebrados) 

Future improvements:  
1. Cleaning my code by implementing modules and creating a pipeline.
2. Find a way to make data acquisition process automatic.
3. Implement Streamlit
4. Make visualizations for all the different data-sets that I have to get insights as to regions that have more animals at risk and analyze the threats that they are subject to. 


## **Please remember to do your part  to save the planet and all it's inhabitants.** ##

# WE DID IT!!!!

![Image](https://c.tenor.com/p662RWbCxJAAAAAd/ead-formatura.gif)































