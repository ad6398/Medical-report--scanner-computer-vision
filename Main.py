# this program uses pytesseract and open cv for ocr, either use this or provide ocr text as input to variable name text in line 16
import pytesseract as pt
import re
import cv2
import json

filename = "report2.jpg"
img = cv2.imread(filename)

# Declmairs: result of this code is totally dependent on capabilities of ocr of image file, better ocr better is result


text = pt.image_to_string(img, lang="eng")





defined_dict = {'Hospital Name': ['Hospital Name', 'Hospital_Name',
                                'hospital name'],
              'Hospital Address': ['Address', 'city', 'Hospital Address'],
              'Patient Name': ['Name', 'Patient_Name', 'Patient Name', 'patient name'],
              'Address': ['Patient Address', 'Address', 'Add'],
              'Age': ['Age', 'age'],
              'Sex': ['Sex', 'sex', 'gender', 'Gender', 'M/F', 'Male/Feamal'],
              'Doctor Name': ['Doctor Name', 'doctor name', 'doctor', 'treating doctor',
                              'Consultants', 'CONSULTANT', 'Consultant Name', 'Dr.', 'ref', 'ref by', 'reffered by'],
              'Date': ['Dated', 'Date', 'DOC', 'DOD', 'DOA'],
              'Diagnosis': ['Diagnosis', 'Final Diagnosis', 'Principal/Secondary Diagnosis'],
              'Treatment Given': ['Treatment Given', 'On Examination', 'Examination'],
              'Summary': ['Summary', 'Past Treatment Given'],
              'MR Number': ['MR No', 'MR Number', 'MRNO '],
              'Blood Urea': ['Blood Urea', 'Urea in Blood'],
              'Serum Creatinine': ['serum creatinine', 'creatinine serum'],
              'Urine Sugar': ['urine sugar', 'sugar (urine)'],
              'Bile Pigment': ['bile pigment', 'pigment(bile)'],

              }

result_dict = defined_dict
result_dict = result_dict.fromkeys(result_dict, '')
for key in defined_dict.keys():  
    for similar_keys in defined_dict[key]:  
        q = 0
        para = [similar_keys.lower()+r":(.*) ",similar_keys.lower()+r" : (.*) ",similar_keys.lower()
        +r": (.*)",similar_keys.lower()+r": (.*)",
             similar_keys.lower()+r"( *)\n(.*)", similar_keys.lower()+r" (.*)",
             similar_keys.lower()+r"\n\n(.*)", similar_keys.lower()+r": (.*)" ]  #tring to find string matches and its reponses this just written on basis of observing possibilities of ocr
        for target in para:
            
            match = re.search(target, text.lower())
            if match:
                result = match.group(1)
                q = 1
                result_dict[key] = result
                break
            else:
                result = ""
        if q == 1:
            break


#result_dict will be stored as output.json

with open('output.json', 'w') as fp:
    json.dump(result_dict, fp)
