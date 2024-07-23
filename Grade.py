class Grade:
    @staticmethod
    def grader(marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid Range: Please Enter marks in the range of 1-100.")
        
        if marks < 60:
            grade = 'F'
        elif 60 <= marks < 70:
            grade = 'D'    
        elif 70 <= marks < 80:
            grade = 'C'
        elif 80 <= marks < 90:
            grade = 'B'
        else:
            grade = 'A'

        return grade


print(Grade.grader(75))
print(Grade.grader(100))
print(Grade.grader(60)) 

#Grades should spell out CAD