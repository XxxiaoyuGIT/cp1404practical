def count_word_occurrences(text):
    word_count = {}
    words = text.split()

    for word in words:
        # Remove punctuation and convert to lowercase for consistency
        word = word.strip('.,!?()[]{}"\'').lower()

        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Find the maximum width for formatting
    max_width = max(len(word) for word in word_count)

    # Sort the dictionary by keys
    sorted_word_count = sorted(word_count.items())

    # Print the counts with aligned formatting
    for word, count in sorted_word_count:
        print(f"{word:{max_width}} : {count}")


def main():
    user_input = input("Enter a string: ")
    count_word_occurrences(user_input)


if __name__ == "__main__":
    main()
