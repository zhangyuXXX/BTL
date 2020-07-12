# Begin to learn Machine Learning
## 第一章 
scikit-learn(sklearn)的定位是通用机器学习库。TensorFlow(tf)的定位主要是深度学习库。
tf并未提供强大的特征工程，如纬度压缩、特征选择等。
---

1.功能不同
* 传统的机器学习：利用特征工程(feature engineering)，人为对数据进行提炼清晰
* 深度学习：利用表示学习(representation learing)，机器学习模型自身对数据进行提炼

sklearn更倾向于使用者可以自行对数据进行处理，比如选择特征、压缩纬度、转换格式，是传统机器学习库。
而以tf为代表的深度学习库会自动从数据中抽取有效特征，不需要人为来做这件事情，因为并未提供类似功能。

2.使用自由度不同
* sklearn中的模块都是高度抽象化的，所有的分类器基本都可以在3-5行内完成，
所有的转化器(如scaler和transformer)也有固定的格式。这种抽象限制了使用者的自由度，
增加了模型的效率，降低了批量化、标准化的难度

  > clf = svm.SVC()  #初始化一个分类穷                                                                                              
  > clf.fit(X_train, t_train) #训练分类器                                                                                                                      >
  > y_predict = clf.predict(X_test) #使用训练好的分类器进行预测
* tf虽然是深度学习库，但具有很高的自由度，依然可以用他做传统的机器学习所做的事情，
代价是需要自己实现算法。

---
因此从自由度角度来看，tf更高；从抽象化、封装角度来看sklearn更高；从已用性角度sklearn更高