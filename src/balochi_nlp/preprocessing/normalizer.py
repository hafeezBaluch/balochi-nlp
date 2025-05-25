"""Normalization utilities for Balochi text."""
import re

class BalochiTextNormalizer:
    """A class for normalizing Balochi text."""

    def __init__(self):
        """Initialize normalizer with character mappings."""
        self.char_map = {
            'ي': 'ی',
            'ك': 'ک',
            'ة': 'ہ',
            'ۀ': 'ہ',
        }
        self.diacritics = re.compile(r'[\u064B-\u065F\u0670]')

    def normalize(self, text: str, remove_diacritics: bool = False) -> str:
        """Normalize Balochi text.

        Args:
            text: Input text to normalize
            remove_diacritics: Whether to remove diacritical marks

        Returns:
            Normalized text string
        """
        # Replace characters according to mapping
        for old, new in self.char_map.items():
            text = text.replace(old, new)

        # Remove diacritics if requested
        if remove_diacritics:
            text = self.diacritics.sub('', text)

        return text


def normalize_text(text):
    """
    Normalize the input text by converting it to lowercase and removing extra spaces.

    Args:
        text (str): The input text to normalize.

    Returns:
        str: The normalized text.
    """
    # Convert to lowercase
    normalized_text = text.lower()
    # Remove extra spaces
    normalized_text = " ".join(normalized_text.split())
    return normalized_text


def handle_diacritics(text):
    """
    Handle diacritics in the input text.

    Args:
        text (str): The input text to process.

    Returns:
        str: The text with diacritics handled.
    """
    # Example implementation (to be customized based on Balochi language specifics)
    # This is a placeholder for actual diacritic handling logic
    return text.replace("َ", "a").replace("ِ", "i").replace("ُ", "u")


def normalize_corpus(corpus):
    """
    Normalize a corpus of text.

    Args:
        corpus (list of str): A list of text strings to normalize.

    Returns:
        list of str: A list of normalized text strings.
    """
    return [normalize_text(handle_diacritics(text)) for text in corpus]
