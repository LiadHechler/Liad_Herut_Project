## Explanation about the code ##

class data
##
Class to keep the information of the data.
safety_reports is a list of dictionaries,
each element in the list represents the information of a safety report.
bag_of_drugs is a dictionary- each key is a name of a drug,
                            each value is the frequency of this drug.
reaction_outcome_freq is a dictionary - each key is a reaction outcome,
                                        each value is the frequency of this reaction.
                                        **for every report we consider only the most severe reaction outcome
##

def medical_product_calc_freq(item: ET.Element, bag_of_drugs: dict)
##
Updates the data_info.bag_of_drugs dictionary, each key is a word from a name of a drug
and each value is the frequency of this word in the safety reports.
We save the dictionary as an attribute in the data class.
##

def reaction_outcome_handling(most_severe_outcome: str, reaction_outcome_freq: dict)
##
Updates the data_info.reaction_outcome_freq dictionary,
each key is a reaction outcome, and each value is the frequency of this reaction.
For each report, we count only the most severe outcome.
##

def drug_handling(root: ET.Element, bag_of_drugs: dict) -> dict
##
Treats the "drug" field.
Each report consists of many of drugs and each drug has many sub-fields,
so we keep the information of each field in a dictionary.
The function returns the dictionary with the information of the current field.
##

def reaction_handling(root: ET.Element, most_severe: str) -> str:
##
Function to save the most severe reaction outcome for every report.
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
In addition, the function removes some of the drug fields, which we assumed that they are irrelevant.
##

def main()
##
The function reads the XML files, for each file it creates an Element Tree,
and for each safety report it calls the function treat_safety_report.
##
