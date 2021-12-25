## Explanation about the code ##

class DataInfo
##
Class to keep the information of the data.
safety_reports is a list of dictionaries,each element in the list represents the information of a safety report.
feature_names is a list of the feature names.
labels is a np.array of the labels.
##

class DataDrugs
##
Class to keep information that is relevant for the drugs features.
list_of_drugs_route is a list of new drug names (after renaming).
unit_dict is eventually a dictionary that the drug names are the keys and the values are a 
list of the most frequent units.
dose_dict is eventually a dictionary that the drug names are the keys and the values are a 
counter dict of the dose numbers.
##

class DataOutiers
##
Class to keep information that is relevant for the ouliers removal.
countries is a list of all the countries in the data (with repeats).
eports_to_remove is a lost of indexes of reports that we will remove before the modeling.
##

def drug_reading(root: ET.Element, data_drugs: DataDrugs) -> dict
##
Treats the "drug" field.
Each report consists of many of drugs and each drug has many subfields.
For each drug field we change the "medicinalproduct" subfield to it's first word and concatenate 
the "drugadministrationroute" subfield value, if "drugadministrationroute" subfield does not exist 
in the drug field we concatenate "other" instead.
Moreover, we delet drugs that don't have both "drugstructuredosagenumb" and "drugstructuredosageunit" 
subfields because the drug is not informative if it doesn't have dosage.
Eventually we keep the information of the fields: "medicinalproduct","drugstructuredosagenumb",
"drugstructuredosageunit" in a dictionary. The function returns the dictionary with the information of
the current drug field.
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
The function converts the age from representations as decade, month, week, day, hour to year. 
##

def treat_safety_report(root: ET.Element, data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers):
##
The function gets a root of a safety report and it saves its information in a dictionary.
For the "drug" field, it creates a list of dictionaries, using the function drug_reading.
For the "reaction" field, the function saves the most severe reaction outcome,using the function reaction_handling.
For the "patientonsetage", "patientweight" and "serious" fields, the function saves the value as a float type.
For the "patientonsetageunit" field, the function converts the age using the function change_age_unit function.
For the "occurcountry" field, the function saves the text of the field as a value.
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
The function removes from the given list the empty dicts.
##

def keep_high_freq_drugs(data_info: DataInfo, data_drugs: DataDrugs) -> list:
##
The function counts the frequencies of drug names and for each report, saves only
the drug names that appear in more than 3 reports. The function call the function
remove_empty_dicts to delete drugs. The function returns a list of the remained drugs.
##

def convert_unit(drug: dict)
##
The function makes some convertions for dose units, according to the FDA website:
https://admin.ich.org/sites/default/files/inline-files/ICH_ICSR_Specification_V2-3.pdf
##

def dose_unit_dict(data_info: DataInfo, data_drugs: DataDrugs, field_name: str) -> dict
##
The function creates a dictionary, that its keys are drug names and its values are a 
counter dict of the values of the given field_name in the data.
##

def keep_most_freq_units(unit_dict: dict)
##
The function keeps up to 3 most frequent units for each drug.
##

def remove_unfrequent_unit(data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers)
##
The function calls keep_most_freq_units function, and according to its result, it removes
unfrequent units for each drug.
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
The function uses counter dict to calculate the frequency of each country in the reports,
and than it removes reports that its frequency is less than 4.
##

def reading_the_data(data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers)
##
The function reads the XML files containing the data, for each file it creates an Element Tree,
and for each safety report it calls the function treat_safety_report.
##

def drug_handling(data_info: DataInfo, data_drugs: DataDrugs, data_outliers: DataOutliers)
##
The function calls al the functions that treats the drugs information.
##
