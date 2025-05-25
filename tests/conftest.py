"""Pytest configuration file."""

import os
import sys
import tempfile

import pytest


@pytest.fixture(scope="session")
def test_data_dir(tmp_path_factory):
    """Create and return a temporary directory for test data."""
    return tmp_path_factory.mktemp("test_data")


@pytest.fixture(scope="session")
def sample_balochi_text():
    """Return a sample Balochi text for testing."""
    return """
    منی نام احمد اِنت۔ من بلوچستان ءَ زندگ کنان۔
    من بلوچی زبان ءَ گپ کنان۔
    """


@pytest.fixture(scope="session")
def sample_mixed_text():
    """Return a sample text with mixed content for testing."""
    return """
    منی نام احمد اِنت۔ https://example.com
    Email: user@email.com
    Numbers: 123 456 789
    Latin: ABC DEF GHI
    Emojis: 😊 🌟 💫
    """


@pytest.fixture(scope="session")
def sample_special_chars():
    """Return a sample text with special Balochi characters."""
    return "دشتءِ کتابءَ گسءُ"


@pytest.fixture(scope="session")
def sample_compound_words():
    """Return a sample text with compound Balochi words."""
    return "کتاب\u200cخانہ گل\u200cزار"


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "cleaner: mark test as cleaner related")
    config.addinivalue_line("markers", "tokenizer: mark test as tokenizer related")
    config.addinivalue_line("markers", "integration: mark test as integration test")
