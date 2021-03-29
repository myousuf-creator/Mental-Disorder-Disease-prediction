import pandas as pd

import joblib
import config


def make_prediction(input_data):

	data = pd.DataFrame(input_data,index=[0])
	_pipe_price = joblib.load(filename=config.PIPELINE_NAME)
	prediction = _pipe_price.predict(data[config.FEATURES])
	pred = prediction.toarray()

	output = []
	for i,v in enumerate(pred):
		index_list = [j for j, value in enumerate(pred[i]) if value == 1]
		class_list = [config.CLASS_LIST[i] for i in index_list]
		output.append(class_list)

	results = {"predictions": output}

	return results
   
# if __name__ == '__main__':
# 	make_prediction()
    
    # test pipeline
    # import numpy as np
    # from sklearn.model_selection import train_test_split
    # from sklearn.metrics import accuracy_score

    # data = pd.read_csv(config.TRAINING_DATA_FILE)

    # X_train, X_test, y_train, y_test = train_test_split(
    #     data[config.FEATURES],
    #     data[config.TARGET],
    #     test_size=0.1,
    #     random_state=0)
    
    # pred = make_prediction(X_test[0:1])

    # print(pred)
    
    # final = []
    # for i,v in enumerate(pred):
    #     index_list = [j for j, value in enumerate(pred[i]) if value == 1]
    #     class_list = [config.TARGET[i] for i in index_list]
    #     final.append(class_list)
    # print(final)

    # determine mse and rmse
    # print('test mse: {}'.format(int(
    #     mean_squared_error(y_test, np.exp(pred)))))
    # print('test rmse: {}'.format(int(
    #     np.sqrt(mean_squared_error(y_test, np.exp(pred))))))
    # print('test r2: {}'.format(
    #     r2_score(y_test, np.exp(pred))))
    # print()

    #print('accuracy_score : {}'.format((accuracy_score(y_test,pred))))

