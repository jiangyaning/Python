from sklearn.model_selection import train_test_split
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer
from sklearn.externals import joblib

boston=datasets.load_boston()
#print(iris)
boston_X=boston.data
#print(iris_X)
boston_y=boston.target
#将导入的数据集分为训练集与测试集
X_train,X_test,y_train,y_test=train_test_split(boston_X,boston_y,test_size=0.2)
#print(y_train)
#训练回归模型
regr=linear_model.LinearRegression()
regr.fit(X_train,y_train)
y_predict=regr.predict(X_test)
# print(y_predict)
# print(y_test)
#均方误差
print("均方误差:",mean_squared_error(y_test,y_predict))
#使用K折交叉验证模块
scores=cross_val_score(regr,boston_X,boston_y,cv=5)
#print(scores)
print("Accuracy:%0.2f(+/-%0.2f)"%(scores.mean(),scores.std()*2))
print("准确率：%f"%regr.score(X_test,y_test))
#保存模型
# joblib.dump(regr,'boston_house_price.pkl')
# clf3=joblib.load('boston_house_price.pkl')
# print(clf3.predict(boston_X[0:1]))