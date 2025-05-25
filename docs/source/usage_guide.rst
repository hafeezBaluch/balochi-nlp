Usage Guide
===========

Basic Usage
----------

The Balochi NLP library provides various NLP tools for processing Balochi text.

Text Preprocessing
----------------

.. code-block:: python

    from balochi_nlp.preprocessing import normalize_text, clean_text
    
    text = "Your Balochi text here"
    normalized = normalize_text(text)
    cleaned = clean_text(text)

Tokenization
-----------

.. code-block:: python

    from balochi_nlp.tokenizers import word_tokenize, sentence_tokenize
    
    # Word tokenization
    words = word_tokenize(text)
    
    # Sentence tokenization
    sentences = sentence_tokenize(text)

Advanced Features
---------------

For more advanced features and detailed examples, please refer to the API Reference section. 