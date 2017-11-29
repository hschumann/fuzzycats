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
	df['Time Occurred'][np.where(df['Time Occurred'] < 800)] = 2400 - (800 - df['Time Occurred'])
	df['Time Occurred'][np.where(df['Time Occurred'] >= 800)] = df['Time Occurred'] - 800

## make sex binary!
def newSex(df):
	if df['Victim Sex'] == 'M':
		df['Sex'] = 1
	else:
		df['Sex'] = 0

## clean age (remove missing values)
def cleanAge(df):
	if df['Victim Age'] == '':
		df['Age'] = np.mean(df['Victim Age'])
	
## normalize all the variables
def normalizeDF(df,columns):
	for col in columns:
		df[col] = df[col] / np.max(df[col])

## distance formula
def L2Norm(pt1,pt2):
	distance = 0.0
	for var in pt1.columns:
		distance += (pt1[var] - pt2[var]) ** 2
	return distance ** 0.5

def L1Norm(pt1,pt2):
	distance = 0.0
	for var in pt1.columns:
		distance += abs(pt1[var] - pt2[var])
	return distance

## getting the new centroids
def getCentroids(df,k):
	for i in range(k):
		for col in df.columns:
			cent[i][col] = np.sum(df[col]) / len(df[col])
	return cent

## classifies points
def classifyPoint(centroids,point):
	smallestDist = np.inf
	closest = 0
	i = 0
	for c in centroids:
		i += 1
		temp = L2Norm(c,point)
		if temp < smallestDist:
			closest = i
			smallestDist = temp

## the big function
def cluster(df,columns,k):
	## pick k random points from the data set
	firstIDs = np.random.randint(np.len(df),size = k)
	## set centroids
	centroids = df[firstIDs,columns]
	while True:
		for obs in df:
			classifyPoint(centroids,obs)
		newCentroids = getCentroids(df)
		if (centroids == newCentroids):
			break
		else:
			centroids = newCentroids
	return df

## columns we wanna use
cols = ['Time Occurred','Area ID','Reporting District','Crime Code','Victim Age','Victim Sex','Premise Code','latitude','longitude']

## data cleaning
newTimes(crime)
newSex(crime)
cleanAge(crime)

cluster(crime,cols,50)






