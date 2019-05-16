def model_train():
    import pickle

    from random import randint
    TRAIN_SET_LIMIT = 1000
    TRAIN_SET_COUNT = 100

    TRAIN_INPUT = list()
    TRAIN_OUTPUT = list()
    for i in range(TRAIN_SET_COUNT):
        a = randint(0, TRAIN_SET_LIMIT)
        b = randint(0, TRAIN_SET_LIMIT)
        c = randint(0, TRAIN_SET_LIMIT)
        op = a + (2*b) + (3*c)
        TRAIN_INPUT.append([a, b, c])
        TRAIN_OUTPUT.append(op)

    from sklearn.linear_model import LinearRegression

    predictor = LinearRegression(n_jobs=-1)
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

    filename = 'finalized_model4.sav'
    pickle.dump(predictor, open(filename, 'wb'))

def model_predict(a,b,c):
    import pickle
    a,b,c=int(a),int(b),int(c)
    filename= 'finalized_model4.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[a,b,c]])
    return result
