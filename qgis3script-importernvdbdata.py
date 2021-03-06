# -*- coding: utf-8 -*-
"""
Script for å interaktivt legge til NVDB-vegnett og fagdata via python 
kommandolinje i QGIS. Se dokumentasjon på bruk av nvdbapi - funskjoner på
https://github.com/LtGlahn/nvdbapi-V2


Legg dette scriptet et sted hvor det er lettvint 
å finne fra QGIS. F.eks. C:/Users/<dittbrukernavn>. 

EKSEMPLER

#Vegnett europaveger Trondheim kommune
v = nvdbVegnett()
v.addfilter_geo({ 'kommune' : 1601, 'vegreferanse' : 'E' })" ) 
nvdbsok2qgis( v, lagnavn='Europaveger Trondheim') 

# Vegnett innenfor kartutsnitt
v = nvdbVegnett()
nvdb2kart( v, iface) 


# Bomstasjoner
b = nvdbFagdata(45)
nvdbsok2qgis( b) 

# Søk etter fartsgrenser innenfor kartflaten, legg til 
f = nvdbFagdata(105)
nvdb2kart( f, iface)

# Søk etter kjent objektID, legg til kartflaten
nvdb2kart( 572672190, iface )

"""

import sys
# import os 

# Endre stien til dit du har lastet ned biblioteket
# https://github.com/LtGlahn/nvdbapi-V2 
nvdblibrary = 'C:/Data/test/github/nvdbapi-V2'
# nvdblibrary = '/home/jan/Documents/jobb/nvdbapi-V2-test'

if not [ k for k in sys.path if 'nvdbapi-V2' in k]: 
    print( 'Føyer', nvdblibrary, 'til søkestien') 
    sys.path.append(nvdblibrary)

from nvdbapi import nvdbFagdata, nvdbVegnett
from nvdb2qgis3 import  nvdb2kart, nvdbsok2qgis

## Bruk linjene nedenfor for debugging
# import imp
# import nvdb2qgis3
# import nvdbapi 
# imp.reload(nvdb2qgis3 )
#