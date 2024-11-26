dict1= {1:'ford',2:'toyota',3:'suzuki'}
a=list(dict1.keys())
b=list(dict1.values())

new_dict =dict(zip(b,a))
print(new_dict)