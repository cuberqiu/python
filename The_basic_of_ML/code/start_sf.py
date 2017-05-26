# coding:utf-8s
import graphlab

sf = graphlab.SFrame('/home/wsn/Documents/python/The_basic_of_ML/people-example.csv')

# SFrame basics
sf.head()

# Graphlab Canvas
sf.show()
graphlab.canvas.set_target('ipynb')
sf['age'].show(view='Categorical')

# Inspect columns of dataset

sf['Country']

sf['age'].max()
sf['age'].mean()

# Create new columns in our SFrame
sf['Full name'] = sf['First Name'] + ' ' + sf['Last Name']
sf

sf['age'] -= 10
sf
sf['age'] +=10
sf

# use apply() function to do a advance transformation of our data
sf['Country']
sf['Country'].show()
