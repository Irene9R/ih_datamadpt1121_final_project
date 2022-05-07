#Imports
import time
import pandas as pd
import numpy as np
from functools import reduce
from os import listdir
from os.path import isfile, join
import warnings
from tabulate import tabulate
import time
import argparse
import webbrowser
warnings.filterwarnings('ignore')

pd.set_option('display.width',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)

#Variables

list_of_id_columns = ["internalTaxonId", "assessmentId"]
joined_column_name = 'total_id'
on_column = "internalTaxonId"
url = "https://www.iucnredlist.org/species/"
columns = ["assessmentId","internalTaxonId","yearPublished"]

#Mammalia - mamíferos
path_mammalia = "data/animalia_chordata/mammalia/"
#Aves
path_aves1 = "data/animalia_chordata/aves/aves1/"
path_aves2 = "data/animalia_chordata/aves/aves2/"
#Actinopterygii - peces óseos
path_actinopterygii = "data/animalia_chordata/actinopterygii/"
#Amphibia - anfibios
path_amphibia = "data/animalia_chordata/amphibia/"
#Cephalaspidomorphi - peces sin mandibula
path_cephalaspidomorphi = "data/animalia_chordata/cephalaspidomorphi/"
#Chondrichthyes - peces vertebranos cartilaginosos
path_chondrichthyes = "data/animalia_chordata/chondrichthyes/"
#Myxini - peces agnatos
path_myxini = "data/animalia_chordata/myxini/"
#Reptilia - reptiles
path_reptilia = "data/animalia_chordata/reptilia/"
#Sarcopterygii - peces de aletas carnosas
path_sarcopterygii = "data/animalia_chordata/sarcopterygii/"

#Animals
columns_animalia_chordata_complete = ["total_id",
                                      "scientificName_x",
                                      "kingdomName",
                                      "phylumName",
                                      "className",
                                      "orderName",
                                      "familyName",
                                      "redlistCategory",
                                      "systems",
                                      "realm",
                                      "url"]
columns_animalia_chordata_user = ["scientificName",
                                  "className",
                                  "orderName",
                                  "familyName",
                                  "redlistCategory",
                                  "systems",
                                  "realm",
                                  "url"]
#Threats
path_threats = 'data/threats/'
column_name_threats = "threat"
column_name_threats1 = "sub-threat"
columns_threats_list = ["total_id",
                        "scientificName",
                        "kingdomName",
                        "phylumName",
                        "className",
                        "orderName",
                        "familyName",
                        "redlistCategory_x",
                        "systems_x",
                        "threat",
                        "sub-threat",
                        "realm_x",
                        "url"]
old_value = "_"
new_value = " "
old_value1 = "."
new_value1 = "-"
old_value2 = "("
new_value2 = "/"
new_columns_list = ["threat","sub-threat"]
separator = "-"

#Habitats
path_habitats = 'data/habitats/'
column_name_habitats = "habitats"
columns_habitats_list = ["total_id",
                         "scientificName_x",
                         "kingdomName",
                         "phylumName",
                         "className",
                         "orderName",
                         "familyName",
                         "redlistCategory_x",
                         "systems_x",
                         "habitats",
                         "realm_x",
                         "url"]

#Land_Regions
path_land_regions = 'data/land_regions/'
column_name_land_regions = "land_regions"
columns_land_regions_list = ["total_id",
                                 "scientificName_x",
                                 "kingdomName",
                                 "phylumName",
                                 "className",
                                 "orderName",
                                 "familyName",
                                 "redlistCategory_x",
                                 "land_regions",
                                 "url"]

#Marine_Regions
path_marine_regions = 'data/marine_regions/'
column_name_marine_regions = "marine_regions"
columns_marine_regions_list = ["total_id",
                                   "scientificName_x",
                                   "kingdomName",
                                   "phylumName",
                                   "className",
                                   "orderName",
                                   "familyName",
                                   "redlistCategory_x",
                                   "marine_regions",
                                   "url"]


#Saving_reports
path1_csv = "data/final_report_animalia.csv"
path2_csv = "data/final_report_threats.csv"
path3_csv = "data/final_report_habitats.csv"
path4_csv = "data/final_report_land_regions.csv"
path5_csv = "data/final_report_marine_regions.csv"
path6_csv = "data/user_report_animalia.csv"


