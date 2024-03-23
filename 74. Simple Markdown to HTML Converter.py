import markdown

def convert_markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def main():
    markdown_text = input("Enter Markdown text: ")
    html_text = convert_markdown_to_html(markdown_text)
    print("Converted HTML:")
    print(html_text)

if __name__ == "__main__":
    main()
