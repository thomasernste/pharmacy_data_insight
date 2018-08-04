# Insight Data Engineering - Pharmacy Drugs and Price Counting ( ~ Thomas Ernste)

This repository contains a project used to process data from a large list of pharmaceutical drugs that are sold on online pharmacies. The source code, written in python, reads an input .txt file, processes the file, and generates an output .txt file that includes each drug, a count of the number of time each drug appears in the input data, and the total sum cost of all instances of each drug that appears in the input file. The data is sorted first in descending order by price and secondly in descending order alphabetically by the drug name.


# Input Dataset

The original input dataset (itcont.txt, in the input directory) came from the Centers for Medicare & Medicaid Services. It includes information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name*. It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication.


# Libraries used

The Python libraries used in the source code include:

- islice (from itertools, which enables skipping the header line in the process of reading in the input file and writing the data to a dict)

- csv (needed for writing final array to .txt file)

- sys (enables reading the function arguments)


# Output

Each line of the output file contains these fields in a comma-separated format:

- drug_name: each drug name from the input dataset
- num_prescriber: the number of unique prescribers who prescribed the drug. A prescriber is considered the same person if two lines share the same prescriber first and last names
- total_cost: total cost of the drug across all prescribers


# Code

The code is documented in detail and it has been tested to work small and large datasets with both integers and floats for the drug price values.


# Repo directory structure

A test script called run_tests.sh is included to facilitate testing my code to ensure the correct directory structure and the correct format for my output files. In addition, the ./run_tests.sh file can be run from the command line in the directory called insight_testsuite. I have two tests included in my repository: one for a small input dataset where the drug prices are in integers (just dollar amounts, no cents), and a second larger input dataset where the drug prices are in floats (dollar amounts with cents). As I explain in my code documentation, the different integer and float datatypes required different considerations for adding up the drug prices.
