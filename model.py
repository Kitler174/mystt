import sqlite3
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pickle 

def fetch_data():
    conn = sqlite3.connect('baza.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT data3, key FROM dane ORDER BY key ASC")
    rows = cursor.fetchall()
    conn.close()
    keyy=[]
    data=[]
    for r in rows:
        print(r)
        data.append(eval(r[0]))
        keyy.append(r[1])
    return data,keyy

def model():
    d,k = fetch_data()
    rc = XGBClassifier(eta=0.1,min_child_weight=2,colsample_bytree=0.5,reg_alpha=0,reg_lambda=0, max_depth=10, gamma=0)
    X_train, x_test, y_train, y_test = train_test_split(d, k, test_size=0.1)
    rc.fit(X_train,y_train)
    with open("model.pkl", "wb") as f:
        pickle.dump((rc),f)

if __name__ == "__main__":
    model()