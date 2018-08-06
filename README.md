#### Thomas Ernste

# Insight Data Engineering - Pharmacy Drugs and Price Counting

This repository contains a project used to process data from a large list of pharmaceutical drugs sold by online pharmacies. The source code, written in Python 3, reads an input .txt file, processes the file, and generates an output .txt file that includes the name of each drug in the input list, a count of the number of medical professionals who have prescribed that drug, and the total sum cost of all instances of each drug that appear in the input file. The data is sorted first in descending order by price and secondly (if the total sum cost is the same for two or more drugs) in descending order alphabetically by the drug name.



# Input Dataset

The original input dataset (itcont.txt, in the input directory) came from the Centers for Medicare & Medicaid Services. It includes information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their medical ID, last name, and first name. It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication.



# Libraries used

The Python libraries used in the source code include:

- **islice** - (imported from itertools, this library enables skipping the header line in the process of reading in the input file and writing the data to a dict)

- **csv** - (needed for writing final array to .txt file)

- **sys** - (enables reading the function arguments)



# Output file

Each line of the output file contains the following fields in a comma-separated format:

- **drug_name**: each drug name that appears in the input dataset
- **num_prescriber**: the number of unique prescribers who prescribed the drug. For the purpose of this project, unique prescribers are identified by their first and last names.
- **total_cost**: total cost of each drug across all prescribers



# Code

The code is documented in detail and has been tested for scalability to work on small and large datasets and to handle either integers or floats for the drug price values.



# Repo directory structure

A test script called run_tests.sh is included to facilitate testing the source code. This test ensures the correct directory structure and the correct format for the output files. In addition, the run_tests.sh file can be run as follows from the command line in the directory called insight_testsuite:

`insight_testsuite~$ ./run_tests.sh`

There are two tests included in this repository: one for a small input dataset in which the drug prices are represented as integers (just whole dollar amounts, no cents), and a second larger input dataset in which the drug prices are represented as floats (dollar amounts with cents). As I explain in my code documentation, the different integer and float datatypes required different coding considerations for adding up and rounding the drug prices and to arrive at the desired output data. Notably, this code also successfully processed a file that was much larger than either of the two files in the included tests. However, Github's file size limitations prevented uploading this file for testing.
