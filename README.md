## Explanation about the code ##

class data
##
Class to keep the information of the data.
safety_reports is a list of dictionaries,
each element in the list represents the information of a safety report.
bag_of_drugs is a dictionary- each key is a name of a drug,
                            each value is the frequency of this drug.
bag_of_route is a dictionary- each key is a route of administration code,
                            each value is the frequency of this route.
##

def drug_route_freq(curr_d: dict, item: ET.Element, data_info: data)
##
Updates the data_info.bag_of_drugs dictionary, each key is a name of a drug
and each value is the frequency of this drug in the safety reports.
A name of a drug in the dictionary is the first word of the name of the drug in the report.

Updates the data_info.bag_of_route dictionary, each key is a route of administration code
and each value is the frequancy of this route in the safety reports.

We save the dictionaries as attributes in the data class.
##

def drug_handling(root: ET.Element, bag_of_drugs: dict) -> dict
##
Treats the "drug" field.
Each report consists of many of drugs and each drug has many sub-fields,
so we keep the information of the fields: "medicinalproduct","drugadministrationroute","drugstructuredosagenumb","drugstructuredosageunit" in a dictionary.
The function returns the dictionary with the information of the current drug field.
##

def most_severe_reaction_func(root: ET.Element, most_severe: str) -> str:
##
Function to save the most severe reaction outcome for every report.
##

def make_reaction_binary(most_severe_reaction: str) -> int
##
The function returns the binary label (1/0) for the field "reaction".
##

def treat_safety_report(root: ET.Element, data_info: data)
##
The function gets a root of a safety report and it saves its information in a dictionary.
For the "drug" field, it creates a list of dictionaries, using the function drug_handling.
For the "reaction" field, the function saves the most severe reaction outcome,using the function reaction_handling.
For the other fields, it saves the name of the field as a key,
and the text of the field as a value.
##

def keep_high_freq_drugs(data_info: data)
##
Each report has information about many drugs.
For each report, the function keeps only the drugs that have the highest frequency, according to data_info.drugs_freq.
##

def main()
##
The function reads the XML files, for each file it creates an Element Tree,
and for each safety report it calls the function treat_safety_report.
##
