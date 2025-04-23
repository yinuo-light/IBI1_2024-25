import os
import pandas as pd
import matplotlib.pyplot as plt

# Change the working directory to where the data file is located
os.chdir(r"C:\Users\admin\Desktop\ibi\IBI1_2024-25\Practical10")
# Load the DALYs data from the CSV file into a pandas DataFrame
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Use a Boolean to extract the 'Year' column for Afghanistan 
AFG_data= dalys_data[dalys_data['Entity'] == 'Afghanistan']['Year']
# print the first 10 lines
print(AFG_data.iloc[0:10])
print("The 10th year with DALYs data recorded in Afghanistan is 1999.")

# Use a Boolean to select the lines which year is 1990, and extract their Entity and DALYs
dalys_1990 = dalys_data.loc[dalys_data['Year'] == 1990, ['Entity', 'DALYs']]
print("DALYs of 1990：")
print(dalys_1990)

# Use a Boolean to select the lines of UK and France, and extract their DALYs
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']['DALYs']
france_data = dalys_data[dalys_data['Entity'] == 'France']['DALYs']
# Calculate their mean values
mean_uk = uk_data.mean()
mean_france = france_data.mean()
print(f"Average DALYs in the UK: {mean_uk}")
print(f"Average DALYs in France: {mean_france}")

# Judge the size of the two mean values
if mean_uk > mean_france:
    print("Average DALYs in the UK is larger than France")
else:
    print("Average DALYs in the UK is lower than France")

# Darw a plot for the DALYs of the UK
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over Time in the UK')
plt.show()


# The code for the question: What country or countries have recorded a DALYs greater than 650,000 in a single year?
high_dalys_data = dalys_data[dalys_data['DALYs'] > 650000]
countries = high_dalys_data['Entity'].unique()
print("countries have recorded a DALYs greater than 650,000 in a single year:", countries)
