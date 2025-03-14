from text_to_speech.exception import CustomException
import os, sys
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from text_to_speech.components.get_accent import get_accent_message, get_accent_tld
from text_to_speech.components.textTospeech import TTSapplication

app=Flask(__name__)
CORS(app)

import requests
response = requests.get("https://translate.google.com")
print(response.status_code)


@app.route("/",methods=['GET'])
@cross_origin()
def home():
    try:
        accent_list=get_accent_message()
        return render_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise CustomException(e,sys) from e
    
@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()

def predict():
    try:
        if request.method=='POST':
            data=request.json['data']
            accent_input=request.json['accent']
            accent=get_accent_tld(accent_input)
            
            result=TTSapplication().textTospeech(data, accent)
            return {"data": result.decode('utf-8')}
        
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__=='__main__':
    app.run(port=8000,debug=True)
    

