# Convert a nested list to a data frame.

continents <- list(
    list(continent = "Asia", area = 31.0, population = 3261),
    list(continent = "Africa", area = 29.6, population = 1341),
    list(continent = "Europe", area = 22.1, population = 748),
    list(continent = "North America", area = 21.3, population = 592),
    list(continent = "South America", area = 17.5, population = 431),
    list(continent = "Australia", area = 8.5, population = 43),
    list(continent = "Antarctica", area = 13.7, population = 0)
)

# Method 1
#
# This is a base R solution and doesn't require any packages.
#
do.call(rbind, lapply(continents, data.frame))

# Method 2
#
library(dplyr)
#
bind_rows(continents)

# Method 3
#
library(purrr)
#
continents %>% map_dfr(identity)