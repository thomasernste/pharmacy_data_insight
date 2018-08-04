import csv
import sys
from itertools import islice


def process_pharm_data(input_data_txt, output_data_txt):

    drug_dict = {}
    with open(input_data_txt, "r") as file:
        skipped = islice(file, 1, None)
        for i, line in enumerate(skipped, 2):
            try:
                number, last, first, drug, price = line.split(',')
            except ValueError:
                pass
            try:
                a = round(float(price), 2)
                price = a
            except ValueError:
                b = int(price)
                price = b

            if drug not in drug_dict:
                drug_dict[drug] = [1, price]
            else:
                drug_dict[drug][0] += 1
                drug_dict[drug][1] += price

    final_sorted_list = sorted(drug_dict.items(), key=lambda d: (d[1][1], d[0]), reverse=True)

    final_array = [[row[0], row[1][0], round(row[1][1])] for row in final_sorted_list]

    # final_array = [[row[0], row[1][0], round(row[1][1], 2)] if round(row[1][1]) != row[1][1] else [row[0], row[1][0],
    #                         round(row[1][1])] for row in final_sorted_list]

    final_array.insert(0, ['drug_name', 'num_prescriber', 'total_cost'])

    with open(output_data_txt, 'w') as myfile:
        wr = csv.writer(myfile)
        for i in final_array:
            wr.writerow(i)

# process_pharm_data('../input/itcont.txt', '../output/top_cost_drug.txt')

def main():
    input_data_txt = sys.argv[1]
    output_data_txt = sys.argv[2]
    process_pharm_data(input_data_txt, output_data_txt)

if __name__ == '__main__':
    main()