# SPCP_FEP_Thermo

Files for running molecular dynamics simulations to obtain average pressures that can be used for thermodynamic integration to calculate free energy profiles. 

Included files are for relevant simulations on ZnMOP-bibPh, ZnMOP-bipy, ZnMOP-bix, ZnMOP-Dabco, DUT-48, DUT-49, and DUT-50. Files for each SPCP include an initial data.[] file as the starting crystalline structure, in.expand and in.contract files for LAMMPS simulations to obtain a range of volumes. The shell script volume_sweep.sh begins NVT MD simulations for each volume point, and once those have run get_avg_pressures.sh to calculate average pressures. From there the jupyter notebook uses pressure data files to calculate and plot free energy profiles.

Also included are input files for RASPA Grand Canonical Monte Carlo simulations.
