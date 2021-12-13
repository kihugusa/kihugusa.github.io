library(tidyverse)
sales <- read_csv("sales-data-wide.csv")
sales %>% 
  gather(`2015`:`2019`, key = "year", value = "qtd_sold"
  )

sales_long <- read_csv("sales-data-long.csv")
sales_long %>% 
  spread(year, qty_sold)

diamonds %>% 
  mutate(ppc = price/carat) %>% 
  group_by(cut) %>% 
  summarize(avg_ppc = mean(ppc))

diamonds %>% 
  group_by(color) %>% 
  filter(n() > 6000) %>% 
  arrange(color)

diamonds %>% 
  summarize(n = n(), price_10000 = sum(price > 10000), prop = price_10000/n)

diamonds %>% 
  group_by(cut) %>% 
  summarize(avg_ppc = mean(price/carat))