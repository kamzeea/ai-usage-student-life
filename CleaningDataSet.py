import pandas as pd
data_set = pd.read_csv('ai_assistant_usage_student_life.csv')
#examining the data
data_set.info() #gets number of columns, number of entries, etc.
description = data_set.describe() #gets numerical values such as mean and standard deviation for columns with numerical values
print(description)
#cleaning the data
null_sum = data_set.isnull().sum() #check for null values and records the total number
print(null_sum)
duplicates_sum = data_set.duplicated(subset = ['SessionID']).sum() #checks for duplicate values and records the total number
print(f'The number of duplicate sessions in this data set is {duplicates_sum}')
#subset parameter specifies that we want to check for duplicates in the SessionID only to make sure no session was recorded twice
data_set = data_set.drop_duplicates(subset = ['SessionID']) #removes any duplicate rows and outputs the cleaned data set
# Handle missing values
# Fill in missing values for SessionLengthMin with the average
average_session_length = data_set["SessionLengthMin"].mean()
data_set["SessionLengthMin"].fillna(average_session_length, inplace=True)
# Fill in missing values for SatisfactionRating with the middle value
middle_satisfaction = data_set["SatisfactionRating"].median()
data_set["SatisfactionRating"].fillna(middle_satisfaction, inplace=True)
# Fill in missing values for TotalPrompts with the average
average_prompts = data_set["TotalPrompts"].mean()
data_set["TotalPrompts"].fillna(average_prompts, inplace=True)
# Fill in missing values for AI_AssistanceLevel with the middle value
middle_assistance = data_set["AI_AssistanceLevel"].median()
data_set["AI_AssistanceLevel"].fillna(middle_assistance, inplace=True)
# Fill in missing values for TaskType with "Unknown"
data_set["TaskType"].fillna("Unknown", inplace=True)
# Fill in missing values for StudentLevel with "Unknown"
data_set["StudentLevel"].fillna("Unknown", inplace=True)
# Fill in missing values for Discipline with "Unknown"
data_set["Discipline"].fillna("Unknown", inplace=True)
# Fill in missing values for FinalOutcome with "Unknown"
data_set["FinalOutcome"].fillna("Unknown", inplace=True)
# Fill in missing values for UsedAgain with 1 (meaning "No")
data_set["UsedAgain"].fillna(1, inplace=True)
# Convert UsedAgain column to whole numbers (integers)
data_set["UsedAgain"] = data_set["UsedAgain"].astype(int)
# Encode categorical variables
data_set["StudentLevel"] = data_set["StudentLevel"].map({"High School": 1, "Undergraduate": 2, "Graduate": 3, "Unknown": 0})
data_set = pd.concat([data_set, pd.get_dummies(data_set["TaskType"], prefix="TaskType")], axis=1)
data_set.drop("TaskType", axis=1, inplace=True)
# Validate cleaning
print("\nNull Values After Cleaning:")
print(data_set.isnull().sum())
duplicates_sum_after = data_set.duplicated(subset=['SessionID']).sum()
print(f'The number of duplicate sessions after cleaning is {duplicates_sum_after}')
# Save cleaned dataset
data_set.to_csv("cleaned_dataset.csv", index=False)
print("\nPreprocessing complete. Saved to cleaned_dataset.csv")
