from pyfiglet import Figlet

def generate_ascii_art(text):
    figlet = Figlet()
    return figlet.renderText(text)

def main():
    text = input("Enter text to generate ASCII art: ")
    ascii_art = generate_ascii_art(text)
    print("ASCII Art:")
    print(ascii_art)

if __name__ == "__main__":
    main()
