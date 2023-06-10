getwd()

setwd("~/PRIVATE FOLDER/TETRIS PROGRAM BATCH 3/Capstone Project")

library(dplyr)
library(ggplot2)
library(gganimate)

df <- read.csv("Data Ekspor Impor 2014-2023.csv")
pivot_df <- read.csv("Pivot Data Ekspor Impor 2014-2023.csv")
head(df)
head(pivot_df)

plot <- df %>%
  ggplot(aes(x = Nilai.Impor..US..., y = Nilai.Ekspor..US..., size = Berat.Ekspor..KG., color = Tahun)) + 
  geom_point(alpha = 0.9) + theme(panel.background = element_rect(fill = "black"),
                                  axis.line = element_line(color = "black"),
                                  axis.text = element_text(color = "white")) + 
  ggtitle('Nilai Ekspor vs. Nilai Impor') + 
  labs(x = 'Nilai Impor (USD)', y = 'Nilai Ekspor (USD)') + 
  transition_time(Tahun) + 
  shadow_mark(alpha = 0.5, size = 0.5) +
  ggtitle("Hubungan Nilai Ekspor vs. Nilai Impor", subtitle = "Tahun: {frame_time}")

animate(plot, renderer = gifski_renderer())
anim_save("Nilai Ekspor vs Nilai Impor.gif", plot, bg = "transparent")

plot <- df %>%
  ggplot(aes(x = Berat.Impor..KG., y = Berat.Ekspor..KG., size = Nilai.Ekspor..US..., color = Tahun)) + 
  geom_point(alpha = 0.9) + theme_bw() + 
  ggtitle('Berat Ekspor vs. Berat Impor') + 
  labs(x = 'Berat Ekspor (kilogram)', y = 'Berat Ekspor (kilogram)') + 
  transition_time(Tahun) + 
  shadow_mark(alpha = 0.5, size = 0.5) +
  ggtitle("Hubungan Berat Ekspor vs. Berat Impor", subtitle = "Tahun: {frame_time}")

animate(plot, renderer = gifski_renderer())
anim_save("Berat Ekspor vs Berat Impor.gif", plot, bg = "transparent")

