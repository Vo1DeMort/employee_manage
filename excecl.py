import pandas as pd

# Employee data
employee_data = {
    'ID': [1, 2],
    'Name': ['John Doe', 'Jane Smith'],
    'DOB': ['1985-06-15', '1990-09-22'],
    'Gender': ['Male', 'Female'],
    'Email': ['john.doe@example.com', 'jane.smith@example.com'],
    'State': ['CA', 'TX'],
    'Address': ['123 Elm Street', '456 Oak Avenue'],
    'Skills': ['Python, Django', 'JavaScript, React']
}

# Education data
education_data = {
    'Employee Name': ['John Doe', 'John Doe', 'Jane Smith', 'Jane Smith'],
    'Education Type': ['Bachelor\'s', 'Master\'s', 'Bachelor\'s', 'Master\'s'],
    'Description': ['B.Sc. in Computer Science', 'M.Sc. in Data Science', 'B.A. in Computer Science', 'M.A. in Software Engineering'],
    'Graduation Year': [2007, 2009, 2012, 2014]
}

# Create dataframes
df_employees = pd.DataFrame(employee_data)
df_educations = pd.DataFrame(education_data)

# Save to Excel files
df_employees.to_excel('employees.xlsx', sheet_name='Employees', index=False)
df_educations.to_excel('educations.xlsx', sheet_name='Educations', index=False)

print("Files generated successfully: 'employees.xlsx' and 'educations.xlsx'")

