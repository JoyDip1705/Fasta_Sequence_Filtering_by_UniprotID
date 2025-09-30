🧬 Biopython FASTA Sequence Filter

This Python script uses the powerful Biopython library (Bio.SeqIO) to perform highly specific filtering of sequences from a large multi-FASTA file. It enables researchers to subset a FASTA file by matching a list of desired UniProt IDs against the sequence headers.

✨ Features

  1 ID-Driven Filtering: Extracts only the sequences whose IDs are present in a separate text file.

  2 UniProt Compatibility: Specifically designed to parse standard UniProt FASTA headers (e.g., >sp|A6V0D3|NAME_ORGANISM...) to correctly identify the target ID.

  3 Efficiency: Utilizes Python's set structure for lightning-fast lookup of wanted IDs, making it suitable for large input files.

  4 Standard Library Usage: Relies on the widely-used and robust Biopython library for reliable FASTA parsing and writing.


  🚀 How to Use

1. Requirements

You must have Python 3 installed, along with the Biopython library.
Bash

pip install biopython

2. Prepare Input Files

You need two files:

    Input FASTA File: The multi-sequence FASTA file you want to filter (e.g., uniprotkb_...fasta).

    ID List File: A simple text file where each line is a single UniProt ID you wish to keep (e.g., ID.txt).

    A6V0D3
    Q9I1S5
    P0A8G3
    ...

3. Configuration

Edit the Python script and update the three file paths to match your local setup:
Python

# File containing the list of IDs to keep
ids_file = "path/to/your/ID.txt"

# Input FASTA file
input_fasta = "path/to/your/input.fasta"

# Output FASTA file for the filtered sequences
output_fasta = "path/to/your/filtered_sequences.fasta"

4. Execution

Run the script from your terminal:
Bash

python fasta_sequence_filter.py

The script will report the number of sequences successfully written to the output file.

⚙️ How the ID Extraction Works

The script is specifically written to handle standard UniProt headers, which often look like this:
>sp|A6UZH4|EFTU_PSEP7 Elongation factor Tu [Pseudomonas septica]

The script uses .split('|') on the header description. The desired UniProt ID (A6UZH4) is always the second element (index 1) of the resulting list. This robust extraction ensures correct filtering.
