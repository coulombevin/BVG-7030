#!/bin/bash

module add StdEnv/2020 samtools/1.16.1

CPU=4

#cd NGS
# create a log file
exec &> convert.log

# convert SAM format to BAM format

parallel -j $CPU samtools view -b -S -h {}.sam ">" {}.temp.bam ::: $(ls -1 >                if [ $? -ne 0 ]
                        then
                                printf "There is a problem in the samtools->                                exit 1
                fi
# sort BAM files

parallel -j $CPU samtools sort {}.temp.bam -o {}.sort.bam ::: $(ls -1 *.tem>                if [ $? -ne 0 ]
                        then
                                printf "There is a problem in the samtools->                                exit 1
                fi

# indexing of BAM files
parallel -j $CPU samtools index {} ::: $(ls -1 *.sort.bam)
                if [ $? -ne 0 ]
                        then
                                printf "There is a problem in the samtools->                                exit 1
                fi
                
# create a list of BAM files with path

for i in $(ls -1 *.sort.bam)
                        do
                                printf "$PWD/${i}\n" >> "bamlist"
                                if [ $? -ne 0 ]
                                        then
                                        printf "There is a problem in the p>
                                        exit 1
                                fi
                        done
