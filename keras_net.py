import keras as k
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_frame = pd.read_csv("keras_net.csv")
input_names = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
output_names = ["res"]

encoders = {"4": lambda four: {1: [1], 2: [0]}.get(four),
            "5": lambda five: {1: [1], 2: [0]}.get(five),
            "6": lambda six: {1: [1], 2: [0]}.get(six),
            "7": lambda seven: {1: [1], 2: [0]}.get(seven),
            "8": lambda eight: {1: [1], 2: [0]}.get(eight),
            "9": lambda nine: {1: [1], 2: [0]}.get(nine),
            "10": lambda ten: {1: [1], 2: [0]}.get(ten),
            "11": lambda eleven: {1: [1], 2: [0]}.get(eleven),
            "12": lambda twelve: {1: [1], 2: [0]}.get(twelve),
            "13": lambda thirteen: {1: [1], 2: [0]}.get(thirteen),
            "14": lambda fourteen: {1: [1], 2: [0]}.get(fourteen),
            "15": lambda fifteen: {1: [1], 2: [0]}.get(fifteen),
            "16": lambda sixteen: {1: [1], 2: [0]}.get(sixteen),
            "17": lambda seventeen: {1: [1], 2: [0]}.get(seventeen),
            "18": lambda eighteen: {1: [1], 2: [0]}.get(eighteen),
            "19": lambda nineteen: {1: [1], 2: [0]}.get(nineteen),
            "res": lambda s_value: [s_value]}


def dataframe_to_dict(df):
    result = dict()
    for column in df.columns:
        values = data_frame[column].values
        result[column] = values
    return result


def make_supervised(df):
    raw_input_data = data_frame[input_names]
    raw_output_data = data_frame[output_names]
    return {"inputs": dataframe_to_dict(raw_input_data),
            "outputs": dataframe_to_dict(raw_output_data)}


def encode(data):
    vectors = []
    for data_name, data_values in data.items():
        encoded = list(map(encoders[data_name], data_values))
        vectors.append(encoded)
    formatted = []
    for vector_raw in list(zip(*vectors)):
        vector = []
        for element in vector_raw:
            for e in element:
                vector.append(e)
        formatted.append(vector)
    return formatted


supervised = make_supervised(data_frame)
encoded_inputs = np.array(encode(supervised["inputs"]))
encoded_outputs = np.array(encode(supervised["outputs"]))

train_x = encoded_inputs[:25]
train_y = encoded_outputs[:25]

test_x = encoded_inputs[25:]
test_y = encoded_outputs[25:]

model = k.Sequential()
model.add(k.layers.Dense(units=16, activation="relu"))
model.add(k.layers.Dense(units=1, activation="sigmoid"))
model.compile(loss="mse", optimizer="sgd", metrics=["accuracy"])
fit_results = model.fit(x=train_x, y=train_y, epochs=1000, validation_split=0.2)

plt.title("Losses train/validation")
plt.plot(fit_results.history["loss"], label="Train")
plt.plot(fit_results.history["val_loss"], label="Validation")
plt.legend()
plt.show()

plt.title("Accuracies train/validation")
plt.plot(fit_results.history["accuracy"], label="Train")
plt.plot(fit_results.history["val_accuracy"], label="Validation")
plt.legend()
plt.show()

predicted_test = model.predict(test_x)
real_data = data_frame.iloc[25:][input_names+output_names]
real_data["PRes"] = predicted_test
print(real_data)
pred = model.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
print(pred)
