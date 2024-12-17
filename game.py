import pygame
import sys
from audio_manager import AudioManager

def main_menu(audio):
    audio.stop_all_music_layers()
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
    current_music = None
    while True:
        print("\nBattle Scene")
        print("1. Attack")
        print("2. Special")
        print("3. Run")
        print("a. Instant Attack (a)")
        print("m. Monster Music")
        print("u: Increase music volume")
        print("d: Decrease music volume")
        print("U: Increase sound effects volume")
        print("D: Decrease sound effects volume")
        choice = input("Choose an action: ")
        
        if choice == "1":
            audio.play_sound('attack', priority=True)
        elif choice == "2":
            audio.play_sound('special', priority=True)
        elif choice == "3":
            main_menu(audio)
        elif choice == "a":
            audio.play_sound('attack', priority=True)
        elif choice == "m":
            current_music = audio.current_music
            audio.stop_music()
            audio.stop_all_music_layers()
            monster_music_submenu(audio)
            audio.stop_all_music_layers()
            audio.play_music(current_music, fade_time=2000)
        elif choice == "u":
            current_volume = audio.music_volume
            audio.set_music_volume(min(current_volume + 0.1, 1.0))
        elif choice == "d":
            current_volume = audio.music_volume
            audio.set_music_volume(max(current_volume - 0.1, 0.0))
        elif choice == "U":
            current_volume = audio.sound_effects_volume
            audio.set_sound_effects_volume(min(current_volume + 0.1, 1.0))
        elif choice == "D":
            current_volume = audio.sound_effects_volume
            audio.set_sound_effects_volume(max(current_volume - 0.1, 0.0))
        else:
            print("Invalid action. Please try again.")

def monster_music_submenu(audio):
    active_layers = set()
    while True:
        print("\nMonster Music")
        print("Available Layers:")
        print("q. Monster Perc (on/off)")
        print("w. Monster Bass (on/off)")
        print("e. Monster Lead (on/off)")
        print("b. Back")
        choice = input("Choose an option: ")
        
        if choice == "q":
            layer = 'monster_perc'
            if layer in active_layers:
                audio.stop_music_layer(layer)
                active_layers.remove(layer)
            else:
                audio.play_music_layer(layer)
                active_layers.add(layer)
        elif choice == "w":
            layer = 'monster_bass'
            if layer in active_layers:
                audio.stop_music_layer(layer)
                active_layers.remove(layer)
            else:
                audio.play_music_layer(layer)
                active_layers.add(layer)
        elif choice == "e":
            layer = 'monster_lead'
            if layer in active_layers:
                audio.stop_music_layer(layer)
                active_layers.remove(layer)
            else:
                audio.play_music_layer(layer)
                active_layers.add(layer)
        elif choice == "b":
            return
        else:
            print("Invalid option. Please try again.")

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

    music_layers = {
        'monster_perc': './music/monster_perc.mp3',
        'monster_bass': './music/monster_bass.mp3',
        'monster_lead': './music/monster_lead.mp3',
    }
    
    audio.initialize_sounds(sound_files)
    audio.initialize_music(music_files)
    audio.initialize_music_layers(music_layers)
    
    main_menu(audio)