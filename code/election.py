import csv
import h5py
import pandas as pd
import numpy as np

galaxy = pd.read_csv('galaxy1.csv', sep = ',')
fof = pd.read_csv('fof.csv', sep = ',')

min_ID = fof['GroupID'].min()
fof['GroupID'] = fof['GroupID'] - min_ID + 1

gal_id= galaxy['GroupID']
fof_id = fof['GroupID']


match = np.loadtxt('match.dat')
eagle_id, dm_id = match[:,0], match[:,1]
table =  h5py.File('gal_halo.h5','w')
ngal = len(gal_id)



table.create_dataset('gal_CentreOfMass_x', (ngal,) , data = galaxy['CentreOfMass_x']) 
table.create_dataset('gal_CentreOfMass_y', (ngal,) , data = galaxy['CentreOfMass_y'])
table.create_dataset('gal_CentreOfMass_z', (ngal,) , data = galaxy['CentreOfMass_z'])
table.create_dataset('gal_GalaxyID', (ngal,) , data = galaxy['GalaxyID'])
table.create_dataset('gal_GroupID', (ngal,) , data = galaxy['GroupID'])
table.create_dataset('gal_GroupNumber', (ngal,) , data = galaxy['GroupNumber'])
table.create_dataset('gal_SubGroupNumber', (ngal,) , data = galaxy['SubGroupNumber'])
table.create_dataset('gal_MassType_Star', (ngal,) , data = galaxy['MassType_Star'])
table.create_dataset('gal_StarFormationRate', (ngal,) , data = galaxy['StarFormationRate'])
table.create_dataset('gal_StellarVelDisp', (ngal,) , data = galaxy['StellarVelDisp'])
table.create_dataset('gal_Vmax', (ngal,) , data = galaxy['Vmax'])

table.create_dataset('fof_GroupCentreOfPotential_x', (ngal,) , data = fof['GroupCentreOfPotential_x'])
table.create_dataset('fof_GroupCentreOfPotential_y', (ngal,) , data = fof['GroupCentreOfPotential_y'])
table.create_dataset('fof_GroupCentreOfPotential_z', (ngal,) , data = fof['GroupCentreOfPotential_x'])
table.create_dataset('fof_GroupID', (ngal,) , data = fof['GroupID'])
table.create_dataset('fof_Group_M_Crit200', (ngal,) , data = fof['Group_M_Crit200'])
table.create_dataset('fof_Group_R_Crit200', (ngal,) , data = fof['Group_R_Crit200'])

print
