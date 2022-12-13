# BVG-7030

### Repertory
This repertory contains all the documents make during the course BVG-7030.


### Basic_python_code.py
This document contain some basic codes frequently used in python scripts.


### biopython.py
This document show some applications of the package biopython.


## GWAS/Fastq2vcf
This folder contains scripts needed to past from fastq files to vcf on NARVAL (COMPUTE CANADA).

#### 1_Sabre.sh
This bash file group all sequencing data based on their barcode.

#### 2_Cutadapt.sh
This bash file create a virtual environment to pip install cutadapt then trim the adaptors used for the sequencing.

#### 3_bwa.sh
This bash file convert fastq files to SAM files.

#### 4_sam2bam.sh
This bash file convert SAM files to BAM files then sort and index those bam files. The last block of code create a list of all the BAM files for the next step (5_samt_var.sh).

#### 5_samt_var.sh
This bash file make a variant calling and output a VCF file.

## GWAS/R_Analysis
That folder contains command used on R Studio to produce analysis and graphs.

#### GAPIT.R
That script use the GAPIT package to produce heat map to show proximity between cultivars.
(GAPIT) Wang J., Zhang Z., GAPIT Version 3: Boosting Power and Accuracy for Genomic Association and Prediction, Genomics, Proteomics & Bioinformatics (2021), doi: https://doi.org/10.1016/j.gpb.2021.08.005.

#### mvp.R
That script create circular Manhattan plot, Manhattan plot, QQ plot and SNP density plot.
