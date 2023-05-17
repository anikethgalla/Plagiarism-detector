import difflib

# Function to check plagiarism
def check_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Calculate the similarity ratio
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

    return similarity_ratio

# Example usage
file1 = 'fish.txt'
file2 = 'guns.txt'
similarity = check_plagiarism(file1, file2)
print(f"Similarity ratio: {similarity}")

threshold = 0.00000001  # Adjust the threshold as per your requirements

if similarity >= threshold:
    print("The text is potentially plagiarized.")
