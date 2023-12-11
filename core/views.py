import json
from .forms import SymptomForm
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    statistics= models.CholeraDatabase.objects.all()
    context = {
        'statistics':statistics
    }

    return render(request, 'index.html', context)


def Bot(request):
    return render(request, 'bot2.html')


def Dio(request):
    return render(request, 'di.html')

# disease_detector/views.py
from django.shortcuts import render
from .forms import SymptomForm
import os
import json
import difflib

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
def predict_disease(symptoms, disease_data, weights):
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

# Helper function to retrieve information about a disease
def get_disease_info(disease_name):
    return disease_data.get(disease_name, {})

def disease_detection(request):
    form = SymptomForm()

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['symptoms']
            user_input = remove_stop_words(user_input, stop_words)
            symptoms = user_input.split(',')
            predicted_disease = predict_disease(symptoms, disease_data, weights)

            # Retrieve additional information about the predicted disease
            disease_info = get_disease_info(predicted_disease)

            return render(
                request,
                'disease_detector/result.html',
                {
                    'predicted_disease': predicted_disease,
                    'description': disease_info.get('description', ''),
                    'treatment_suggestions': disease_info.get('treatment', ''),
                }
            )

    return render(request, 'disease_detector/index1.html', {'form': form})



from django.shortcuts import render
from .models import District

def view_district(request, pk):
    
    district = models.CholeraDatabase.objects.get(pk=pk)
    context = {
        'district' : district,
        
        
    }
    return render(request, 'view.html', context)