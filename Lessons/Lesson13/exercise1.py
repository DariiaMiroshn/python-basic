import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):

    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{html_file}' not found in directory with program.")
        return

    clean_text = re.sub(r'<[^>]*>', '', html_content)
    final_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    final_result = "\n".join(final_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_result)

    print(f"File '{html_file}' was successfully cleaned, saved as '{result_file}'")

delete_html_tags('draft.html')