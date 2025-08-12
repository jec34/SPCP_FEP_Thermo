# SPCP_FEP_Thermo

Files for running molecular dynamics simulations to obtain average pressures that can be used for thermodynamic integration to calculate free energy profiles. 

Included files are for relevant simulations on ZnMOP-bibPh, ZnMOP-bipy, ZnMOP-bix, ZnMOP-Dabco, DUT-48, DUT-49, and DUT-50. Files for each SPCP include an initial data.[] file as the starting crystalline structure, in.expand and in.contract files for LAMMPS simulations to obtain a range of volumes. The shell script volume_sweep.sh begins NVT MD simulations for each volume point, and once those have run get_avg_pressures.sh to calculate average pressures. From there the jupyter notebook uses pressure data files to calculate and plot free energy profiles.

Also included are input files for RASPA Grand Canonical Monte Carlo simulations.

## MD Runs Overview
To set up an MD run and obtain a free energy profile first use the contract.job and expand.job scripts to obtain the full range of volumes of interest. Next, use volume_sweep.sh to initialize an MD run for each volume point. The temperature of this run and the number of methane molecules present are defined in obtain_pressure_template.in. On completion of all MD simulations, use get_avg_pressures.sh to produce a txt file containing average pressure data for this run. This process can be repeated at all temperatures and pressures of interest.

## Jupyter Notebook
The Jupyter notebook is used to read in the pressure data from the MD simulations and calculate and visualize the free energy profile. Place all pressure.txt files into the FreeEnergy_Sept_data folder (with unique names!) and expand the Jupyter notebook to include any additional thermodynamic conditions of interest.
