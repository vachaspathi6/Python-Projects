import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    file_path = input("Enter music file path: ")
    play_music(file_path)
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    main()
