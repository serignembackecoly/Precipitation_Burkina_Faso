import os
import wget

bbox_1 = [340,360,0,28]
bbox_2 = [0,20,0,28]

base_url = "https://ds.nccs.nasa.gov/thredds/ncss/AMES/NEX/GDDP-CMIP6/{}/{}/{}/{}/{}_day_{}_{}_{}_{}_{}.nc?var={}&north={}&west={}&east={}&south={}&disableProjSubset=on&horizStride=1&time_start={}-01-01T12%3A00%3A00Z&time_end={}-12-{}T12%3A00%3A00Z&timeStride=1&addLatLon=true"

models = ["KIOST-ESM"]
# models = ["KACE-1-0-G", "CMCC-ESM2",
#         "CMCC-CM2-SR5","NorESM2-MM","NorESM2-LM","MRI-ESM2-0",
#         "ACCESS-ESM1-5", "ACCESS-CM2","EC-Earth3", "HadGEM3-GC31-LL",
#         "IPSL-CM6A-LR", "MPI-ESM1-2-LR", "UKESM1-0-LL", "TaiESM1",
#         "GFDL-ESM4", "INM-CM5-0","INM-CM4-8", "MPI-ESM1-2-HR",
#         "MIROC6","MIROC-ES2L","IPSL-CM6A-LR", "CNRM-CM6-1",
#         "FGOALS-g3", "CanESM5", "CNRM-ESM2-1"]

# "KIOST-ESM" <- 2072:2101,
realz = {
    "UKESM1-0-LL":"r1i1p1f2","TaiESM1":"r1i1p1f1","NorESM2-MM":"r1i1p1f1",
    "NorESM2-LM":"r1i1p1f1","NESM3":"r1i1p1f1","MRI-ESM2-0":"r1i1p1f1",
    "MPI-ESM1-2-LR":"r1i1p1f1","MPI-ESM1-2-HR":"r1i1p1f1","MIROC6":"r1i1p1f1","MIROC-ES2L":"r1i1p1f2","KIOST-ESM":"r1i1p1f1",
    "KACE-1-0-G":"r1i1p1f1","IPSL-CM6A-LR":"r1i1p1f1","INM-CM5-0":"r1i1p1f1","INM-CM4-8":"r1i1p1f1","IITM-ESM":"r1i1p1f1","HadGEM3-GC31-MM":
    "r1i1p1f3","HadGEM3-GC31-LL":"r1i1p1f3","GISS-E2-1-G":"r1i1p1f2","GFDL-ESM4":"r1i1p1f1","GFDL-CM4_gr2":"r1i1p1f1","GFDL-CM4":"r1i1p1f1",
    "FGOALS-g3":"r3i1p1f1","EC-Earth3-Veg-LR":"r1i1p1f1","EC-Earth3":"r1i1p1f1","CanESM5":"r1i1p1f1","CNRM-ESM2-1":"r1i1p1f2",
    "CNRM-CM6-1":"r1i1p1f2","CMCC-ESM2":"r1i1p1f1","CMCC-CM2-SR5":"r1i1p1f1","CESM2-WACCM":"r3i1p1f1","CESM2":"r4i1p1f1","BCC-CSM2-MR":"r1i1p1f1",
    "ACCESS-ESM1-5":"r1i1p1f1","ACCESS-CM2":"r1i1p1f1"
} 


scetype = {"UKESM1-0-LL":"gn","TaiESM1":"gn","NorESM2-MM":"gn",
    "NorESM2-LM":"gn","NESM3":"gn","MRI-ESM2-0":"gn","MPI-ESM1-2-LR":"gn","MPI-ESM1-2-HR":"gn",
    "MIROC6":"gn","MIROC-ES2L":"gn","KIOST-ESM":"gr1","KACE-1-0-G":"gr","IPSL-CM6A-LR":"gr","INM-CM5-0":"gr1","INM-CM4-8":"gr1","IITM-ESM":"gn",
    "HadGEM3-GC31-MM":"gn","HadGEM3-GC31-LL":"gn","GISS-E2-1-G":"gn","GFDL-ESM4":"gr1","GFDL-CM4_gr2":"gr2","GFDL-CM4":"gr1","FGOALS-g3":"gn",
    "EC-Earth3-Veg-LR":"gr","EC-Earth3":"gr","CanESM5":"gn","CNRM-ESM2-1":"gr","CNRM-CM6-1":"gr","CMCC-ESM2":"gn","CMCC-CM2-SR5":"gn",
    "CESM2-WACCM":"gn","CESM2":"gn","BCC-CSM2-MR":"gn","ACCESS-ESM1-5":"gn","ACCESS-CM2":"gn"
} #

scens = ["ssp245"] #, "ssp245", "ssp585","historical"
vars = ["sfcWind"]#,"tasmin", "pr","tasmax","rsds","hurs","tas","sfcWind"

os.chdir("D:\\CMIP6\\")

for scen in scens:
    for var in vars:
        print("Processing {} - {}:".format(var, scen))
        for m in models:
            fpath_1 = "bbox_1\\{}\\{}\\{}\\".format(var,scen,m)
            fpath_2 = "bbox_2\\{}\\{}\\{}\\".format(var,scen,m)
            if not(os.path.exists(fpath_1)): os.makedirs(fpath_1)
            if not(os.path.exists(fpath_2)): os.makedirs(fpath_2)

            rlz = realz[m]
            stype = scetype[m]
            years = range(1950,2015) if scen == "historical" else range(2015,2101)
            eday = 30 if m in ["UKESM1-0-LL", "KACE-1-0-G", "HadGEM3-GC31-LL"] else 31
            for year in years:
                url_1 = base_url.format(m,scen, rlz, var, var, m, scen, rlz, stype, year, var, bbox_1[3],bbox_1[0],bbox_1[1],bbox_1[2],year, year, eday)
                url_2 = base_url.format(m,scen, rlz, var, var, m, scen, rlz, stype, year, var, bbox_2[3],bbox_2[0],bbox_2[1],bbox_2[2],year, year, eday)
                print("          Downloading model {} -> year {}".format(m, year))
                wget.download(url_1, out = fpath_1)
                wget.download(url_2, out = fpath_2)