module load python/3.10 scipy-stack/2022a

#initialise virtual environment
virtualenv --no-download $SLURM_TMPDIR/env

#activate virtual environment
source $SLURM_TMPDIR/env/bin/activate

#upgrade pip and install cutadapt
pip install --no-index --upgrade pip
python3 -m pip install --user --upgrade cutadapt

#exit virtual environment
deactivate

#trimming of adaptors
ADAP=AGATCGGAA
exec &> cutadapt.log
parallel -j 4 cutadapt -a $ADAP -m 50 -o {}.fastq {}.fq ::: $(ls -1 *.fq | >        if [ $? -ne 0 ]
                then
                        exit 1
        fi
