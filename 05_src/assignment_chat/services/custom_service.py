def create_study_design(topic: str) -> str:
    """
    A simple function-calling style service that creates a basic study design.
    """
    return f"""
Here is a simple research study design for your topic: {topic}

Research Question:
What factors are associated with {topic} in the target population?

Suggested Study Design:
A cross-sectional study would be a good starting point.

Population:
Adults or patients relevant to the topic.

Data to Collect:
- Age
- Sex
- Socioeconomic status
- Main exposure variables
- Main outcome variable
- Relevant clinical or public health factors

Analysis Plan:
- Descriptive statistics
- Chi-square test for categorical variables
- T-test or ANOVA for continuous variables
- Logistic regression if the outcome is binary

Expected Output:
This study can identify important associations and help guide future research or intervention planning.
"""