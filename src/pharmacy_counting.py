import csv
import sys
from collections import defaultdict


def filter_pharm_data(input_data_txt, output_data_txt):

    #Open the file from the first argument (input_data_txt) and read it in as a list
    with open(input_data_txt, 'r') as file:
        reader = csv.reader(file)
        pharm_input = list(reader)

    # Preserve only the columns I need from the input data array to complete the data processing
    for row in pharm_input:
        del row[:3]
    pharm_input[0].insert(5, 'count_value')
    for row in pharm_input[1:]:
        row.insert(3, 1)


    count_dict = {}  # Initialize final dict that will contain output data
    cost_dict = {}

    for drug, cost, counter in pharm_input[1:]:
    # # #     #if the user value for a row is equal to some 'ip' address, iterate through all of these ip addresses

        if drug in count_dict:
            count_dict[drug] += 1
        else:
            count_dict[drug] = counter

        if drug in cost_dict:
            cost_dict[drug] += int(cost)
        else:
            cost_dict[drug] = int(cost)

    final_dict = defaultdict(list)


    for d in (count_dict, cost_dict):  # you can list as many input dicts as you want here
        for key, value in d.items():
            final_dict[key].append(value)

    final_dict = dict(final_dict)

    final_sorted_list = sorted(final_dict.items(), key=lambda kv: (-kv[1][1], kv[0]))


    final_array = [[row[0], row[1][0], row[1][1]] for row in final_sorted_list]
    final_array.insert(0, ['drug_name', 'num_prescriber', 'total_cost'])

    with open(output_data_txt, 'w') as myfile:
        wr = csv.writer(myfile)
        for i in final_array:
            wr.writerow(i)

def main():
    input_data_txt = sys.argv[1]
    output_data_txt = sys.argv[2]
    filter_pharm_data(input_data_txt, output_data_txt)

if __name__ == '__main__':
	main()