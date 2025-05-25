"""Command line interface for Balochi NLP tools."""
import argparse
import sys

def create_parser():
    """Create the command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Balochi NLP command line tools"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Clean text command
    clean_parser = subparsers.add_parser(
        "clean", help="Clean and normalize Balochi text"
    )
    clean_parser.add_argument(
        "input", help="Input text or file path"
    )
    clean_parser.add_argument(
        "-o", "--output",
        help="Output file path (if not specified, prints to stdout)",
        default=None
    )
    clean_parser.add_argument(
        "--preserve-numbers",
        help="Preserve numbers in the text",
        action="store_true"
    )
    clean_parser.add_argument(
        "--preserve-urls",
        help="Preserve URLs in the text",
        action="store_true"
    )
    clean_parser.add_argument(
        "--preserve-emails",
        help="Preserve email addresses in the text",
        action="store_true"
    )

    return parser

def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "clean":
        from balochi_nlp.preprocessing.cleaner import BalochiTextCleaner
        cleaner = BalochiTextCleaner()

        # Read input
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            text = args.input

        # Clean text
        cleaned_text = cleaner.clean_text(
            text,
            remove_numbers=not args.preserve_numbers,
            remove_urls=not args.preserve_urls,
            remove_emails=not args.preserve_emails
        )

        # Output
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(cleaned_text)
        else:
            print(cleaned_text)

if __name__ == "__main__":
    main()
