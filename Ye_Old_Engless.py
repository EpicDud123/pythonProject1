def to_old_english(text):
    replacements = {
        'th': 'þ',
        'w': 'ƿ',
        'y': 'ȳ',
        'thou': 'þū',
        'your': 'ȳower',
        'you': 'þē',
        'is': 'ys',
        'are': 'art',
        'Th': 'Þ',
        'W': 'Ƿ',
        'Y': 'Ȳ',
        'Thou': 'Þū',
        'Your': 'Ȳower',
        'You': 'Þē',
        'Is': 'Ys',
        'Are': 'Art',
        # Add more replacements as desired
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


input_text = "Can you change text into Old English?"
old_english_text = to_old_english(input_text)
print(old_english_text)
