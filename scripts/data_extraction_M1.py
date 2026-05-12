import os
import re

def extract_answers_sequence(file_path: str) -> list[int]:
    """
    Parses a respondent's answer file and extracts their answers into a structured sequence
    of integers.

    Parameters
    ----------
    file_path : str 
        The path to the quiz answers text file.

    Returns
    -------
    list[int] 
        A list of 100 integers representing the respondent's answers. Each integer is 
        1, 2, 3, or 4 corresponding to the selected option, or 0 if the question was 
        not answered.

    Raises
    ------
    FileNotFoundError
        If the provided file_path does not exist.

    ValueError
        If an incomplete question block is found, multiple answers are selected 
        for a single question, or if the file does not contain exactly 100 answers.
    """

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
                raise ValueError(
                    "Incomplete question block detected: each question must be followed by four answer lines."
                )

            option_lines = lines[i+1 : i+5]
            selected_options = []

            # Check each of the 4 lines for an [x] or [X] indicating a selected answer
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


def write_answers_sequence(answers: list[int], n: int, destination_path: str) -> None:
    """
    Saves the extracted sequence for respondent n to a text file in the 'output' folder.

    Parameters
    ----------
    answers : list[int]
        A list of exactly 100 integers representing the answer sequence. Each value must be in {0, 1, 2, 3, 4}.
        
    n : int
        The positive integer identifier for the respondent.

    destination_path : str
        Folder where the output file will be saved. The file will be named "answers_list_respondent_n.txt" 
        where n is the respondent number.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If 'answers' is not a valid list of 100 integers, or if 'n' is not a positive integer.
    """
    
     # Defensive programming: validate the inputs
    if not isinstance(answers, list):
        raise ValueError("answers must be provided as a list.")

    # Ensure exactly 100 answers are present
    if len(answers) != 100:
        raise ValueError(f"answers must contain exactly 100 values, but received {len(answers)}.")
    
    # Ensure every answer is an integer between 0 and 4 
    if not all(isinstance(val, int) and val in {0, 1, 2, 3, 4} for val in answers):
        raise ValueError("Each answer must be an integer in {0, 1, 2, 3, 4}.")

    # Ensure respondent ID is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")


    # Create the destination directory if it does not exist
    os.makedirs(destination_path, exist_ok=True)

    # Generate output filename and path
    output_filename = f"answers_list_respondent_{n}.txt"
    output_path = os.path.join(destination_path, output_filename)

    # Write cleaned answers into the file seperated by spaces
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(" ".join(str(val) for val in answers) + "\n")

# Simple test blocks so group members can verify the module works
if __name__ == "__main__":
    test_file = "data/answers_respondent_1.txt"
    test_output_folder = "output"

    extracted_answers = extract_answers_sequence(test_file)

    print("First 10 extracted answers:=", extracted_answers[:10])
    print("Number of answers extracted:", len(extracted_answers))

    write_answers_sequence(extracted_answers, 1, test_output_folder)

    print("Test output saved successfully")