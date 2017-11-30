import sys
import numpy as np
import pandas as pd

## read in the data
crime = pd.read_csv('C:/Users/Owner/Downloads/Crime_Data_Chicago.csv',low_memory = False)

## create latitude and longitude columns separately
crime['latitude'] = np.array([float(s.split(',')[0][1:]) for s in crime['Location ']])
crime['longitude'] = np.array([float(s.split(',')[1][:-1]) for s in crime['Location ']])

## rescale time variable
def newTimes(df):
	df['Time Occurred'][np.where(df['Time Occurred'] < 800)[0]] = 2400 - (800 - df['Time Occurred'][np.where(df['Time Occurred'] < 800)[0]])
	df['Time Occurred'][np.where(df['Time Occurred'] >= 800)[0]] = df['Time Occurred'][np.where(df['Time Occurred'] >= 800)[0]] - 800
	
## make sex binary!
def newSex(df):
	df['Sex'] = np.zeros(len(df['Victim Sex']))
	df['Sex'][np.where(df['Victim Sex'] == 'M')[0]] = 1
	df['Sex'][np.where(df['Victim Sex'] == 'F')[0]] = 0
	df['Sex'][np.where(df['Victim Sex'] == '')[0]] = 0

## clean age (remove missing values)
def cleanAge(df):
    meanAge = np.mean(df['Victim Age'])
	df['Victim Age'][np.isnan(df['Victim Age'])] = meanAge
	
## normalize all the variables
def normalizeDF(df,columns):
    df = (df - df.mean()) / (df.max()) 
	#for col in columns:
		#df[col] = df[col] / np.max(df[col])

## distance formulas
def L2Norm(pt1,pt2):
	# distance = 0.0
	return np.sum((pt1.values[0] - pt2.values[0]) ** 2)
	# for var in pt1.columns:
	# 	print (pt1[var] - pt2[var])
	# 	distance += (pt1[var] - pt2[var]) ** 2
	# return distance ** 0.5

def L1Norm(pt1,pt2):
	distance = 0.0
	for var in pt1.columns[0]:
		distance += abs(pt1[var] - pt2[var])
	return distance

## getting the new centroids
def getCentroids(df,k):
	for i in range(k):
		for col in df.columns:
			cent[i][col] = np.sum(df[col]) / len(df[col])
	return cent

## classifies points
def classifyPoint(df,centroids,point):
	smallestDist = np.inf
	closest = 0
	i = 0
	for c in range(len(centroids)):
		i += 1
		if i%1000 == 0:
			print ("Hans")
		temp = L2Norm(centroids.iloc[[c]],df.iloc[[point]])
		if temp < smallestDist:
			closest = i
			smallestDist = temp
	df.iloc[[point]]['Class'] = closest

# def classifyPoints(df,centroids):


## the big function
def cluster(df,columns,k):
	df = df[columns]
	## pick k random points from the data set
	firstIDs = np.random.randint(len(df),size = k)
	## set centroids
	centroids = df.iloc[firstIDs]
	## run until clusters don't change (hopefully not forever)
	while True:
		# print ("Here")
		df['Class'] = np.zeros(len(df))
		centroids['Class'] = np.zeros(len(centroids))
		for i in range(len(df)):
			classifyPoint(df,centroids,i)
		newCentroids = getCentroids(df,columns)
        # maybe check if it hits a certain threshold?
		if (centroids == newCentroids):
			break
		else:
			centroids = newCentroids
	return df

## columns we wanna use
cols = ['Time Occurred','Area ID','Reporting District','Crime Code','Victim Age','Sex','Premise Code','latitude','longitude']

## data cleaning
newTimes(crime)
newSex(crime)
cleanAge(crime)

## still need to fix and use the normalizing of variables

cluster(crime,cols,50)




