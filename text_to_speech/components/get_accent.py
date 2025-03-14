from text_to_speech.logger import logger
from text_to_speech.exception import CustomException

import os, sys


# maps country names with respective TLD's(top level domains)

def get_accent_tld(user_input):
    try:
        
        accent_input={
            'Australian': 'com.au',
            'South Africa': 'co.za',
            "British": 'co.uk',
            'Indian': 'co.in',
            'Canadian': 'ca',
            'Irish': 'ie',
            'Spanish': 'es'
        }
        tld=accent_input.get(user_input)  # based on user input getting mapped with respective maps (co.au, co.za)
         
        return tld
    except Exception as e:
        raise CustomException(e,sys)

    
def get_accent_message():
    try:
        accent=['Australian', 'South Africa', 'British', 'Indian', 'Canadian', 'Irish', 'Spanish']
        return accent
    
    except Exception as e:
        raise CustomException(e,sys)
    