#!/bin/bash

module add StdEnv/2020 intel/2020.1.217 sabre/1.00

#set variable
DATA=/home/vicou67/scratch/BVG-7003/Cours_9/GBS_data/FC20150701_1.fq
BARCODE=/home/vicou67/scratch/BVG-7003/Cours_9/GBS_data/FC20150701_1.txt

#output a log of my sh
exec &> sabre.log

#execute sabre tool with variable to demultiplex and trim fastq
sabre se -f $DATA -b $BARCODE -u FC20150701_1_Sabre.fastq
