shapeor = data.shape
 91     data = data.reshape(-1, data.shape[-1])
 92     if num_components != None:
 93         data = PCA(n_components=num_components).fit_transform(data)
 94         shapeor = np.array(shapeor)
 95         shapeor[-1] = num_components
 96     #data = MinMaxScaler().fit_transform(data)
 97     data = StandardScaler().fit_transform(data)
 98     data = data.reshape(shapeor)
 99     num_class = len(np.unique(labels)) - 1
100     return data, labels, num_class

