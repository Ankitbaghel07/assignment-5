# Dictionary of Student Marks
a=input(" Enter a student name: ").lower()
student ={"ankit":80,"pranjal":90}
try:
    print(f"{a} marks is:{student[a]}")
except KeyError:
    print("student name not found.")

    

