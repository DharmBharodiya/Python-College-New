dict1={'Dev':{'sem':3,'age':20,'Cpi':9.1},'Dharm':{'sem':3,'age':20,'Cpi':9.4},'Dhruvan':{'sem':4,'age':20,'Cpi':9.68}}
student_name=list(dict1.keys())
print(student_name)
high_cpi = 0
for i,j in dict1.items():
    if j['Cpi']>high_cpi:
        high_cpi = j['Cpi']
        top_student = i
        
print("Highest CPI",high_cpi)
print("Student:",top_student)