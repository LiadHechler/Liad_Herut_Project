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

def drug_handling(root: ET.Element, data_info: data) -> dict
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

def plot_route_graph(sort_route: list, sort_route_values: list)
##
The function calculates the value of 1% of the total number of routes.
Then it plots the routes that have more than 1% of total routes and its frequencies.
It helped us to determine which routes we will use to describe the drugs' names. (function rename_drug)
NOTE: the route "065", which has the highest frequency is "unknown".
##

def switch_route_num_to_str(route_name: str) ->str
##
We changed codes to its literal meaning, according to the FDA website:
https://admin.ich.org/sites/default/files/inline-files/ICH_ICSR_Specification_V2-3.pdf
##

def rename_drug(drug: dict, data_info: data)
##
The function adds to the name of the drug, the drug administration route, to differ between types of drugs.
We chose the 3 most frequent administration route codes, according to graph 1.
We named he rest of the codes, including "o65" (="unknown"), as "other".
##

def keep_high_freq_drugs(data_info: data) -> list
##
Each report has information about many drugs.
For each report, the function keeps only 200 drugs that have the highest frequency, according to data_info.bag_of_drugs.
The function calls to the function rename_drug, and than it calculate the frequencies of the new name (including the administration route).
In addition, the function ***PLOT***...
According to the plot, we decided to keep only the drugs that their frequencies are more than 1% of the number of the safety reports.
It returns the list of the remined drugs.
##

def main()
##
The function reads the XML files, for each file it creates an Element Tree,
and for each safety report it calls the function treat_safety_report.
##