#Funciones

def data_adquisition_csv(path):
    #function to retrieve the information from a csv file stored locally.  
    imported_df = pd.read_csv(path)
    return imported_df

def import_files_from_directory_with_file_name_column_into_list(directory_path,column_name):
    files_list = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
    df_list = []
    for i in files_list:
        df = pd.read_csv(directory_path + i)
        df[column_name] = i
        df[column_name] = df[column_name].str[:-4]
        df_list.append(df)
    return df_list

def import_files_from_directory_into_list(directory_path):
    files_list = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
    df_list = []
    for i in files_list:
        df = pd.read_csv(directory_path + i)
        df_list.append(df)
    return df_list

def convert_column_float_to_int(df,columns):
    df[columns] = df[columns].astype(int)

def merge_df_list (on_column,df_list):
    df = reduce(lambda x, y: pd.merge(x, y, on = on_column), df_list)
    return df

def merge_dfs(df1,df2,on_column):
    df = pd.merge(df1,df2,on= on_column)
    return df

def clean_column_names(df):
    df = df.rename(lambda x: x[:-2] if '_x' in x else x, axis=1)
    return df

def cleaning_non_numerical_id_rows(df,list_of_id_columns):
    df[list_of_id_columns].applymap(lambda x: str(x).isdigit())
    return df

def removing_extra_columns(df,list_columns_to_keep):
    df = df[list_columns_to_keep]
    return df

def adding_new_column_with_specific_value(df,new_column_name,value):
    df[new_column_name] = value
    return df

def joining_columns(df,new_column_name,concat_cols):
    df[new_column_name] = df[concat_cols].apply(lambda row: '/'.join(row.values.astype(str)), axis=1)
    
def cleaning_column_values(df,column,old_value,new_value):
    df[column] = df[column].str.replace(old_value,new_value)
    df[column] = df[column].str.title()
    
def separate_column_in_two(df,column_to_separate,new_columns_list,separator):
    df[new_columns_list] = df[column_to_separate].str.split(separator,expand=True)
    return df

def save_data_to_csv (df,path):
    df.to_csv(path, index=False)

def class_adquisition(path,on_column):
    fun_list = import_files_from_directory_into_list(path)
    df = merge_df_list (on_column,fun_list)
    return df

def creation_of_animalia_df(list_of_id_columns):
    mammalia = class_adquisition(path_mammalia,on_column)
    aves1 = class_adquisition(path_aves1,on_column)
    aves2 = class_adquisition(path_aves2,on_column)
    actinopterygii = class_adquisition(path_actinopterygii,on_column)
    amphibia = class_adquisition(path_amphibia,on_column)
    cephalaspidomorphi = class_adquisition(path_cephalaspidomorphi,on_column)
    chondrichthyes = class_adquisition(path_chondrichthyes,on_column)
    myxini = class_adquisition(path_myxini,on_column)
    reptilia = class_adquisition(path_reptilia,on_column)
    sarcopterygii = class_adquisition(path_sarcopterygii,on_column)
    animalia_df_list = [mammalia,aves1,aves2,actinopterygii,reptilia,
                    amphibia,chondrichthyes,myxini,cephalaspidomorphi,sarcopterygii]
    animalia_chordata_df = pd.concat(animalia_df_list)
    joining_columns(animalia_chordata_df,joined_column_name,list_of_id_columns)
    animalia_chordata_df["url"] = url + animalia_chordata_df[joined_column_name]
    return animalia_chordata_df
    
def saving_cleaned_chordata_df (df,path1,path2):
    animalia_chordata_final_df = df[columns_animalia_chordata_complete]
    animalia_chordata_final_df = clean_column_names(animalia_chordata_final_df)
    save_data_to_csv(animalia_chordata_final_df,path1)
    animalia_chordata_final_user = animalia_chordata_final_df[columns_animalia_chordata_user]
    animalia_chordata_final_user = animalia_chordata_final_user.reset_index(drop=True)
    save_data_to_csv(animalia_chordata_final_user,path2)
    return animalia_chordata_final_user

