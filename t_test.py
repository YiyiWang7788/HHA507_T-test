# -*- coding: utf-8 -*-
"""T-test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1citOOIQyeV-KTy97X0TgvqdxZek-ZTjm
"""

import pandas as pd
from scipy.stats import shapiro 
from matplotlib import pyplot
import scipy.stats as stats
from scipy.stats import ttest_ind

## print dataframe and show a small sample of the dataframe
diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(50)
diabetes_small

##show list of variables in the dataframe
list(diabetes_small)

##1) Is there a difference between sex (M:F) and the number of days in hospital?
Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

### t-test to find the t-score and p value
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])
### the result for question 1 is p-value = 1.4217299655114968e-21, T-score= 9.542637042242887
## p < 0.05, t-score is high, therefore  significant difference between male and female for number of days in the hospital

##2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
Caucasian = diabetes[diabetes['race']=='Caucasian']
## T-test
ttest_ind(AfricanAmerican['time_in_hospital'], Caucasian['time_in_hospital'])
## the t-score is high as 5.0610017032095325, p= 4.178330085585203e-07 and p < 0.05, therefore there is a significant difference between RACE (Caucasian and African American) and the number of days in hospital.

##3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
Asian = diabetes[diabetes['race']=='Asian']
#T-test
ttest_ind(AfricanAmerican['num_lab_procedures'], Asian['num_lab_procedures'])
## t-score is 3.9788715315360292, p is 6.948907528800307e-05 which is smaller than 0.05, therefore there is a significant difference between RACE (Asian and African American) and the number of lab procedures performed