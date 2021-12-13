#install.packages("palmerpenguins")
library(palmerpenguins)
library(tidyverse)
library(lubridate)

penguins %>% 
  ggplot(aes(flipper_length_mm, body_mass_g)) + 
  geom_point(aes(shape = species, color = species))+
  geom_smooth(se=FALSE)+
  facet_wrap(~species)

penguins %>% 
  drop_na(sex) %>% 
  ggplot(aes(flipper_length_mm, body_mass_g))+
  geom_point(aes(color = species, shape = species))+
  facet_wrap(~sex)