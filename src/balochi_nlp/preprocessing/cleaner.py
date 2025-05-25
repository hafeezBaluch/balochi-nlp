"""Text cleaning utilities for Balochi text."""
import re

class BalochiTextCleaner:
    """A class for cleaning and preprocessing Balochi text.

    This class provides methods to clean Balochi text by removing unwanted
    elements like URLs, email addresses, numbers, and special characters.
    """

    def __init__(self):
        """Initialize the cleaner with regex patterns."""
        self.url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self.email_pattern = re.compile(r'\S+@\S+\.\S+')
        self.number_pattern = re.compile(r'\d+')
        self.emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+"
        )

    def clean_text(
        self,
        text: str,
        remove_urls: bool = True,
        remove_emails: bool = True,
        remove_numbers: bool = True,
        remove_emojis: bool = True,
        preserve_special_chars: bool = True
    ) -> str:
        """Clean the input text by removing unwanted elements.

        Args:
            text: Input text to clean
            remove_urls: Whether to remove URLs
            remove_emails: Whether to remove email addresses
            remove_numbers: Whether to remove numeric digits
            remove_emojis: Whether to remove emoji characters
            preserve_special_chars: Whether to preserve special Balochi chars

        Returns:
            Cleaned text string
        """
        if remove_urls:
            text = self.url_pattern.sub('', text)
        if remove_emails:
            text = self.email_pattern.sub('', text)
        if remove_numbers:
            text = self.number_pattern.sub('', text)
        if remove_emojis:
            text = self.emoji_pattern.sub('', text)

        # Normalize whitespace
        text = ' '.join(text.split())

        return text

    def clean_file(self, file_path: str, **kwargs) -> str:
        """Clean text from a file.

        Args:
            file_path: Path to the input file
            **kwargs: Additional arguments passed to clean_text()

        Returns:
            Cleaned text string
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.clean_text(text, **kwargs)
