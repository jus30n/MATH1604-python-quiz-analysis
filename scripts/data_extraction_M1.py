import os
import re

def extract_answers_sequence(file_path: str) -> list[int]:
   
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read the file and strip newline characters from the right
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]

    answers = []
    # Pattern to match the start of a question block (e.g., "Question 1.")
    question_pattern = re.compile(r"^\s*Question\s+\d+\.")
    i = 0

    while i < len(lines):
        line = lines[i]
        
        # When a question header is found, check the next 4 lines for options
        if question_pattern.match(line):
            if i + 4 >= len(lines):
                raise ValueError("Incomplete question block detected: each question must be followed by four answer lines.")

            option_lines = lines[i+1 : i+5]
            selected_options = []

            # Check each of the 4 lines for an [x] or [X]
            for option_number, option_line in enumerate(option_lines, start=1):
                stripped = option_line.strip()
                if stripped.startswith("[x]") or stripped.startswith("[X]"):
                    selected_options.append(option_number)

            # Ensure a respondent didn't select multiple answers for one question
            if len(selected_options) > 1:
                raise ValueError(f"More than one selected answer found for question {len(answers) + 1}.")

            # Append the selected option (1-4), or 0 if unanswered
            if len(selected_options) == 1:
                answers.append(selected_options[0])
            else:
                answers.append(0)

            # Skip ahead past the current question and its 4 options
            i += 5
        else:
            i += 1

    # Validate that exactly 100 answers were extracted
    if len(answers) != 100:
        raise ValueError(f"Expected 100 answers, but extracted {len(answers)}")

    return answers


def write_answers_sequence(answers: list[int], n: int) -> None:
    """
    Saves the extracted sequence for respondent n to a text file in the 'output' folder.

    Parameters:
        answers (list[int]): A list of exactly 100 integers representing the answers.
        n (int): The positive integer identifier for the respondent.

    Returns:
        None

    Raises:
        ValueError: If 'answers' is not a list, contains invalid values, or if 'n' is not positive.
    """
    # Defensive programming: validate the inputs
    if not isinstance(answers, list):
        raise ValueError("answers must be provided as a list.")

    if not all(isinstance(val, int) and val in {0, 1, 2, 3, 4} for val in answers):
        raise ValueError("Each answer must be an integer in {0, 1, 2, 3, 4}.")

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    # Hardcode the output directory to match project architecture slides
    output_dir = "output"
    
    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the output filename
    output_filename = f"answers_list_respondent_{n}.txt"
    output_path = os.path.join(output_dir, output_filename)

    # Write the list of integers to the text file separated by spaces
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(" ".join(str(val) for val in answers) + "\n")





file_path = "/Users/abdulazizalsulami/Downloads/data/a1.txt" 


answers = extract_answers_sequence(file_path)


print("Here is the extracted list:")
print(answers)

# 4. Save the results (Notice we only pass TWO parameters now!)
write_answers_sequence(answers, 1)
print("File successfully saved to the 'output' folder!")

import os
print("The file was actually saved right here:")
print(os.path.abspath("output"))
