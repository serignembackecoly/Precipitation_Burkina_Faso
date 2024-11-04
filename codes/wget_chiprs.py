import os
import wget

base_url = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/chirps-v2.0.{}.days_p05.nc"
dossier = "E:\\Chirps_daily\\"
annees = range(1986,2023)
for annee in annees:
    url = base_url.format(annee)
    print("          Downloading year {}".format(annee))
    wget.download(url, out = dossier)