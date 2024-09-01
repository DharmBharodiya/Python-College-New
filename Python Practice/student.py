students = {
    "Dharm":{"semester":5,"age":18,"cpi":9.65},
    "Elon":{"semester":4,"age":19,"cpi":9.10},
    "Steve":{"semester":6,"age":23,"cpi":8.76}
}

highest_cpi = 0 #the lowest possible value of the CPI
highest_cpi_student = None #initially

for name, info in students.items(): #name -> keys of students, info -> values of students
    if  info["cpi"] > highest_cpi:
        highest_cpi = info["cpi"]
        highest_cpi_student = name


print(highest_cpi_student, " got the highest CPI of: ", highest_cpi)
