library(tidyverse)
class(economics$date)

# Today's date
Sys.Date()

# Converts strings to dates
as.Date("1/1/80", format = "%m/%d/%y")
as.Date("1970/1/1") # string must be in "y/m/d"

dt <- as.Date("1-1-70", format = "%m-%d-%y")
as.numeric(dt) # Returns 0 because it stores no. of days till 1970

dt <- as.Date("1/1/2001", format = "%m/%d/%y")
dt + 100 # "2001-04-11"
dt + 31 # "2001-02-01"

d1 <- as.Date("1980/1/1")
d2 <- as.Date("1982/1/1")
d3 <- as.Date("1980/1/5")
seq(d1,d3,"day")

seq(from = d1, by = "4 months", length.out = 4)

# Generating the second element of the 3 weeks sequence from d1
seq(from = d1, by = "3 weeks", length.out = 2)[2]

# Line plots
a <- ggplot(economics, aes(date,uempmed))+
          geom_line()
b <- ggplot(economics, aes(date, unemploy/pop))+
          geom_line()

library(gridExtra)
grid.arrange(a, b)

year <- function(x) as.POSIXlt(x)$year + 1900
ggplot(economics, aes(unemploy/pop, uempmed, color = year(date)))+
  geom_point()+
  geom_path()

# geom_path() connects points by their order of appearance in the data

#gp <- read.csv("gas-price-series.csv")
#class(gp$date) ##factor
#gp <- read.csv("gas-price-series.csv", 
#               stringsAsFactors = FALSE)
#gp$date_converted <- as.Date(gp$date, format = "%m/%d/%Y")
#class(gp$date_converted) # Date

