import pickle

with open(r"C:\Users\dzoum\OneDrive\Υπολογιστής\E-Commerce\Model_Prediction\model.pkl",'rb') as file:
    model = pickle.load(file)

input_data = input("Enter your data: ")
predictions = model.predict(input_data)
print("Predictions: ",predictions )
    