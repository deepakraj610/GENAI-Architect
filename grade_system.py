def determine_grade(mark):
    """Returns the letter grade for a given mark based on the grading scale."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

def main():
    print("--- Student Grading System ---")
    
    # Prompt the user for input
    user_input = input("Enter a mark (0 - 100): ")
    
    # Handle edge cases and invalid inputs
    try:
        # Convert input to a float to accommodate decimal marks (e.g., 85.5)
        mark = float(user_input)
        
        # Check if the mark is outside the valid 0-100 range
        if mark < 0 or mark > 100:
            print("Error: The mark must be between 0 and 100. Please try again.")
        else:
            # Calculate and display the valid grade
            grade = determine_grade(mark)
            # Format the output to drop the decimal if it's a whole number
            formatted_mark = int(mark) if mark.is_integer() else mark
            print(f"Result: A mark of {formatted_mark} corresponds to a grade of {grade}.")
            
    except ValueError:
        # Handle the case where the user types letters, symbols, or nothing at all
        print("Error: Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()