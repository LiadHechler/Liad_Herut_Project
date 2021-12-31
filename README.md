## Explanation about the code ##

class DataInfo
##
Class to keep the information of the train data.
safety_reports is a list of dictionaries, each element in the list represents the information of a safety report. After the preprocessing, it is being changed to a list of np.arrays.
feature_names is a list of the feature names.
labels is a np.array of the labels.
##

class DataValid
##
Class to keep the information of the validation data.
##

class DataTest
##
Class to keep the information of the test data.
##

class DataDrugs
##
Class to keep information that is relevant for the drugs features.
list_of_drugs_route is a list of new drug names (after renaming).
list_of_remained_drugs os a list of the drugs that we keep. It starts as a set and later being changed to a list.
unit_dict is eventually a dictionary that the drug names are the keys and the values are a 
list of the most frequent units.
dose_dict is eventually a dictionary that the drug names are the keys and the values are a 
counter dict of the dose numbers.
##

class DataPreProcessing
##
Class to keep information that is relevant for the preprocessing.
countries is a list of all the countries in the data (with repeats).
reports_to_remove is a list of indexes of reports that we will remove before the modelling part.
average_age is a dictionary for the average age for each age group and the total average.
average_weight is a dictionary for the average weight for each age group and the total average.
major_serious, major_serious_hosp, major_fulfill_exp and major_report_type are dictionaries for the frequency of each field’s values. We use itto find the value of the majority.
##

def drug_reading(root: ET.Element, data_drugs: DataDrugs) -> dict
##
Treats the "drug" field.
Each report consists of many of drugs and each drug has many subfields.
For each drug field we change the "medicinalproduct" subfield to it's first word and concatenate 
the "drugadministrationroute" subfield value. If "drugadministrationroute" subfield does not exist,  we concatenate "other" instead.
Moreover, we remove drugs that don't have both "drugstructuredosagenumb" and "drugstructuredosageunit" subfields, because the drug is not informative if it doesn't have dosage.
Eventually, we keep the information of the fields: "medicinalproduct","drugstructuredosagenumb",
"drugstructuredosageunit" in a dictionary. The function returns the dictionary with the information of the current drug field.
##

def most_severe_reaction_func(root: ET.Element, most_severe: str) -> str:
##
Function to save the most severe reaction outcome for every report.
##

def make_reaction_binary(most_severe_reaction: str) -> int
##
The function returns the binary label (1/0) for the field "reaction".
##

def change_age_unit(text: str, report: dict):
##
The function converts the age from representations as decade, month, week, day and hour to representation as a year. 
##

def treat_safety_report(root: ET.Element, data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers):
##
The function gets a root of a safety report and it saves its information in a dictionary.
•	For the "drug" field, it creates a list of dictionaries, using the function drug_reading.
•	For the "reaction" field, the function saves the most severe reaction outcome, using the function reaction_handling.
•	For the "patientonsetage", "patientweight" fields, the function saves the values as float types.
•	For the "patientonsetageunit" field, the function converts the age using the function change_age_unit function.
•	For the “patientagegroup” field, it saves the value as a string.
•	For the fields: “patientsex”, “serious”, “seriousnesshospitalization” and “fulfillexpeditecriteria”, the function saves binary values.
•	For the “reporttype field”, the function saves its values as integers.
•	For the "occurcountry" field, the function saves the text of the field as a value.
##

def plot_route_graph(sort_route: list, sort_route_values: list)
##
The function calculates the value of 1% of the total number of routes.
Then it plots the routes that have more than 1% of total routes and its frequencies.
It helped us to determine which routes we will use to describe the drugs' names. (function rename_drug)
NOTE: the route "065", which has the highest frequency is "unknown".
##

def remove_empty_dicts(lst: list)
##
The function removes empty dictionaries from a given list.
##

def keep_high_freq_drugs(data_info: DataInfo, data_drugs: DataDrugs)
##
For each report , the function saves only the drug names that appear in more than 3 reports. The function calls the function remove_empty_dicts to remove empty drugs. The function also updates the list of the remained drugs.
##

