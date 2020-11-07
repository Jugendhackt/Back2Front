import pandas as pd

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

#print(str(sortbycontroversial(stuff)) + "\naveragescore: " + str(averagescore(stuff)) + "\n" + str(flairpercentage(stuff)))

print(convertdates(stuff)["created_utc"])
