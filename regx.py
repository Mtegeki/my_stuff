import re 
import spacy
import tensorflow as tf

text = "email yangu ni anordmtegeki23@gmail.com"
textb = "namba yangu ni 0757914834"
title = '''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)'''
pattern = "[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-zA-Z0-9]*"
#patternb = "\d{10}"
patternb = "namba[^\d]*(\d*)"
patternc = "Born(.*)"
patternd = "Citizenship(.*)"
email_finder = re.findall(patternb, textb)
#title_r = re.findall(patternc, title)
title_r = re.findall(patternd, title)
print(email_finder[0])
print(title_r[0].strip())