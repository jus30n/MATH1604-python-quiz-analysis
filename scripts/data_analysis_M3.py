import os
import tempfile
import matplotlib.pyplot as plt
from data_extraction_M1 import extract_answers_sequence

def _get_all_sequences(collated_answers_path: str) -> list[list[int]]:
    """
    Helper function to parse the collated file using M1's extraction logic.
    Splits the collated file by the '*' separator, writes each block to a 
    temporary file, and runs M1's extract_answers_sequence on it.
    """
    if not os.path.exists(collated_answers_path):
        raise FileNotFoundError(f"Collated file not found: {collated_answers_path}")

    with open(collated_answers_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    
    blocks = [block.strip() for block in content.split('*') if block.strip()]
    
    all_answers = []
    
  
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_path = temp_file.name
        
    try:
        for block in blocks:
           
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(block)
            
           
            answers = extract_answers_sequence(temp_path)
            all_answers.append(answers)
    finally:
        
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    return all_answers

def generate_means_sequence(collated_answers_path: str) -> list[float]:
    """
    Computes the mean answer value for each of the 100 questions across all respondents.
    
    Parameters:
        collated_answers_path (str): The path to the collated answers text file.

    Returns:
        list[float]: A list of 100 floats representing the mean value for each question.
                     Unanswered questions (coded as 0) are excluded from the mean calculation.
    """
    all_answers = _get_all_sequences(collated_answers_path)
    
    if not all_answers:
        return []

    means = []
    
   
    for q_idx in range(100):
       
        valid_answers = [respondent[q_idx] for respondent in all_answers if respondent[q_idx] != 0]
        
        if valid_answers:
            question_mean = sum(valid_answers) / len(valid_answers)
            means.append(float(question_mean))
        else:
           
            means.append(0.0)
            
    return means

def visualize_data(collated_answers_path: str, n: int) -> None:
    """
    Generates visualisations to detect patterns in the quiz responses.

    Parameters:
        collated_answers_path (str): The path to the collated answers text file.
        n (int): 1 to display a scatter plot of the means sequence.
                 2 to display a line plot of all individual answer files.

    Returns:
        None
    """
    if n == 1:
       
        means = generate_means_sequence(collated_answers_path)
        
        plt.figure(figsize=(12, 6))
        plt.scatter(range(1, 101), means, color='blue', alpha=0.7)
        plt.title("Mean Answer Value per Question (Excluding Unanswered)")
        plt.xlabel("Question Number (1-100)")
        plt.ylabel("Mean Answer Value")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()
        
    elif n == 2:
      
        all_answers = _get_all_sequences(collated_answers_path)
        
        plt.figure(figsize=(14, 7))
        for answers in all_answers:
           
            plt.plot(range(1, 101), answers, alpha=0.15, color='purple')
            
        plt.title("Individual Answer Sequences for All Respondents")
        plt.xlabel("Question Number (1-100)")
        plt.ylabel("Selected Answer (0-4)")
        plt.yticks([0, 1, 2, 3, 4])
        plt.grid(True, linestyle='--', alpha=0.4)
        plt.show()
        
    else:
       
        print("Error: Parameter 'n' must be either 1 or 2.")