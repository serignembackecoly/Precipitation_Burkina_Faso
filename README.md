## Assessing Climate Change Impacts on Precipitation in Burkina Faso

### Project Overview

This repository contains the code and data for assessing the impact of climate change on precipitation patterns in Burkina Faso. The analysis focuses on two time periods: 1981-2014 (historical period) and 2025-2050 (future period).

**Data:**

* **CHIRPS:** Climate Hazards Group InfraRed Precipitation with Stations data for the historical period (1981-2014).
* **CMIP6 NASA-NEXX-GDP:** Climate Model Intercomparison Project Phase 6 data for the future period (2025-2050).

**Methodology:**

1. **Data Preprocessing:**
   * Download and preprocess CHIRPS and CMIP6 data using R packages like `raster` and `ncdf4`.
   * Ensure consistency in spatial and temporal resolution.
   * Apply quality control procedures to remove outliers and inconsistencies.
2. **Climate Index Calculation:**
   * Calculate the following ETCCDI (Expert Team on Climate Change Detection and Indices) precipitation indices using R packages like `climdex` and `doParallel` for parallel processing:
     * Annual total precipitation
     * Maximum 1-day precipitation
     * Number of wet days
     * Consecutive dry days
     * Precipitation concentration index
3. **Trend Analysis:**
   * Apply trend analysis techniques (e.g., Mann-Kendall test) using R packages like `trend` and `Kendall`.
4. **Spatial Analysis:**
   * Create maps to visualize spatial patterns of precipitation changes using R packages like `ggplot2` and `raster`.
5. **Statistical Analysis:**
   * Conduct statistical tests to determine the significance of changes in precipitation indices using R's built-in statistical functions.

**Code Structure:**

* **Data:** Folder containing the downloaded and processed data.
* **Codes:** Folder containing the R scripts for data preprocessing, index calculation, statistical analysis, and visualization.
* **Figures:** Folder to store the output files, including plots, tables, and maps.
* **Report:** The final report summarizing the findings of the analysis.

**Requirements:**

* **R:** Essential for data analysis and visualization.
* **R packages:** `raster`, `ncdf4`, `climdex`, `doParallel`, `trend`, `Kendall`, `ggplot2`, and `raster`.
* **wget:** For downloading data from the web.

**To run the code:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/climate-change-burkina-faso.git
   ```
2. **Set up the R environment:**
   Ensure you have the required R packages installed. You can use package management tools like `install.packages()` to install them.
3. **Run the R scripts:**
   Execute the R scripts in the `R` folder, following the provided instructions.


