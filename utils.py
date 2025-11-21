import numpy as np

def split_data(X,y,test_size=0.1):  

    # copy the data
    X = np.copy(X)
    y = np.copy(y)

    # find the split index
    n_items = len(X)
    np.random.shuffle(X), np.random.shuffle(y)   
    split_idx  = int(n_items * test_size)

    # split the data
    X_train,X_test = X[split_idx:],X[:split_idx]
    y_train,y_test = y[split_idx:],y[:split_idx]

    return X_train,X_test,y_train,y_test