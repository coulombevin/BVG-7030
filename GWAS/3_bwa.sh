#!/bin/bash

module add StdEnv/2020 bwa/0.7.17

#set variable for trimmed gbs and ref genome
DATA=/home/vicou67/scratch/BVG-7003/Cours_9/GBS_data/3_fastqTrimme
REF=/home/vicou67/scratch/BVG-7003/Cours_9/refgenome/Gmax_275_v2.0.fa
CPU=3
THR=2

#launch bwa in parallel
exec &> bwa.log
cd $DATA
                parallel -j $CPU bwa mem -t $THR $REF {}.fastq ">" {}.sam :>
                if [ $? -ne 0 ]
                        then
                                exit 1
                fi
