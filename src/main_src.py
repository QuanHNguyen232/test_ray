def main():
    print("Hello from test-ray/src!")
    try:
        import emoji
        print(emoji.emojize("This is a test :thumbs_up:"))
    except ImportError:
        print("Emoji library not found. Please install it to see emojis.")


if __name__ == "__main__":
    main()
