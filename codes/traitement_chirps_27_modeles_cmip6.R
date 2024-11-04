# Traitements des données chirps et cmip6

# Librairies
library(sf)
library(raster)
library(hydroGOF)
library(tidyverse)
library(reshape2)
library(verification)

# Repertoire de travail
setwd("E:/Etude/Donnees/")
# Repertoire de figures
figs_path <- "figures/"
# Ouvrir les données
fichiers <- list.files() 
# [1] "masked_sum_mon_ACCESS-CM2.nc"       "masked_sum_mon_ACCESS-ESM1-5.nc"   
# [3] "masked_sum_mon_CanESM5.nc"          "masked_sum_mon_chirps.nc"          
# [5] "masked_sum_mon_CMCC-CM2-SR5.nc"     "masked_sum_mon_CMCC-ESM2.nc"       
# [7] "masked_sum_mon_CNRM-CM6-1.nc"       "masked_sum_mon_CNRM-ESM2-1.nc"     
# [9] "masked_sum_mon_EC-Earth3-Veg-LR.nc" "masked_sum_mon_EC-Earth3.nc"       
# [11] "masked_sum_mon_FGOALS-g3.nc"        "masked_sum_mon_GFDL-ESM4.nc"       
# [13] "masked_sum_mon_GISS-E2-1-G.nc"      "masked_sum_mon_HadGEM3-GC31-LL.nc" 
# [15] "masked_sum_mon_INM-CM4-8.nc"        "masked_sum_mon_INM-CM5-0.nc"       
# [17] "masked_sum_mon_IPSL-CM6A-LR.nc"     "masked_sum_mon_KACE-1-0-G.nc"      
# [19] "masked_sum_mon_KIOST-ESM.nc"        "masked_sum_mon_MIROC-ES2L.nc"      
# [21] "masked_sum_mon_MIROC6.nc"           "masked_sum_mon_MPI-ESM1-2-HR.nc"   
# [23] "masked_sum_mon_MPI-ESM1-2-LR.nc"    "masked_sum_mon_MRI-ESM2-0.nc"      
# [25] "masked_sum_mon_NorESM2-LM.nc"       "masked_sum_mon_NorESM2-MM.nc"      
# [27] "masked_sum_mon_TaiESM1.nc"          "masked_sum_mon_UKESM1-0-LL.nc"

chirps <- brick("masked_sum_mon_chirps.nc")

df_rmse <- function(nc_path) {
  modele1 <- brick(nc_path)
  
  # Extraction des données de pluie en vecteur
  pr_c <- getValues(chirps)
  observed <- as.vector(pr_c)
  pr_m1 <- getValues(modele1)
  modeled <- as.vector(pr_m1)
  
  #Suppression des NA
  observed <- observed[!is.na(observed)]
  modeled <- modeled[!is.na(modeled)]
  
  #### Visualisations ####
  # Compute the difference between the two rasters
  difference <- chirps - modele1
  
  # Compute the squared difference
  squared_difference <- difference^2
  
  # Compute the mean squared difference
  mean_squared_difference <- mean(squared_difference, na.rm = TRUE)
  
  # Compute the RMSE
  root_mean_square <- sqrt(mean_squared_difference)
  
  # Convert the raster to a dataframe
  df <- as.data.frame(root_mean_square, xy = TRUE)
  
  # Melt the dataframe for ggplot
  df_melt <- melt(df, id.vars = c("x", "y"))
  
  df_melt<- df_melt[complete.cases(df_melt),]
  # Add a column for the model name
  model_name <- strsplit(nc_path, "_")
  model_name <- strsplit(model_name[[1]][4], "[.]")
  model_name <- model_name[[1]][1]
  df_melt<- cbind(df_melt, model = rep(model_name, nrow(df_melt)))
}

# Checking if the function work
dff <- df_rmse(fichiers[2])

# Create a big dataframe of all the models
output_list <- lapply(fichiers[-4], df_rmse) # fichiers[-4] to not consider chirps data
combined_dataframe <- do.call(rbind, output_list)


# Create the ggplot
# Read the shapefile
shapefile <- st_read("data/regions.shp")
jet_palette <- c("#00008F", "#0000FF", "#0080FF", "#00FFFF", "#80FF80", "#FFFF00", "#FF8000", "#FF0000", "#800000")

# let's do it
rmse_plot <- ggplot() +
  geom_raster(data = combined_dataframe, aes(x = x, y = y, fill = value)) +
  scale_fill_gradientn(name = "RMSE", colours = jet_palette) +
  geom_sf(data = region, color = "black", fill = NA) +
  labs(title = "Root Mean Square Error (RMSE) Spatial Visualization",
       x = "Longitude",
       y = "Latitude") +
  facet_wrap(~model) +
  ggthemes::theme_tufte() +
  theme(legend.background = element_rect(colour = "black"))

# save the figure
ggsave("rmseChirpsVsModels.png", rmse_plot, path = figs_path, type = "cairo",
       dpi = 400, height = 8, width = 12)

