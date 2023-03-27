#!/usr/bin/env python3

import argparse


def read_fasta_file(fasta_file):
    """
    Reads a FASTA file and returns a dictionary of sequence IDs and sequences
    """
    sequences = {}
    with open(fasta_file, 'r') as f:
        sequence_id = ''
        sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = sequence
                    sequence = ''
                sequence_id = line[1:]
            else:
                sequence += line
        sequences[sequence_id] = sequence
    return sequences

def write_single_sequence_file(fasta_file, output_file):
    """
    Reads a FASTA file and writes a single string output file
    """
    sequences = read_fasta_file(fasta_file)
    with open(output_file, 'w') as f:
        for sequence_id, sequence in sequences.items():
            sequence = sequence.upper()
            cleaned_sequence = ''.join([base for base in sequence if base in 'ATGC'])
            f.write(cleaned_sequence)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Read a FASTA file and write a single uppercase plain string output file')
    parser.add_argument('input', help='Input FASTA file name')
    parser.add_argument('output', help='Output file name')

    # Parse arguments
    args = parser.parse_args()

    # Call write_single_sequence_file function
    write_single_sequence_file(args.input, args.output)

if __name__ == '__main__':
    main()
