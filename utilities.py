import pandas as pd
import numpy as np
import config
import pickle

with open(config.model_file_path,"rb") as file:
    model=pickle.load(file)

def predict_admission(data):
    GRE_Score=float(data['GRE_Score'])
    TOEFL_Score=float(data['TOEFL_Score'])
    University_Rating=float(data['University_Rating'])
    SOP=float(data['SOP'])
    LOR=float(data['LOR'])
    CGPA=float(data['CGPA'])
    Research=float(data['Research'])

    pred_input=np.array([GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research])
    pred_output=model.predict([pred_input])[0]

    if pred_output==1:
        pred_output="Congratulations!  You will get Admission"
    elif pred_output==0:
       pred_output="No Chance of Admission"

    return pred_output


# GRE_Score=337
# TOEFL_Score=118
# University_Rating=4
# SOP=4.5
# LOR=4.5
# CGPA=9.65
# Research=1

