# sample2.py
import json
import difflib
import os

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load disease data from the data.json file
with open(os.path.join(script_dir, 'data.json'), 'r') as data_file:
    disease_data = json.load(data_file)

# Define symptom weights (customize as needed)
weights = {
    "fever": 1.5,
    "diarrhea": 1.2,
    "vomiting": 1.2,
    "fatigue": 1.0,
    "chills": 1.0,
    # Add more symptoms and their weights as needed
}

# Update the weights based on the symptoms in the JSON file
for disease_info in disease_data.values():
    disease_symptoms = disease_info.get("symptoms", [])
    for symptom in disease_symptoms:
        if symptom not in weights:
            weights[symptom] = 1.0  # You can customize the weight as needed

# List of common stop words to filter out from user input
stop_words = ["i", "have", "and", "the", "for", "with", "a", "an"]

# Function to predict the disease based on user input
def predict_disease(symptoms, weights):
    best_matches = []
    best_similarities = []
    
    for disease, disease_info in disease_data.items():
        disease_symptoms = disease_info.get("symptoms", [])
        similarity = weighted_similarity(symptoms, disease_symptoms, weights)
        
        if similarity > 0.0:
            best_matches.append(disease)
            best_similarities.append(similarity)
    
    if best_matches:
        sorted_matches = [x for _, x in sorted(zip(best_similarities, best_matches), reverse=True)]
        return sorted_matches[0]
    
    return None

# Function to correct misspelled symptoms
def correct_spelling(input_symptoms, valid_symptoms):
    corrected_symptoms = []
    for symptom in input_symptoms:
        closest_match = difflib.get_close_matches(symptom, valid_symptoms, n=1, cutoff=0.4)  # Adjust the cutoff here
        if closest_match:
            corrected_symptoms.append(closest_match[0])
        else:
            corrected_symptoms.append(symptom)
    return corrected_symptoms

# Function to remove stop words from user input
def remove_stop_words(user_input, stop_words):
    words = user_input.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

# Function to calculate the weighted similarity between symptoms
def weighted_similarity(user_symptoms, disease_symptoms, weights):
    similarity = 0.0
    for symptom in user_symptoms:
        if symptom in weights:
            similarity += weights[symptom] * (symptom in disease_symptoms)
    return similarity
