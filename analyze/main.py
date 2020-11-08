import pandas as pd
import matplotlib.pyplot as plt

myfile = "../data/postdata.csv"


def sortbycontroversial(data):
	return data.sort_values(by="ratio", ascending=True, key=lambda x: abs(x-0.5))

def averagescore(data):
	return data["score"].sum() / data.shape[0]

def flairpercentage(data):
	g = data["flair"]
	return pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))

def convertdates(data):
	data["created_utc"] = pd.to_datetime(data["created_utc"],unit='s')
	return(data)


stuff = pd.read_csv(myfile)
stuff = convertdates(stuff)

def plotdates(stuff):

	groupdata = stuff["flair"].groupby(stuff["created_utc"].dt.hour).count()
	index = [i for i in range(0,24)]
	groupdata.reindex(index).plot(kind="bar")
	plt.xlabel("Uhrzeit")
	plt.ylabel("Anzahl Posts")
	plt.title("Anzahl Posts in Abhängigkeit von der Uhrzeit")
	plt.show()

def flairplot(data):
	data["score"].groupby(data["flair"]).mean().plot(kind="bar")
	#data.boxplot(by=data["flair"], column="score")
	plt.show()

def ratioplot(data):
	data["score"].groupby(data["ratio"]).mean().plot()
	plt.show()

def timeplot(stuff):
	groupdata = stuff["score"].groupby(stuff["created_utc"].dt.hour).mean()
	index = [i for i in range(0,24)]
	groupdata.reindex(index).plot(kind="bar")
	plt.xlabel("Uhrzeit")
	plt.ylabel("Avg. Score")
	plt.show()
	
	
#
#print(str(sortbycontroversial(stuff)) + "\naveragescore: " + str(averagescore(stuff)) + "\n" + str(flairpercentage(stuff)))


timeplot(stuff)
#plotdates(stuff)
#print(ratioplot(stuff))
#print(stuff["created_utc"])

