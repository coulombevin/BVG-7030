#!/bin/bash
module add StdEnv/2020 samtools/1.16.1 gcc/9.3.0 bcftools/1.16


DATA=/home/vicou67/scratch/BVG-7003/Cours_9/GBS_data/4_samfiles/bamlist
REF=/home/vicou67/scratch/BVG-7003/Cours_9/refgenome/Gmax_275_v2.0.fa
OUT=variantcalling
CPU=4

mkdir results1
cd results1

exec &> samt_var.log
#option -g retire car erreur
samtools mpileup -f $REF -b $DATA > variants.bcf

        if [ $? -ne 0 ]
                        then
                                printf "There is a problem at the samtools_>                                exit 1
                fi


bcftools call -mv variants.bcf > variants.vcf

        if [ $? -ne 0 ]
                        then
                                printf "There is a problem at the bcf2vcf s>                                exit 1
                fi
