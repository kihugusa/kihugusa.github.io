library(tidyverse)
who
who1 <- who %>% 
  gather(new_sp_m014:newrel_f65, 
         key = "key", value = "cases", na.rm = TRUE)

who1 %>% 
  count(key)

who2 <- who1 %>% 
  mutate(key = stringr::str_replace(key,"newrel","new_rel"))
who2

who3 <- who2 %>% 
  separate(key, c("new","type","sexage"),
           sep = "_")
who3

who4 <- who3 %>% 
  select(-new,-iso2,-iso3)
who4

who5 <- who4 %>% 
  separate(sexage, c("sex", "age"),
           sep = 1)
who5

#Putting everything together
who %>% 
  gather(code, value, new_sp_m014:newrel_f65,
         na.rm = TRUE) %>% 
  mutate(code = stringr::str_replace(code, "newrel","new_rel")) %>% 
  separate(code, c("new","type","sexage"), sep = "_") %>% 
  select(-new,-iso2,-iso3) %>% 
  separate(sexage, c("sex","age"),sep = 1)
