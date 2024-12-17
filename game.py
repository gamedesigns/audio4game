import pygame
import sys
from audio_manager import AudioManager

def main_menu(audio):
    audio.play_music('menu', fade_time=2000)
    while True:
        print("\nMain Menu")
        print("1. Start Game")
        print("2. Settings")
        print("3. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            battle_scene(audio)
        elif choice == "2":
            settings(audio)
        elif choice == "3":
            print("Goodbye!")
            audio.stop_all()
            pygame.quit()
            sys.exit()
        else:
            print("Invalid option. Please try again.")

def battle_scene(audio):
    audio.play_music('battle', fade_time=2000)
    while True:
        print("\nBattle Scene")
        print("1. Attack")
        print("2. Special")
        print("3. Run")
        choice = input("Choose an action: ")
        
        if choice == "1":
            audio.play_sound('attack', priority=True)
        elif choice == "2":
            audio.play_sound('special', priority=True)
        elif choice == "3":
            main_menu(audio)
        else:
            print("Invalid action. Please try again.")

def settings(audio):
    while True:
        print("\nSettings")
        print("1. Mute Music")
        print("2. Unmute Music")
        print("3. Mute Sound Effects")
        print("4. Unmute Sound Effects")
        print("5. Back")
        choice = input("Choose an option: ")
        
        if choice == "1":
            audio.mute_music()
        elif choice == "2":
            audio.unmute_music()
        elif choice == "3":
            audio.mute_sound_effects()
        elif choice == "4":
            audio.unmute_sound_effects()
        elif choice == "5":
            return
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    pygame.init()
    audio = AudioManager()
    
    sound_files = {
        'attack': './sounds/attack.wav',
        'special': './sounds/special.wav',
        'door_open': './sounds/door_open.wav',
    }

    music_files = {
        'menu': './music/menu_music.mp3',
        'battle': './music/battle_music.mp3',
    }
    
    audio.initialize_sounds(sound_files)
    audio.initialize_music(music_files)
    
    main_menu(audio)