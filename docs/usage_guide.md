# Usage Guide

This guide provides detailed examples of how to use the Balochi NLP package for various text processing tasks.

## Basic Usage

### 1. Text Cleaning

```python
from balochi_nlp.preprocessing import BalochiTextCleaner

# Initialize the cleaner
cleaner = BalochiTextCleaner()

# Clean a simple text
text = "منی نام احمد اِنت۔ https://example.com user@email.com 123 ABC"
cleaned_text = cleaner.clean_text(text)
print(cleaned_text)  # Will remove URLs, emails, numbers, and non-Balochi text

# Clean with specific options
cleaned_with_numbers = cleaner.clean_text(text, remove_numbers=False)
cleaned_without_special = cleaner.clean_text(text, preserve_special_chars=False)
```

### 2. Tokenization

#### Word Tokenization
```python
from balochi_nlp.tokenizers import BalochiWordTokenizer

# Initialize the tokenizer
tokenizer = BalochiWordTokenizer()

# Basic tokenization
text = "منی نام احمد اِنت"
tokens = tokenizer.tokenize(text)
print(tokens)  # List of words

# Tokenization with affix analysis
tokens_with_affixes = tokenizer.tokenize_with_affixes(text)
for token_info in tokens_with_affixes:
    print(f"Word: {token_info['word']}")
    print(f"Prefix: {token_info.get('prefix', '')}")
    print(f"Suffix: {token_info.get('suffix', '')}")
```

#### Sentence Tokenization
```python
from balochi_nlp.tokenizers import BalochiSentenceTokenizer

# Initialize the tokenizer
sentence_tokenizer = BalochiSentenceTokenizer()

# Tokenize into sentences
text = """
منی نام احمد اِنت۔
من بلوچستان ءَ زندگ کنان۔
من روچ روچ کتابءَ وانان۔
"""
sentences = sentence_tokenizer.tokenize(text)
for sentence in sentences:
    print(f"Sentence: {sentence}")
```

## Advanced Usage

### 1. Processing Files

```python
# Clean text from a file
input_file = "input.txt"
cleaned_text = cleaner.clean_file(input_file)

# Save cleaned text
with open("cleaned_output.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

# Process multiple files
import glob
import os

for file_path in glob.glob("data/*.txt"):
    cleaned = cleaner.clean_file(file_path)
    output_path = os.path.join("cleaned", os.path.basename(file_path))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)
```

### 2. Combined Processing Pipeline

```python
# Create a complete processing pipeline
def process_text(text):
    # Clean the text
    cleaned = cleaner.clean_text(text)
    
    # Split into sentences
    sentences = sentence_tokenizer.tokenize(cleaned)
    
    # Tokenize each sentence
    word_tokenizer = BalochiWordTokenizer()
    processed_sentences = []
    
    for sentence in sentences:
        tokens = word_tokenizer.tokenize(sentence)
        processed_sentences.append(tokens)
    
    return processed_sentences

# Use the pipeline
text = """
منی نام احمد اِنت۔
من بلوچستان ءَ زندگ کنان۔
"""
results = process_text(text)
for sentence_tokens in results:
    print(f"Sentence tokens: {sentence_tokens}")
```

### 3. Error Handling

```python
def safe_process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        print(f"Error: File {file_path} has incorrect encoding")
        return None
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    
    try:
        cleaned = cleaner.clean_text(text)
        tokens = tokenizer.tokenize(cleaned)
        return tokens
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None
```

## Best Practices

1. **Always specify encoding**
   ```python
   with open(file_path, "r", encoding="utf-8") as f:
       text = f.read()
   ```

2. **Use context managers for file operations**
   ```python
   with open(output_file, "w", encoding="utf-8") as f:
       f.write(processed_text)
   ```

3. **Handle large files efficiently**
   ```python
   def process_large_file(file_path, chunk_size=1024):
       with open(file_path, "r", encoding="utf-8") as f:
           while True:
               chunk = f.read(chunk_size)
               if not chunk:
                   break
               # Process chunk
               cleaned = cleaner.clean_text(chunk)
               # Do something with cleaned chunk
   ```

4. **Proper error handling**
   ```python
   try:
       processed_text = cleaner.clean_text(text)
   except Exception as e:
       logger.error(f"Error processing text: {str(e)}")
       # Handle error appropriately
   ``` 