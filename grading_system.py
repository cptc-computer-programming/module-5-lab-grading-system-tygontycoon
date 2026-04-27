# grading_system.py
# Simple Grading System

#change
Late_penalty = 10
Extra_Credit_Bonus = 5
# ------------------------------------------------------------
# Step 1: Get starting information
# ------------------------------------------------------------

student_name = input("Student name: ")

score = int(input("Assignment score out of 100: "))
was_late = input("Was the assignment late? (yes/no): ") == "yes"
extra_credit_completed = input("Was extra credit completed? (yes/no): ") == "yes"

# use boolean variables to represent logic so that our decision structures are cleaner later

# These variables will be updated by your decision structures.
final_score = score
letter_grade = ""
is_passing = False
message = ""


# ------------------------------------------------------------
# Step 2: Apply late penalty
# ------------------------------------------------------------

# TODO 1:
# If the assignment was late:
# - subtract 10 from final_score
# - set message to "Late penalty applied."
if was_late: 
    final_score = final_score
    message = "late penalty applied"



# ------------------------------------------------------------
# Step 3: Apply extra credit
# ------------------------------------------------------------

# TODO 2:
# If extra credit was completed:
# - add 5 to final_score
# - set message to "Extra credit applied."
if extra_credit_completed:
    final_score = final_score + Extra_Credit_Bonus
    message = "extra credit applied"



# ------------------------------------------------------------
# Step 4: Keep score within valid range
# ------------------------------------------------------------

# TODO 3:
# Use if / elif / else.
#
# If final_score is greater than 100:
# - set final_score to 100
#
# Else if final_score is less than 0:
# - set final_score to 0
#
# Else:
# - leave final_score unchanged

if final_score > 100:
    final_score = 100
elif final_score < 0:
    final_score = 0


# ------------------------------------------------------------
# Step 5: Decide letter grade
# ------------------------------------------------------------

# TODO 4:
# Use if / elif / else to set letter_grade.
#
# 90 or above: A
# 80 or above: B
# 70 or above: C
# 60 or above: D
# Below 60: F

if final_score > 90:
    letter_grade = "A"
elif final_score >= 80:
    letter_grade = "B"
elif final_score >= 70:
    letter_grade = "C"
elif final_score >= 60:
    letter_grade = "D" 
else:
    letter_grade = "F"

# ------------------------------------------------------------
# Step 6: Decide if the student is passing
# ------------------------------------------------------------

# TODO 5:
# If final_score is 60 or higher:
# - set is_passing to True
#
# Else:
# - set is_passing to False

is_passing = final_score >= 60



# ------------------------------------------------------------
# Step 7: Add a message using nested decisions
# ------------------------------------------------------------

# TODO 6:
# If the student is passing:
#     If the final score is 90 or higher:
#         set message to "Excellent work!"
#     Else:
#         set message to "Passing assignment."
#
# Else:
#     set message to "Not passing yet. Keep practicing."

if is_passing:
    if final_score >= 90:
        message = " excellent work!"
    else:
        message = "Passing assimgnment."
else: 
    message = "not passing yet. keep practicing."

# ------------------------------------------------------------
# Step 8: Challenge — combine conditions
# ------------------------------------------------------------

# TODO 7:
# Create a boolean variable called needs_review.
#
# needs_review should be True if:
# - the student is not passing
# OR
# - the assignment was late AND the final score is below 70
#
# Otherwise, needs_review should be False.
needs_review = (not is_passing) or (was_late and final_score < 70)



# ------------------------------------------------------------
# Step 9: Final output
# ------------------------------------------------------------

print()
print("--- Grade Report ---")
print("Student:", student_name)
print("Original score:", score)
print("Final score:", final_score)
print("Letter grade:", letter_grade)
print("Passing:", is_passing)
# print("Needs review:", needs_review)
print("Message:", message)