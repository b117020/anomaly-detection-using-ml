from sklearn.model_selection import train_test_split
dir = "C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\train_1"

y = dir.pop('output')
X = dir

X_train,X_test,y_train,y_test = train_test_split(X.index,y,test_size=0.2)
X.iloc[X_train]