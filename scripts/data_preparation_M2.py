"""
M2 Data Preparation Module

This module is to download the raw respondent answer files from the cloud and save them to
the data folder using consistent naming conventions. 

These downloaded files are still raw text files contatining the full question blocks and
[x] answer selections. M1 will later parse each respondent file into a cleaned sequence
of integers.
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

if __name__ == "__main__":
    cloud_url = "https://raw.githubusercontent.com/fc-leeds/MATH1604_2025_2026_data/main"
    download_answer_files(cloud_url, "data", 64)