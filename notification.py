import pygame
import time

def play_sound(sound_file_path):
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(sound_file_path)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

        # Allow time for the sound to play
        time.sleep(3)

    except pygame.error as e:
        print(f"Error playing sound: {e}")

    finally:
        pygame.mixer.quit()

sound_file_path = "notification.wav"


