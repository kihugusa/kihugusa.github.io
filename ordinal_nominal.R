gender <- c("F", "F", "M", "F")
gender_f <- factor(gender, levels = c("F","M"), labels = c("Female","Male"))
# gender_f
salary <- c("Low", "Low", "Medium", "High", "Medium", "Low")
salary_f <- factor(salary)
salary_ordered <- ordered(salary,levels = c("Low","Medium","High"))
salary_ordered