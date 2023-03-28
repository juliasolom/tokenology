# tokenology

- 1. Get plain text genome with script `get_plain_text.py`

- 2. Get promotors file in fasta format with this tool - https://github.com/milesroberts-123/extract-promoter-sequences or this ! - *https://github.com/RimGubaev/extract_promoters*:

>ID=gene-ND6::AY172335.1:14070-14370(-)
CGTAATTTACGTCTCGACAAATGTGTGTTACTGATGAAAAGGCTGTTATTGTATCTGATGTGTAGTGTATGGCTAAGAAAAGACCTGTAATGATTTGGACTATTAGGCAGACTCCTA
GAAGGGACCCAAAGTTTCATCATGATGAAATGTTGGATGGGGCAGGTAGGTCAATGAATGAGTGGTTAATAATTTTAAATAATGGGTGTGTTTTTCGTATGTTTGTCATTAGGTGTT
TCTGTAGTTGAATTACAACGATGATTTTTCATGTCATTGGTCGCAGTTGAATGCTGTGTAGAAATA

results: /mnt/tank/scratch/yusolomennikova/mus_BPE/corpus_mous/extract_promoters/promoters.fa

- 3. create corpus of sequences with `create_corpus.py`  from *GENA_LM*

- 4. create a dataset with `dataset_generator.py` from *GENA_LM* (I changed the script a little and padded the input sequence with 'N' if its length is not divisible by 20)
- 5. split to 5 folds with `dataset_fold_split.py` from .tsv file obtained in previous step
