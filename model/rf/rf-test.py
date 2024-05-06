from joblib import load

# Load the model from the file
loaded_model = load('rf-classifier.joblib')
vectorizer = load("rf-vec.joblib")

# Now you can use the loaded_model to make predictions
# For example, to predict the class of a new repository
new_repository_text = "Classes and Metriсs (CaM): a dataset of Java classes from public open-source GitHub repositories"
new_repository_text_transformed = vectorizer.transform([new_repository_text])
prediction = loaded_model.predict(new_repository_text_transformed)

print(f"The predicted class for the new repository is: {prediction[0]}")
