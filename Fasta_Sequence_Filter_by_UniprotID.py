from Bio import SeqIO

# File containing the list of IDs to keep
ids_file = "C:/Users/Joy/Desktop/ID.txt"

# Input FASTA file
input_fasta = "C:/Users/Joy/Downloads/uniprotkb_P_aeruginosa_AND_reviewed_tru_2025_09_11.fasta"

# Output FASTA file for the filtered sequences
output_fasta = "C:/Users/Joy/Desktop/filtered_sequences.fasta"

# Read the IDs into a set for fast lookup
with open(ids_file) as f:
    # Assuming ids_to_keep.txt contains ONLY the UniProt IDs (e.g., A6V0D3)
    wanted_ids = set(line.strip() for line in f)

# Parse the input file and filter sequences
filtered_records = []
for record in SeqIO.parse(input_fasta, "fasta"):
    # Extract the correct ID from the FASTA header
    # The header is like: >sp|A6UZH4|EFTU_PSEP7 ...
    # We want the second part after splitting by '|' and stripping whitespace.
    header_parts = record.description.split('|')
    if len(header_parts) > 1:
        # The UniProt ID is the second element (index 1) after splitting by '|'
        actual_id = header_parts[1].strip()

        # Now compare this extracted ID with your wanted_ids
        if actual_id in wanted_ids:
            filtered_records.append(record)

# Write the filtered sequences to the output file
with open(output_fasta, "w") as out_handle:
    SeqIO.write(filtered_records, out_handle, "fasta")

print(f"Successfully saved {len(filtered_records)} sequences to {output_fasta}")