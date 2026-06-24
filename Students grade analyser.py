import numpy as np



# Rows:Students
#Colums represent the subs
student_grades= np.random.randint(40,101,(50,5))
subjects=["Maths","English","CS","Chemistry","Physics"]
print("-----------Student Grade Analysis-----------")
result={}

for place,subject in enumerate(subjects):
    data=student_grades[:,place]


    grades={"A": np.sum(data>=80),
            "B": np.sum((data>=70)&(data<=79)),
            "C": np.sum((data>=60)&(data<=69)),
            "D": np.sum((data>=50)&(data<=59)),
            "F": np.sum(data<=50)}
    result[subject]=grades

for subject,grades in result.items():
    print("\n",subject)
    for grade, marks in grades.items():
        print(f"{grade}:{marks}")

print()
print("----------Average----------")

average = np.mean(student_grades,axis=0)
for sub,av in enumerate(average):
    print(f"{subjects[sub]}:{av}")

print()
print("-----Highest per subject------")

highest=np.max(student_grades,axis=0)
for m,high in enumerate(highest):
    print(f"{subjects[m]}:{high}")

print()
print("--------Lowest per subject--------")

lowest=np.min(student_grades,axis=0)
for l,low in enumerate(lowest):
    print(f"{subjects[l]}:{low}")

print()
print("----------Hardest Subject----------")
subject_average=np.mean(student_grades,axis=0)
hardest=np.argmin(subject_average)
print(f"The hardest Subject is:{subjects[hardest]}")

print()
print("----------Easiest Subject----------")
eaisest=np.argmax(subject_average)
print(f"The eaisest subject is :{subjects[eaisest]}")

print()
print("---------Grade concistancy---------")
std = np.std(student_grades, axis=0)
for v,s in enumerate(std):
    print(f"{subjects[v]}:{s}")

print()
print("----------Top 5 Students----------")

student_avrg=np.mean(student_grades,axis=1)
top5_students=np.argsort(student_avrg)[-5:]

for rev in reversed(top5_students):
    print()
    print(f"Student:{rev}    Average:{student_avrg[rev]:.2f}")
    print("------------")
    for j,s in enumerate(subjects):
        print(f"{s}:{student_grades[rev][j]}")

print()
print("-------Bottom 5 Students-------")
bottom5_students=np.argsort(student_avrg)[:5]
for i in bottom5_students:
    print()
    print(f"Students:{i}        Average:{student_avrg[i]}")
    print("------------")
    for a,k in enumerate(subjects):
        print(f"{k}:{student_grades[i][a]}")

print()
print("---------Best Student---------")
best=np.argmax(student_avrg)
print(f"The best Student is:Student {best}")

print()
print("---------Worst Student---------")
worst=np.argmin(student_avrg)
print(f"The worst student is: Student {worst}")


print("------------------------------")