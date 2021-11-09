library(ggplot2)
library(readr)

data <- read_csv("C:\\Users\\rudra\\Desktop\\college things\\senior\\comps\\CS399.02\\scripts\\10_20_hashir_new.csv")
data <- `10_20_hashir_new`

ggplot(data) + 
  geom_bar(aes(x = reorder(ips, size), y = size), stat = "identity") + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))+ 
  labs(x = "ips")

ggplot(data) + 
  geom_bar(aes(x = reorder(ips, length), y = length), stat = "identity") + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) + 
  labs(x = "ips")

