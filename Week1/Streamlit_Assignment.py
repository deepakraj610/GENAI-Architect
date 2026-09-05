import streamlit as st

# Set up the title of the web app
st.title("Student Grade System")

# Take the mark from the user through an input widget
# Setting value=None allows the field to start empty so we can handle empty input edge cases safely.
# Remove min_value and max_value so Python can catch the out-of-bounds numbers
mark = st.number_input(
    "Enter your mark (0-100):", 
    #value=85, 
    step=1
)


# Handle cases where the field is left empty or cleared
if mark is None:
    st.warning("Please enter a valid mark to see your grade.")

# Programmatic check for out-of-bounds inputs (in case boundaries are bypassed via manual typing)
elif mark < 0 or mark > 100:
    st.error("Invalid input! Please enter a mark strictly between 0 and 100.")

# Grading scale logic (Inclusive boundaries)
else:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    # Show a clear message displaying the entered mark and resulting grade
    st.success(f"Mark: {mark} -> Grade: {grade}")
