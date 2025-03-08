def number_to_words(n):
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def words_under_1000(num):
        result = []
        if num >= 100:
            result.append(ones[num // 100] + " hundred")
            num %= 100
        if 10 < num < 20:
            result.append(teens[num - 10])
        else:
            if num >= 10:
                result.append(tens[num // 10])
            if num % 10:
                result.append(ones[num % 10])
        return " ".join(filter(None, result))

    result = []
    chunk_count = 0  # Track thousands place
    while n > 0:
        chunk = n % 1000
        if chunk:
            result.append(words_under_1000(chunk) + (" " + thousands[chunk_count] if thousands[chunk_count] else ""))
        n //= 1000
        chunk_count += 1

    return " ".join(reversed(result))

# Example Usage
num = int(input("Enter a number: "))
print(number_to_words(num))