def creation_of_threats_df (df,path):
    df_threats = import_files_from_directory_with_file_name_column_into_list(path_threats,column_name_threats)
    threats = pd.concat(df_threats)
    convert_column_float_to_int(threats,columns)
    threats = cleaning_non_numerical_id_rows(threats,list_of_id_columns)
    joining_columns(threats,joined_column_name,list_of_id_columns)
    cleaning_column_values(threats,column_name_threats,old_value,new_value)
    separate_column_in_two(threats,column_name_threats,new_columns_list,separator)
    cleaning_column_values(threats,column_name_threats1,old_value1,new_value1)
    cleaning_column_values(threats,column_name_threats1,old_value2,new_value2)
    threats_complete = merge_dfs(threats,df,joined_column_name)
    threats_complete = removing_extra_columns(threats_complete,columns_threats_list)
    threats_complete = clean_column_names(threats_complete)
    save_data_to_csv(threats_complete,path)
    return threats_complete

def creating_of_df(path,column_name,df1,column_list,path1):
    df_list = import_files_from_directory_with_file_name_column_into_list(path,column_name)
    df = pd.concat(df_list)
    df = cleaning_non_numerical_id_rows(df,list_of_id_columns)
    joining_columns(df,joined_column_name,list_of_id_columns)
    cleaning_column_values(df,column_name,old_value,new_value)
    df_complete = merge_dfs(df,df1,joined_column_name)
    df_complete = removing_extra_columns(df_complete,column_list)
    df_complete = clean_column_names(df_complete)
    save_data_to_csv(df_complete,path1)
    return df_complete

# Variables argparse
classes = ['MAMMALIA', 'AVES', 'ACTINOPTERYGII', 'REPTILIA', 'AMPHIBIA','CHONDRICHTHYES', 'MYXINI', 'CEPHALASPIDOMORPHI', 'SARCOPTERYGII']
category = ['Least_Concern', 'Vulnerable','Data_Deficient','Critically_Endangered', 'Endangered', 'Extinct','Near_Threatened',
'Extinct_in_the_Wild','Lower_Risk/near_threatened', 'Lower_Risk/least_concern','Lower_Risk/conservation_dependent']
habitat = ['Artificial_Aquatic_And_Marine', 'Forest', 'Wetlands_Inland','Marine_Intertidal','Artificial_Terrestrial', 'Grassland',
'Shrubland', 'Marine_Coastalsupratidal','Marine_Neritic','Desert', 'Rocky_Areas','Savanna','Marine_Oceanic', 'Introduced_Vegetation',
 'Other','Caves_And_Subterranean_Habitats_Non-Aquatic', 'Unknown','Marine_Deep_Benthic'] 
land = ['Antarctic', 'Caribbean_Islands', 'Europe', 'North_Africa','North_America', 'Oceania', 'South_America', 'Sub_Saharan_Africa',
'East_Asia', 'South_Southeast_Asia', 'West_And_Central_Asia','Mesoamerica', 'North_Asia']
marine = ['Antarctic_Western_Central', 'Atlantic_Eastern_Central','Atlantic_Northeast', 'Atlantic_Northwest', 'Atlantic_Southeast',
'Atlantic_Southwest', 'Indian_Ocean_Eastern','Indian_Ocean_Western', 'Mediterranean_And_Black_Sea','Pacific_Eastern_Central',
 'Pacific_Northeast','Pacific_Northwest', 'Pacific_Southeast', 'Pacific_Southwest','Pacific_Western_Central', 'Atlantic_Antarctic',
 'Indian_Ocean_Antarctic', 'Arctic_Sea', 'Pacific_Antarctic']
threat = ['Agriculture_And_Aquaculture','Natural_System_Modifications', 'Pollution','Biological_Resource_Use',
'Climate_Change_And_Severe_Weather','Energy_Production_And_Mining','Residential_And_Comercial_Development',
'Transportation_And_Service_Corridors','Human_Intrusions_And_Disturbance', 'Other_Options','Geological_Events',
'Invasive_And_Other_Problematic_Species_Genes_And_Diseases']

