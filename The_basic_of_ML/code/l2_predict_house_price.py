import graphlab

# load some house sales dataset

sales = graphlab.SFrame('/home/wsn/Documents/python/The_basic_of_ML/class_file/home_data.gl/')

sales
# Exploring the data for housing sales
sales.show(view="Scatter PLot",x="sqft_living",y="price")

# split train_data and test_data
# random_split(fraction,seed=None)
train_data,test_data = sales.random_split(.8,seed=0)

advanced_features = [
                    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
                    'condition', # condition of house
                    'grade', # measure of quality of construction
                    'waterfront', # waterfront property
                    'view', # type of view
                    'sqft_above', # square feet above ground
                    'sqft_basement', # square feet in basement
                    'yr_built', # the year built
                    'yr_renovated', # the year renovated
                    'lat', 'long', # the lat-long of the parcel
                    'sqft_living15', # average sq.ft. of 15 nearest neighbors
                    'sqft_lot15', # average lot size of 15 nearest neighbors
                    ]

# create(dataset,target,features = None)
advanced_features_model = graphlab.linear_regression.create(train_data,target='price',features = advanced_features,validation_set=None)


house1 = sales[sales['id']=='2414600126']
house2 = sales[sales['id']=='3793500160']

print house1['price']
print house2['price']
print advanced_features_model.predict(house1)
print advanced_features_model.predict(house2)


print sales['price'].max()
