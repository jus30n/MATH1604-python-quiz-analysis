"""
M4 Full Pipeline Script

Runs the full workflow:
1. Download / prepare data
2. Extract sequences 
3. Collate files
4. Analyse data
5. Visualise results
"""

# TODO: import M1, M2, and M3 functions
# from scripts.data_extraction_M1 import ... 
# from scripts.data_preparation_M2 import ...
# from scripts.data_analysis_M3 import ...

def main():
  # Step 1: define cloud URL, data folder, and output paths
  cloud_url = "to_be_filled"
  data_folder = "data"
  output_file = "output/collated_answers.txt"

  # Step 2: run download/preparation setup (M2)
  # TODO: call M2 function here
  
  # Step 3: extract answer sequences (M1)
  # TODO: call M1 function here
  
  # Step 4: collate answer files
  # TODO: combine outputs
  
  # Step 5: generate summary statistics (M3)
  # TODO: call M3 function here
  
  # Step 6: visualise possible patterns
  # TODO: generate plots


if __name__ == "__main__":
  main()
