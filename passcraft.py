import argparse
import random
import string
import math
import sys

try:
    import pyperclip
    CLIPBOARD_ENABLED = True
except ImportError:
    CLIPBOARD_ENABLED = False

def calculate_entropy(length, charset_size):
    return round(length * math.log2(charset_size), 2)

def generate_password(length, use_letters, use_digits, use_symbols, exclude_chars):
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if exclude_chars:
        chars = ''.join(c for c in chars if c not in exclude_chars)

    if not chars:
        raise ValueError("Character set is empty. Adjust your flags.")

    return ''.join(random.choices(chars, k=length)), len(chars)

def main():
    parser = argparse.ArgumentParser(description="passcraft: a secure CLI password generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-letters", action="store_true", help="Exclude letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--exclude", type=str, default="", help="Characters to exclude (e.g., 0O1Il)")
    parser.add_argument("--copy", action="store_true", help="Copy password to clipboard")
    parser.add_argument("--entropy", action="store_true", help="Display password entropy")

    args = parser.parse_args()

    try:
        password, charset_size = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_chars=args.exclude
        )

        print(f"Generated Password: {password}")

        if args.entropy:
            entropy = calculate_entropy(args.length, charset_size)
            print(f"Entropy: {entropy} bits")

        if args.copy:
            if CLIPBOARD_ENABLED:
                pyperclip.copy(password)
                print("Password copied to clipboard.")
            else:
                print("Clipboard functionality requires `pyperclip`.")

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

if __name__ == "__main__":
    main()
