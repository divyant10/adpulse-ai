import google.generativeai as genai

genai.configure(api_key="AIzaSyDvdb4k1pYDFfUGYRut0o5n81quE_vAcAw")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)