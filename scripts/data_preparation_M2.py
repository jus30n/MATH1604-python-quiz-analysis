"""
M2 Data Preparation Module

This module is to download the raw respondent answer files from the cloud and save them to
the data folder using consistent naming conventions. 

It also collates the downloaded raw respondent files into one combined file called
collated_answers.txt in the output/ folder.

These downloaded and collated files are still raw text files contatining the full question 
blocks and [x] answer selections. M3 will later use M1's extraction function to parse the
answer selections into integer sequences for analysis.
"""

import os
import urllib.request
import urllib.error

def download_answer_files(cloud_url: str, path_to_data_folder: str, total_respondents: int) -> None:
    """
    Download raw respondent answer files from the cloud repository.
    
    This function downloads files named a1.txt, a2.txt, ..., aN.txt from the given cloud
    URL and saves them locally in the data folder as answers_respondent_1.txt, 
    answers_respondent_2.txt, ..., answers_respondent_N.txt.
    
    Parameters
    ----------
    cloud_url : str
        The base URL where the raw answer files are stored.
        For this project, the files are named a1.txt, a2.txt, etc.
        
    path_to_data_folder : str
        The local folder where the downloaded respondent files should be saved.
        In this project, we will save them in the "data" folder.
        
    total_respondents : int
        The total number of respondent files to attempt to download.
        
    Returns
    -------
    None
        This function does not return a value. It saves downloaded files into the
        specified data folder.
        
    Raises
    ------
    ValueError
        If total_respondents is not a positive integer.

    Notes
    -----
    If a file does not exist in the cloud location, the function prints a warning and 
    continues instead of stopping the whole download process. This is useful for 
    testing with more files than currently exist in the cloud repository.
    """

    if not isinstance(total_respondents, int) or total_respondents <= 0:
        raise ValueError("total_respondents must be a positive integer.")
    
    # Create the data folder if it does not already exist.
    os.makedirs(path_to_data_folder, exist_ok=True)
    
    # Remove a trailing slash from the URL if there is one.
    cloud_url = cloud_url.rstrip('/')

    for n in range(1, total_respondents +1):
        source_url = f"{cloud_url}/a{n}.txt"
        output_filename = f"answers_respondent_{n}.txt"
        output_path = os.path.join(path_to_data_folder, output_filename)

        try:
            urllib.request.urlretrieve(source_url, output_path)
            print(f"Downloaded {source_url} -> {output_path}")

        except urllib.error.HTTPError as error:
            print(f"Warning: a{n}.txt could not be downloaded. HTTP error: {error.code}")

        except urllib.error.URLError as error:
            print(f"Warning: Could not connect to download a{n}.txt. Reason: {error.reason}")


def collate_answer_files(data_folder_path: str) -> None:
    """
    Collate all respondent answer files into one combined output file.
    
    This function reads respondent files from the data folder using the naming format
    answers_respondent_1.txt, answers_respondent_2.txt, etc. It combines them into one file
    named collated_answers.txt inside the output/ folder.
    
    Each respondent section is separated by a line containing one asterisk (*).
    
    Parameters
    ----------
    data_folder_path : str
        Path to the folder containing the raw respondent answer files.
        
    Returns
    -------
    None
        This function does not return a value. It saves the collated file into the 
        output folder.
        
    Raises
    ------
    FileNotFoundError
        If the provided data folder does not exist.
        
    ValueError
        If no respondent answer files are found in the data folder."""

    if not os.path.exists(data_folder_path):
        raise FileNotFoundError(f"Data folder not found: {data_folder_path}")
    
    # Find files that match the expected respondent filename format
    respondent_files = []

    for filename in os.listdir(data_folder_path):
        if (
            filename.startswith("answers_respondent_") 
            and filename.endswith(".txt")
        ):
            respondent_files.append(filename)

    if len(respondent_files) == 0:
        raise ValueError(f"No respondent answer files found in the data folder.")
    
    # Sort files by respondent number, not alphabetically
    # This ensures respondent_2 comes before respondent_10, etc.
    respondent_files.sort(
        key=lambda filename: int(
            filename.replace("answers_respondent_", "").replace(".txt", "")
        )
    )

    # Create output folder if it does not already exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    collated_path = os.path.join(output_folder, "collated_answers.txt")

    with open(collated_path, "w", encoding="utf-8") as output_file:

        for filename in respondent_files:
            file_path = os.path.join(data_folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as respondent_file:
                content = respondent_file.read().strip()

            # Write the respondent's raw answer file content
            output_file.write(content)
            output_file.write("\n")

            # Separate respondent sections with one asterisk
            output_file.write("*\n") 
            
    print(f"Collated {len(respondent_files)} respondent files into {collated_path}")

if __name__ == "__main__":
    cloud_url = "https://raw.githubusercontent.com/fc-leeds/MATH1604_2025_2026_data/main"

    data_folder = "data"

    download_answer_files(cloud_url, data_folder, 64)

    collate_answer_files(data_folder)