# Argument parser function
def argument_parser():
    parser = argparse.ArgumentParser (description="Welcome to Animalia!!!")
    parser.add_argument("-n", "--class_name", action='store',type = str, required = False,choices = classes,help ="returns information of species name and red list category by class.")
    parser.add_argument("-c", "--red_list_category", action='store',type = str, required = False, choices = category, help ="returns information of species name and red list category by class.")
    parser.add_argument("-l", "--list", action = "store_true", help ="displays a list of all species available in the data.")
    parser.add_argument("-s", "--specific_species", action="store_true", help = "displays red list category, habitat, land region and/or marine region,threats and more information regarding a selected sigle species.")
    parser.add_argument("-a", "--habitats", action='store',type = str, required = False, choices= habitat ,help = "displays species in selected habitat.")
    parser.add_argument("-r", "--land_regions", action='store',type = str, required = False, choices= land , help = "displays species in selected land region.")
    parser.add_argument("-m", "--marine_regions", action='store',type = str, required = False, choices= marine , help = "displays species in selected marine region.")
    parser.add_argument("-t", "--threats", action='store',type = str, required = False, choices= threat, help = "displays species affected by selected threat.") 
    args = parser.parse_args()
    return args


#Main pipeline function:                 

def main(arguments):
    if arguments.list:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        print("The list of the species in data is: ")
        print((animalia_chordata_final_user["scientificName"]))
        save_data_to_csv(animalia_chordata_final_user,'data/report_output/report.csv')
        print("Remember to do you part to save the planet and all it's inhabitants!!")
    elif arguments.class_name:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.class_name = arguments.class_name.replace(old_value, new_value)
        print("The species within the selected class:")
        chordata_user = animalia_chordata_final_user.loc[animalia_chordata_final_user["className"] == arguments.class_name]
        save_data_to_csv(chordata_user,'data/report_output/report.csv')
        print (tabulate(chordata_user))
        print ("This information has also been saved as a CSV document in 'data/report_output' folder.")
        time.sleep(3)
        webbrowser.open("https://public.tableau.com/app/profile/irene1690/viz/RedlistCategoryandAnimaliaChordataStatistics/REDLISTCATEGORYANDANIMALIACHORDATASTATISTICS?publish=yes",new=2)
        print ("Remember to do you part to save the planet and all it's inhabitants!!")
    elif arguments.red_list_category:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.red_list_category = arguments.red_list_category.replace(old_value, new_value)
        print("Species within the selected red category:")
        arguments.red_list_category = arguments.red_list_category.title()
        animalia_chordata_final_user["redlistCategory"] = animalia_chordata_final_user['redlistCategory'].str.title()
        red_list_user = animalia_chordata_final_user.loc[animalia_chordata_final_user["redlistCategory"] == arguments.red_list_category]
        save_data_to_csv(red_list_user,'data/report_output/report.csv')
        print (tabulate(red_list_user))
        print ("This information has also been saved as a CSV document in 'data/report_output' folder.")
        time.sleep(3)
        webbrowser.open("https://public.tableau.com/app/profile/irene1690/viz/RedlistCategoryandAnimaliaChordataStatistics/REDLISTCATEGORYANDANIMALIACHORDATASTATISTICS?publish=yes",new=2)
        print ("Remember to do you part to save the planet and all it's inhabitants!!!!")
    elif arguments.habitats:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.habitats = arguments.habitats.replace(old_value, new_value)
        habitats_complete = creating_of_df(path_habitats,column_name_habitats,animalia_chordata_df,columns_habitats_list,path3_csv)
        print("The following species are found in the selected habitat:")
        habitats_user = habitats_complete.loc[habitats_complete["habitats"] == arguments.habitats]
        habitats_user = habitats_user.reset_index(drop=True)
        save_data_to_csv(habitats_user,'data/report_output/report.csv')
        print (tabulate(habitats_user))
        print ("This information has also been saved as a CSV document in 'data/report_output' folder.")
        print ("Remember to do you part to save the planet and all it's inhabitants!!")
    elif arguments.land_regions:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.land_regions = arguments.land_regions.replace(old_value, new_value)
        land_regions_complete = creating_of_df(path_land_regions,column_name_land_regions,animalia_chordata_df,columns_land_regions_list,path4_csv)
        print("Species found in the selected land region:")
        land_regions_user = land_regions_complete.loc[land_regions_complete['land_regions']==arguments.land_regions]
        land_regions_user = land_regions_user.reset_index(drop=True)
        save_data_to_csv(land_regions_user,'data/report_output/report.csv')
        print (tabulate(land_regions_user))
        print ("This information has also been saved as a CSV document in 'data/report_output' folder.")
        print ("Remember to do you part to save the planet and all it's inhabitants!!!!")
    elif arguments.marine_regions:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.marine_regions = arguments.marine_regions.replace(old_value, new_value)
        marine_regions_complete = creating_of_df(path_marine_regions,column_name_marine_regions,animalia_chordata_df,columns_marine_regions_list,path5_csv)
        print("Species found in the selected marine region:")
        marine_regions_user = marine_regions_complete.loc[marine_regions_complete['marine_regions']==arguments.marine_regions]
        save_data_to_csv(marine_regions_user,'data/report_output/report.csv')
        print (tabulate(marine_regions_user))
        print ("This information has also been saved as a CSV document in 'data/report_output' folder.")
        print ("Remember to do you part to save the planet and all it's inhabitants!!")
    elif arguments.threats:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        arguments.threats = arguments.threats.replace(old_value, new_value)
        threats_complete = creation_of_threats_df(animalia_chordata_df,path2_csv)
        print("Species affected by the selected threat group:")
        threats_user = threats_complete.loc[threats_complete['threat']== arguments.threats]
        save_data_to_csv(threats_user,'data/report_output/report.csv')
        print (tabulate(threats_user))
        print ("This information has also been saved as a CSV document in 'data/report_outpu' folder.")
        print ("Remember to do you part to save the planet and all it's inhabitants!!!!")
    elif arguments.specific_species:
        animalia_chordata_df = creation_of_animalia_df(list_of_id_columns)
        animalia_chordata_final_user = saving_cleaned_chordata_df (animalia_chordata_df,path1_csv,path6_csv)
        habitats_complete = creating_of_df(path_habitats,column_name_habitats,animalia_chordata_df,columns_habitats_list,path3_csv)
        land_regions_complete = creating_of_df(path_land_regions,column_name_land_regions,animalia_chordata_df,columns_land_regions_list,path4_csv)
        marine_regions_complete = creating_of_df(path_marine_regions,column_name_marine_regions,animalia_chordata_df,columns_marine_regions_list,path5_csv)
        threats_complete = creation_of_threats_df(animalia_chordata_df,path2_csv)
        scientific_name = str(input("Please enter the scientific name of the species from which you would like to have more details: "))
        scientific_name = scientific_name.title()
        animalia_chordata_df["scientificName_x"] = animalia_chordata_df["scientificName_x"].str.title()
        specific_id = animalia_chordata_df["total_id"].loc[animalia_chordata_df["scientificName_x"] == scientific_name]
        specific_id = specific_id.values[0]
        print ("The habitat(s) of ", scientific_name,"is/are: ")
        habitats_user = habitats_complete['habitats'].loc[habitats_complete['total_id']== specific_id]
        habitats_user = habitats_user.reset_index(drop=True)
        print (tabulate(habitats_user))
        print ("The land region(s) where the", scientific_name,"can be found (if aplicable) is/are: ")
        land_regions_user = land_regions_complete['land_regions'].loc[land_regions_complete['total_id']== specific_id]
        land_regions_user = land_regions_user.reset_index(drop=True)
        print (tabulate(land_regions_user))
        print ("The marine region(s) where the", scientific_name,"can be found (if aplicable) is/are: ")
        marine_regions_user = marine_regions_complete['marine_regions'].loc[marine_regions_complete['total_id']== specific_id]
        marine_regions_user = marine_regions_user.reset_index(drop=True)
        print (tabulate(marine_regions_user))
        print ("The threat(s) affecting the", scientific_name," (if aplicable) is/are: ")
        threats_user = threats_complete[['threat','sub-threat']].loc[threats_complete['total_id']== specific_id]
        threats_user = threats_user.reset_index(drop=True)
        print (tabulate(threats_user))
        time.sleep(3)
        webbrowser.open(animalia_chordata_df[animalia_chordata_df['total_id'] == specific_id]['url'].values[0],new=2)
        print ("Remember to do you part to save the planet and all it's inhabitants!!!!")
    else:
        print ("incorrect or no command entered, please review the help command for all options available -h")  




if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)