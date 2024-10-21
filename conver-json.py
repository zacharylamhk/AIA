import json
from io import StringIO
import csv

# Function to parse raw text and convert it into JSON format with options

file_path = 'combined_sheets3.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
# Initialize variables
myDict={}
number=0
question=None
A=None
B=None
C=None
D=None
i=None
ii=None
iii=None
iv=None
ref=None

answer = None

for line in lines:
    # Check for question (lines starting with 'Q')
    f = StringIO(line)
    reader = csv.reader(f)
    
    
    if line[0].isdigit():
        parts = line.split(',')
        question = parts[1]
        ref=parts[0]
        number+=1
    elif line.startswith((",i,")):
        parts = line.split(',')
        i=parts[2]
    elif line.startswith((",ii,")):
        parts = line.split(',')
        ii=parts[2]
    elif line.startswith((",iii,")):
        parts = line.split(',')
        iii=parts[2]
    elif line.startswith((",iv,")):
        parts = line.split(',')
        iv=parts[2]        
    elif line.startswith((",A")):
        for row in reader:
            A = (row[2])
        if row[3].find('✓')>-1:
            answer='A'
        '''
        parts = line.split(',')
        A=parts[2]
        if parts[3].find('✓')>-1:
            answer='A'
        '''
    elif line.startswith((",B")):
        for row in reader:
            B = (row[2])
        if row[3].find('✓')>-1:
            answer='B'
            
    elif line.startswith((",C")):
        for row in reader:
            C = (row[2])
        if row[3].find('✓')>-1:
            answer='C'
            
    elif line.startswith((",D")):
        for row in reader:
            D = (row[2])
        if row[3].find('✓')>-1:
            answer='D'
        myDict[int(number)]={'QUESTION':question,'i':i,'ii':ii,'iii':iii,'iv':iv,'A':A,'B':B,'C':C,'D':D,'ANSWER':answer,'REF':ref}
        A=None
        B=None
        C=None
        D=None
        i=None
        ii=None
        iii=None
        iv=None
        ref=None
with open('insurance_exam.json', 'w', encoding='utf-8') as file2:
     file2.write(json.dumps(myDict,indent=3, ensure_ascii=False)) # use `json.loads` to do the reverse
     
     
        
                  
            
            
            
            
            
            
            
            
            
            
            
            
            
'''            
            if question:  # If we already have a question, store it first
                result.append({
                    "question": question,
                    "options": options,
                    "answer": answer
                })
            question = line.strip()  # Extract question
            options = []  # Reset options for the new question
            answer = None  # Reset answer for the new question
        # Check for options (lines starting with 'A', 'B', 'C', etc.)
        elif line[0] in "ABCD":
            option_text = line.strip()
            if option_text.endswith("Y"):  # If this option is the correct answer
                answer = option_text[:-2].strip()  # Store the correct answer without 'Y'
                option_text = option_text[:-2].strip()  # Remove 'Y' from the option text
            options.append(option_text)  # Add the option to the list
        # If it's just an additional line (for example, for the explanation after question text), ignore it

    # Add the last question and answer to the result
    if question:
        result.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    # Convert to JSON
    return json.dumps(result, ensure_ascii=False, indent=4)

# File path to the raw data
file_path = 'raw_q.txt'

# Convert raw data to JSON and print the result
json_data = convert_to_json_with_options(file_path)
print(json_data)

# You can also save it to a file
with open('converted_data_with_options.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
'''