def convert_unit(drug: dict)
##
The function makes some conversions for dose units, according to the FDA website:
https://admin.ich.org/sites/default/files/inline-files/ICH_ICSR_Specification_V2-3.pdf
##

def create_dose_dict (data_info: DataInfo, data_drugs: DataDrugs)
##
The function creates a dictionary, that its keys are drug names and its values are a 
counter dict of the values of “drugstructuredosagenumb” field in the data.
##

def calc_relative_dosage(dose_counter: Counter, dosage: float) -> float
##
The function calculates for a given dosage in a specific drug its relative value:
the number of all the dosages that are equal or less to it, divided by the total number of dosages.
##

def change_drugs_field(data_info: DataInfo, dose_dict: dict, list_of_remained_drugs: list)
##
The function saves in each report its drug names as keys and the drugs' relative
dosages as values.
In addition, it adds to each report the drugs that are missing in the report, 
with the value 0.
##

def countries_outliers(data_info: DataInfo, data_outliers: DataOutliers)
##
The function uses counter dictionary to calculate the frequency of each country in the reports,
and then it removes reports that its occur country appears less than 4 times in the data.
In addition, the function adds to each report the countries that are missing in the report, 
with the value 0. I.e., creates dummy variables for the country feature.
##

def reading_the_data(report: dict, data_preprocessing: DataPreProcessing)
##
The function reads the XML files containing the data, for each file it creates an Element Tree,
and for each safety report it calls the function treat_safety_report.
##

def info_age_avg(report: dict, data_preprocessing: DataPreProcessing)
##
For each age group, the function sums all the ages and counts how many ages are in the age group. This information will be used for calculating the average age in each age group and the total average.
##

def info_weight_avg(report: dict, data_preprocessing: DataPreProcessing)
##
For each age group, the function sums all the weights and counts how many weights are in the age group. This information will be used for calculating the average weight in each age group and the total average.
##

def info_majority(report: dict, data_preprocessing: DataPreProcessing)
##
The function saves the frequencies of each value of the fields: “patientsex”, “serious”, “seriousnesshospitalization”, “fulfillexpeditecriteria” and “reporttype”.
##

def calc_avg_and_majority(data_info: DataInfo, data_preprocessing: DataPreProcessing)
##
The function calculates the weight and age averages for each age group and the total averages.
On addition, it finds the most frequent value in each of the fields: “patientsex”, “serious”, “seriousnesshospitalization”, “fulfillexpeditecriteria” and “reporttype”.
##

def fill_by_avg(report: dict, data_preprocessing: DataPreProcessing)
##
The function fills empty cells in the data with relevant average.
##

def fill_by_majority(report: dict, data_preprocessing: DataPreProcessing)
##
The function fills empty cells in the data with the value of the majority.
##

def fill_empty_features(data_info: DataInfo, data_preprocessing: DataPreProcessing)
##
The function alls the function calc_avg_and_majority.
For each report, it calls the functions: fill_by_avg and fill_by_majority.
##

def drug_handling(data_info: DataInfo, data_drugs: DataDrugs, data_preprocessing: DataPreProcessing)
##
The function calls al the functions that treats the drugs information.
##

def model_data(data_info: DataInfo)
##
The function saves the data as list of np.arrays. It also saves the labels in a np.array and the feature names in a list.
##

def normalize_data(data: list) -> list
##
The function normalizes a given data using StandardScaler().
##

def minmax_scaling(data: list) -> list
##
The function scales a given data using MinMaxScaler().
##

def pca(data: list) -> list
##
The function reduces the dimensionality of the data, using PCA method.
##






Functions that we didn’t use eventually:
def keep_most_freq_units(unit_dict: dict)
##
The function keeps up to 3 most frequent units for each drug.
##

def remove_unfrequent_unit(data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers)
##
The function calls keep_most_freq_units function, and according to its result, it removes
unfrequent units for each drug.
##
