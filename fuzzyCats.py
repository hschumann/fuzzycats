import sys
import numpy as np
import pandas as pd

## read in the data
crime = pd.read_csv('C:/Users/Owner/Downloads/Crime_Data_Chicago.csv',low_memory = False)

## create latitude and longitude columns separately
crime['latitude'] = np.array([float(s.split(',')[0][1:]) for s in crime['Location ']])
crime['longitude'] = np.array([float(s.split(',')[1][:-1]) for s in crime['Location ']])

def L2Norm(pt1,pt2):
	distance = 0.0
	for var in pt1.columns:
		try:
			distance += (pt1[var] - pt2[var]) ** 2
		except:
			if pt1[var] != pt2[var]:
				distance += 1
	return distance ** 0.5

def getCentroids(df):
	for col in df.columns:
		np.sum(df[groupNum == ][col])
	return cent

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


cols = ['Time Occurred','Area ID','Area Name','Reporting District','Crime Code','Victim Age','Victim Sex','Victim Descent','Premise Code','Weapon Used Code','Status Code','Crime Code 1','Crime Code 2','Crime Code 3','Crime Code 4','Address	Cross Street','Location']
cluster(crime,cols,50)





## creating better groupings for crime code description
## creates many dummy variables
# def changeCrimeCode(df):
#     if "BATTERY" in df["Crime Code Description"]:
#         return "Battery"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     elif "ASSAULT" in df["Crime Code Description"]:
#         return "Assault"
#     else:
#         return "other"
    
#beer["style"] = beer.apply(style_func, axis=1)


#print(len(np.unique(list(crime['Crime Code Description']))))



#print (np.mean(crime['latitude']),np.mean(crime['longitude']))

#'Time Occurred','Area ID','Area Name','Reporting District','Crime Code','Victim Age','Victim Sex','Victim Descent','Premise Code','Premise Description','Weapon Used Code','Weapon Description','Status Code','Status Description','Crime Code 1','Crime Code 2','Crime Code 3','Crime Code 4','Address	Cross Street','Location'


