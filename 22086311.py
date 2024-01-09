#Data Source Link : https://www.kaggle.com/code/goyaladi/uber-data-analysis-predictions/input
#Github Link :

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec

#Load Data
df = pd.read_csv('UberDataset.csv')

# Set Uber color palette
uber_colors = ['#09091a' , '#c0c0c0' , '#ffe100' ,
               '#f03b37' , '#0a84ff' , '#2ab0ff']

# Create a figure and a grid layout with background color
fig = plt.figure(figsize=(15 , 10) , facecolor='white')
gs = gridspec.GridSpec(3 , 2 , height_ratios=[3 , 2 , 1])

# Title
fig.suptitle('Uber Ride Analysis Dashboard' , fontsize=18 ,
             color='#09091a' , fontweight='bold')

# Visualization 1: Distribution of Ride Purposes
ax0 = plt.subplot(gs[0 , 1] , facecolor='white')
sns.histplot(data=df , x='PURPOSE' , hue='CATEGORY' ,
             multiple='stack' , shrink=0.8 , ax=ax0 ,
             palette=uber_colors , color='olivegreen')
ax0.set_title('Distribution of Ride Purposes' , fontsize=16 ,
              fontweight='bold')
ax0.set_xlabel('Purpose')
ax0.set_ylabel('Count')
ax0.set_xticklabels(ax0.get_xticklabels() , rotation=45 ,
                    ha='right')
ax0.legend(title='Category')

# Visualization 2: Top 10 Popular Destinations
ax1 = plt.subplot(gs[1 , 0] , facecolor='#f5f5f5')
destinations = pd.concat([df['START'] , df['STOP']])
top_destinations = destinations.value_counts().head(10)
top_destinations.plot(kind='bar' , color='red' , ax=ax1)
ax1.set_title('Top 10 Popular Destinations' , fontsize=16 ,
              fontweight='bold')
ax1.set_xlabel('Destination')
ax1.set_ylabel('Count')
ax1.set_xticklabels(ax1.get_xticklabels() , rotation=45 ,
                    ha='right')

#Visualization 3 : Distribution of Ride Categories
ax2 = plt.subplot(gs[1 , 1] , facecolor='#f5f5f5')
category_counts = df['CATEGORY'].value_counts()
ax2.pie(category_counts , labels=category_counts.index , autopct='%1.1f%%' ,
        startangle=90 , colors=['green' , 'red'] ,
        wedgeprops=dict(width=0.4))
ax2.set_title('Distribution of Ride Categories' , fontsize=16 ,
              fontweight='bold')
ax2.axis('equal')
ax2.legend(category_counts.index , title='Category' ,
           loc='center left' , bbox_to_anchor=(1 , 0.5))
ax2.set_ylabel('')
ax2.set_yticks([])

# Visualization 4: Average Miles per Purpose
ax3 = plt.subplot(gs[0 , 0] , facecolor='#f5f5f5')
average_miles_per_purpose = df.groupby('PURPOSE')['MILES'].mean().sort_values()
average_miles_per_purpose.plot(kind='barh' , color='green' , ax=ax3)
ax3.set_title('Average Miles per Purpose' , fontsize=16 , fontweight='bold')
ax3.set_xlabel('Average Miles')
ax3.set_ylabel('Purpose')

#Analysis:
ax4 = plt.subplot(gs[2 , 0] , facecolor='#f5f5f5')
text = "1. Business meetings are the most frequent ride purpose with a count of 175.\n" \
       "2. Cary is the most popular location for rides with a count of 400 rides.\n" \
       "3. 93.3% rides are business category rides whereas 6.7% are personal rides.\n" \
       "4. Commute is the longest ride category.\n" \

ax4.text(0.5 , 0.5 , text , ha='center' , va='center' , fontsize=14 ,
         color='#09091a', wrap=True)
ax4.axis('off')

#Student details
ax5 = plt.subplot(gs[2 , 1] , facecolor='#f5f5f5')
text = "Student name : Sanghavi Rangineni\n" \
       "Student id : 22086311"
ax5.text(0.5 , 0.5 , text , ha='center' , va='center' , fontsize=14 ,
         color='#09091a' , wrap=True ,fontweight='bold')
ax5.axis('off')


# Save or display the dashboard
plt.tight_layout(rect = [0, 0, 1, 0.92])  # Adjust layout for the title
plt.savefig('22086311.png' , dpi = 300)  # Save the dashboard as an image
# plt.show()
