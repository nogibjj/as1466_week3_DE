#import pandas as pd
#df = pd.read_csv('bmi.csv')

#function to populate all descriptive statistics
def stats(df): 
  return df.describe()
#function  to return mean of a Series 
def mean(series):
  return series.mean()
#function to return median of Series 
def median(series): 
  return series.median()
#function to return standard deviation of statistics 
def std(series):
  return series.std()
  
#main script
import polars as pl 
import matplotlib.pyplot as plt
import seaborn as sns 

#reading csv file
data = pl.read_csv('bmi.csv')

#generate summary statistics 
stats1 = stats(data)
#generate boxplot 
boxplots = sns.boxplot(data[:, :4])
plt.savefig('boxplots.png')
#generate pairplot for variables correlations
d = data.to_pandas()
pairplot = sns.pairplot(d, hue="BmiClass")
plt.savefig('pairplot.png')

s = stats(data)
string = f'''
# This is the generated report for summary statistics and data visualization for [bmi.csv](https://github.com/nogibjj/as1466_week2_DE/blob/main/bmi.csv) file

## Overall dataset descriptive statistics

{s.to_markdown()}

## Here are some data visualizations of data to understand relationships between variables

### Boxplots of each variable
![Boxplot](boxplots.png)



### Pairplots of correlation between numerical variables, segmented by BMI segment

![Variable Correlations](pairplot.png)

'''
# Specify the file path where you want to create the Markdown file
file_path = "Statistics_report.md"

# 
with open(file_path, "w", encoding="utf-8") as md_file:
    md_file.write(string)

