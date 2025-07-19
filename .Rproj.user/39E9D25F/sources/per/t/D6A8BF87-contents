# Load CSV file
df <- read.csv("website_traffic_dataset.csv")

# View top rows
head(df)

# View structure
str(df)

# Summary
summary(df)

# Clean column names using janitor
install.packages("janitor")
library(janitor)
df <- clean_names(df)

# Simple histogram
hist(df$page_views)

df$timestamp <- seq.POSIXt(from = as.POSIXct("2023-01-01"), by = "hour", length.out = nrow(df))

# Time series plot (if you have timestamp)
plot(df$timestamp, df$page_views, type = "l")

df$date <- as.Date(df$timestamp)

library(dplyr)

daily_views <- df %>%
  group_by(date) %>%
  summarise(page_views = sum(page_views))  # or use mean(page_views)

daily_views

plot(daily_views$date, daily_views$page_views, type = "h", col = "blue",
     main = "Daily Page Views",
     xlab = "Date", ylab = "Total Page Views")


plot(df$timestamp, df$page_views, type = "l", col = "blue", main = "Page Views Over Time", xlab = "Time", ylab = "Page Views")


length(df$timestamp)
length(df$page_views)

summary(df$page_views)
summary(df$bounce_rate)

# Select numeric columns
numeric_df <- df[, sapply(df, is.numeric)]

# Compute correlation
cor_matrix <- cor(numeric_df, use = "complete.obs")

# Plot
install.packages("corrplot")   # if not installed
library(corrplot)
corrplot(cor_matrix, method = "number",method = "colour", type = "upper")

table(df$traffic_source)
barplot(table(df$traffic_source), main = "Traffic Source Distribution", col = "skyblue")

library(dplyr)

avg_bounce_df <- df %>%
  group_by(traffic_source) %>%
  summarise(avg_bounce = mean(bounce_rate, na.rm = TRUE))

barplot(
    height = avg_bounce_df$avg_bounce,
    names.arg = avg_bounce_df$traffic_source,
    col = "orange",
    main = "Avg Bounce Rate by Traffic Source"
  )

hist(df$session_duration,
     main = "Distribution of Session Duration",
     xlab = "Duration (seconds)",
     col = "skyblue",
     border = "white")

boxplot(time_on_page ~ traffic_source,
        data = df,
        col = "lightgreen",
        main = "Time on Page by Traffic Source",
        xlab = "Traffic Source",
        ylab = "Time on Page")

plot(df$time_on_page, df$conversion_rate,
     main = "Time on Page vs Conversion Rate",
     xlab = "Time on Page",
     ylab = "Conversion Rate",
     col = "purple",
     pch = 19)

cor(df$conversion_rate, df$time_on_page, use = "complete.obs")  # Example
cor(df$conversion_rate, df$session_duration, use = "complete.obs")


cor(numeric_df, use = "complete.obs")



