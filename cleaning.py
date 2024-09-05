import re
import os
import glob

# Function to remove consecutive duplicate sentences and ensure proper formatting
def remove_consecutive_duplicate_sentences(text):
    # Split the text into sentences using regular expressions
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Remove consecutive duplicate sentences
    unique_sentences = []
    previous_sentence = None
    
    for sentence in sentences:
        if sentence.strip() != previous_sentence:
            unique_sentences.append(sentence.strip())
            previous_sentence = sentence.strip()
    
    # Join the unique sentences back into a single text
    cleaned_text = ' '.join(unique_sentences)
    
    # Ensure there is exactly one space between words and remove any leading/trailing whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    # Add whitespace between punctuation and words if needed
    cleaned_text = re.sub(r'(\w)([^\w\s])', r'\1 \2', cleaned_text)  # Add space before punctuation
    cleaned_text = re.sub(r'([^\w\s])(\w)', r'\1 \2', cleaned_text)  # Add space after punctuation

    return cleaned_text

# Directory containing the files
directory = 'path_to_your_folder'

# Process each text file in the directory
for file_path in glob.glob(os.path.join(directory, '*.txt')):
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove consecutive duplicate sentences
    cleaned_text = remove_consecutive_duplicate_sentences(text)

    # Write the cleaned content to a new file
    cleaned_file_path = os.path.join(directory, 'cleaned_' + os.path.basename(file_path))
    with open(cleaned_file_path, 'w') as cleaned_file:
        cleaned_file.write(cleaned_text)

    print(f"Cleaned content saved to {cleaned_file_path}.")
