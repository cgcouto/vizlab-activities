## Density datacubes

### Requirements

* numpy
* matplotlib
* pickle
* h5py

### Explanation

In this activity, we'll be using simulation data Either do this on the command line (with wget https://github.com/usc-cosmolab/hackspace/blob/master/data/halos_short.bin?raw=true -O halos_short.bin) or follow the Github link and download the file from there. 

The simulation file is an N-body simulation 

### What next?

Run the provided Python script, which will open the simulation file and plot an example snapshot of the data. Once you've done that, consider making some adjustments before binning the points and saving the datacube for viewing in the VizLab: 

* Use the mass of the subhalos ('mvir' keyword). Where are the higher mass located?
* Use the radius of the subhalos ('rvir' keyword)

### Author's note

This exercise is based off of Python exercises from Ethan Nadler, which you can find here: https://github.com/eonadler/Colab-Notebooks/blob/main/Week_4_Exploring_N_body_Simulations.ipynb