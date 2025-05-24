# API Reference

## Text Preprocessing

### BalochiTextCleaner

```python
from balochi_nlp.preprocessing import BalochiTextCleaner
```

Class for cleaning and normalizing Balochi text.

#### Methods

##### clean_text(text: str, remove_numbers: bool = True, preserve_special_chars: bool = True) -> str
Clean and normalize Balochi text.

**Parameters:**
- `text` (str): Input text to clean
- `remove_numbers` (bool): Whether to remove numerical digits
- `preserve_special_chars` (bool): Whether to preserve Balochi special characters

**Returns:**
- str: Cleaned text

**Example:**
```python
cleaner = BalochiTextCleaner()
text = "منی نام احمد 123 اِنت۔"
cleaned = cleaner.clean_text(text, remove_numbers=True)
```

##### clean_file(file_path: str, **kwargs) -> str
Clean text from a file.

**Parameters:**
- `file_path` (str): Path to the input file
- `**kwargs`: Arguments passed to clean_text()

**Returns:**
- str: Cleaned text

## Tokenization

### BalochiWordTokenizer

```python
from balochi_nlp.tokenizers import BalochiWordTokenizer
```

Class for tokenizing Balochi text into words.

#### Methods

##### tokenize(text: str) -> List[str]
Tokenize text into words.

**Parameters:**
- `text` (str): Input text to tokenize

**Returns:**
- List[str]: List of tokens

**Example:**
```python
tokenizer = BalochiWordTokenizer()
text = "منی نام احمد اِنت"
tokens = tokenizer.tokenize(text)
```

##### tokenize_with_affixes(text: str) -> List[Dict[str, str]]
Tokenize text with affix analysis.

**Parameters:**
- `text` (str): Input text to tokenize

**Returns:**
- List[Dict[str, str]]: List of dictionaries containing token information

### BalochiSentenceTokenizer

```python
from balochi_nlp.tokenizers import BalochiSentenceTokenizer
```

Class for tokenizing Balochi text into sentences.

#### Methods

##### tokenize(text: str) -> List[str]
Tokenize text into sentences.

**Parameters:**
- `text` (str): Input text to tokenize

**Returns:**
- List[str]: List of sentences

**Example:**
```python
tokenizer = BalochiSentenceTokenizer()
text = "منی نام احمد اِنت۔ من بلوچستان ءَ زندگ کنان۔"
sentences = tokenizer.tokenize(text)
```

## Utility Functions

### File Processing

#### read_text_file(file_path: str, encoding: str = 'utf-8') -> str
Read text from a file with proper encoding.

**Parameters:**
- `file_path` (str): Path to the input file
- `encoding` (str): File encoding (default: 'utf-8')

**Returns:**
- str: File contents

#### write_text_file(file_path: str, text: str, encoding: str = 'utf-8') -> None
Write text to a file with proper encoding.

**Parameters:**
- `file_path` (str): Path to the output file
- `text` (str): Text to write
- `encoding` (str): File encoding (default: 'utf-8') 