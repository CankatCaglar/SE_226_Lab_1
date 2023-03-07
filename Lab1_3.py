
name = input("Enter the name of the student: ")

# Get the exam grades
labGrade = float(input("Enter the lab grade (%25): "))
midtermGrade = float(input("Enter the midterm grade (%35): "))
finalGrade = float(input("Enter the final grade (%40): "))

lastScore = labGrade * 0.25 + midtermGrade * 0.35 + finalGrade * 0.4

print("Name:", name)
print("Lab:", labGrade)
print("Midterm:", midtermGrade)
print("Final:", finalGrade)
print("Last Score:", lastScore)