# for skipping header line while reading file to dict
from itertools import islice

# for writing final array to .txt file
import csv

# enables reading the arguments from the function
import sys


def process_pharm_data(input_data_txt, output_data_txt):
    # The input file is read in to a dictionary.
    drug_dict = {}

    with open(input_data_txt, "r") as file:
        # This enables skipping the header line.
        skipped = islice(file, 1, None)
        for i, line in enumerate(skipped, 2):
            # A harmless ValueError occurs when reading in drug prices with
            # decimal places. This try and except block enables bypassing the
            # error.
            try:
                number, last, first, drug, price = line.split(',')
            except ValueError:
                pass

            # Because the drug prices on the input files can be either integers
            # (whole dollar figures with no cents) or floats (dollar figures
            # that include cents), This try and except block enables rounding
            # the drug prices to 2 decimal places only if the input data are
            # floats with dollars and cents data
            try:
                a = round(float(price), 2)
                price = a
            except ValueError:
                b = int(price)
                price = b

            # This if/else block creates the drug name grouped with the id as
            # the key in a dictionary if the drug+id does not yet appear. The
            # '$' and id here add to the drug name to create a unique drug+id
            # combination for each prescriber of each drug. The corresponding
            # value for this key is a list of 2 items including a counter for
            # the drug+id (a counter for the 'num_prescriber' column that
            # counts each prescriber once for each drug) and the price of the
            # first instance of that drug. If the drug+id does already appear,
            # the code under the "else" clause then adds the price value of
            # that drug+id to the price that already corresponds with that
            # drug+id.
            if drug + '$' + first + last not in drug_dict:
                drug_dict[drug + '$' + first + last] = [1, price]
            else:
                drug_dict[drug + '$' + first + last][1] += price

        # This block removes the '$' and id value from the previous dictionary,
        # adds the counter that counts the num_prescribers, and adds the dollar
        # value for the particular drug in question
        drug_dict2 = {}
        for k, v in drug_dict.items():
            if k.split('$', 1)[0] not in drug_dict2:
                drug_dict2[k.split('$', 1)[0]] = v
            else:
                drug_dict2[k.split('$', 1)[0]][0] += v[0]
                drug_dict2[k.split('$', 1)[0]][1] += v[1]

    # This line sorts the dictionary data into a list, sorting first in
    # descending ("reverse") order by the price, then by descending order by
    # the alphabetical name of the drug.
    final_sorted_list = sorted(drug_dict2.items(), key=lambda kv: (kv[1][1],
                            kv[0]), reverse=True)

    # This list comprehension appends the data to the correct columns. Also,
    # because floating point arithmetic causes some flawed values when adding
    # floats together, this list comprehension includes conditional if/else
    # clauses that enable rounding float values to two places while ensuring
    # that original integer values (with no cents values) will remain integers.

    final_array = [[row[0], row[1][0], round(row[1][1], 2)] if round(row[1][1]) - row[1][1] != 0 else [row[0], row[1][0], round(row[1][1])]
                        for row in final_sorted_list]

    # This line inserts a header row at position 0 in the final array
    final_array.insert(0, ['drug_name', 'num_prescriber', 'total_cost'])

    # This block writes the data to the output file
    with open(output_data_txt, 'w') as myfile:
        wr = csv.writer(myfile)
        for i in final_array:
            wr.writerow(i)

# process_pharm_data('../input/itcont.txt', '../output/top_cost_drug.txt')

# This block allows execution of the process_pharm_data function from the
# run.sh shell script with the appropriate input and output files included
# in the run.sh shell script and run_tests.sh test script.
def main():
    input_data_txt = sys.argv[1]
    output_data_txt = sys.argv[2]
    process_pharm_data(input_data_txt, output_data_txt)

if __name__ == '__main__':
    main()