import xml.etree.ElementTree as ET # Library for xml files


# Class to keep the information of the data
class data:
    def __init__(self):
        self.safety_reports = []
        self.drugs_freq = {}
        self.reaction_outcome_freq = {}


def medical_product_handling(curr_d: dict, item: ET.Element, drugs_freq: dict):
    curr_d[item.tag] = item.text.split()[0].rstrip("/.,")
    if curr_d['medicinalproduct'].upper() not in drugs_freq:
        drugs_freq[curr_d['medicinalproduct'].upper()] = 1
    else:
        drugs_freq[curr_d['medicinalproduct'].upper()] += 1


def reaction_outcome_handling(most_severe_outcome: str, reaction_outcome_freq: dict):
    if most_severe_outcome not in reaction_outcome_freq:
        reaction_outcome_freq[most_severe_outcome] = 1
    else:
        reaction_outcome_freq[most_severe_outcome] += 1


def drug_reaction_handling(root: ET.Element, data_info: data) -> dict:
    curr_d = {}
    for item in list(root):
        if item.tag == 'activesubstance':
            curr_d[item[0].tag] = item[0].text
        elif item.tag == 'medicinalproduct':
            medical_product_handling(curr_d, item, data_info.drugs_freq)
        else:
            curr_d[item.tag] = item.text

    return curr_d


# Treatment for each report in the file
def treat_safety_report(root: ET.Element, data_info: data):
    report = {}
    list_drugs = []
    list_reactions = []
    most_severe_reaction = ""
    for child in root:
        # If the child has children
        if child.text.find("\n") != -1:
            # Children is list of his children
            children = list(child)
            for item in children:
                if item.text.find("\n") == -1: # There aren't more children
                    report[item.tag] = item.text
                else: ## Reaction or drug
                    d_current = drug_reaction_handling(item, data_info)
                    if item.tag == 'drug': # Dictionary for each drug
                        list_drugs.append(d_current)
                    if item.tag == 'reaction': # Dictionary for each reactions
                        list_reactions.append(d_current)
                        # Keep the most severe reaction outcome for each report
                        if 'reactionoutcome' in d_current:
                            most_severe_reaction = max(d_current['reactionoutcome'], most_severe_reaction)
        else:
            report[child.tag] = child.text
    # Count the frequency of most severe reactions in the data
    reaction_outcome_handling(most_severe_reaction, data_info.reaction_outcome_freq)

    report["drugs"] = list_drugs
    report["reactions"] = list_reactions
    data_info.safety_reports.append(report)


def main():
    data_info = data()
    files = ['1_ADR21Q3.xml','2_ADR21Q3.xml','3_ADR21Q3.xml']
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        for child_report in root:
            if child_report.tag == 'safetyreport':
                treat_safety_report(child_report, data_info)
    print("Patients: ", len(data_info.safety_reports))
    print("Number of drugs: ", len(data_info.drugs_freq))
    sort_d = sorted(data_info.drugs_freq.keys(), key=data_info.drugs_freq.get, reverse=True)
    for i in range(10):
        print(sort_d[i], data_info.drugs_freq[sort_d[i]])

    print("Reactions: ")
    print(data_info.reaction_outcome_freq)
 #       for report in safety_reports:
 #           for key in report:
 #               print(key+": ",report[key])
 #           print('-----------------')


if __name__ == "__main__":
    main()



#for key in report:
#    print(key+": ",report[key])


#for item in root.iter('reportduplicate'):
 #   print(item.text)
