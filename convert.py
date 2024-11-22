import markdown
import pdfkit
import sys

def markdown_to_pdf(markdown_text, output_pdf):
    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)
    # Convert HTML to PDF
    pdfkit.from_string(html, output_pdf)
    print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert.py '<markdown_text>' <output_pdf>")
    else:
        markdown_input = sys.argv[1]
        output_file = sys.argv[2]
        markdown_to_pdf(markdown_input, output_file)
