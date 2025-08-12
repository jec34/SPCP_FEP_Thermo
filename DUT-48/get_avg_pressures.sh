#!/bin/bash
#$ -M jcarpen3@nd.edu
#$ -m e
#$ -q hpc@@colon

module load python

rm pressures.txt
echo "avg_press    volume      avg_enthalp" >> pressures.txt

for index in $(seq 22.49 0.2 57.69)
do
string=${index}
lmps_file=DUT-48_vol_${string}.lmps
in_file=DUT-48_vol_${string}

#python3 -W ignore analyze_lmps.py ${in_file}.out pressures.txt
python3 analyze_lmps.py ${in_file}.out pressures.txt

done
