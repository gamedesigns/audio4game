import pygame
import threading

class AudioManager:
    def __init__(self, frequency=44100, size=-16, channels=8, buffer=4096, num_reserved=2):
        pygame.mixer.init(frequency=frequency, size=size, channels=channels, buffer=buffer)
        self.num_reserved = num_reserved
        pygame.mixer.set_reserved(self.num_reserved)
        self.sounds = {}
        self.music = {}
        self.music_layers = {}
        self.current_music = None
        self.music_volume = 1.0
        self.sound_effects_volume = 1.0
        self.music_muted = False
        self.sound_effects_muted = False

    def initialize_sounds(self, sound_files):
        for name, file_path in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(file_path)
            except pygame.error as e:
                print(f"Error loading sound {name}: {e}")

    def initialize_music(self, music_files):
        for name, file_path in music_files.items():
            self.music[name] = file_path

    def initialize_music_layers(self, music_layers):
        for name, file_path in music_layers.items():
            self.add_music_layer(name, file_path)

    def add_music_layer(self, name, file_path):
        try:
            self.music_layers[name] = pygame.mixer.Sound(file_path)
        except pygame.error as e:
            print(f"Error loading music layer {name}: {e}")

    def play_sound(self, name, priority=False):
        if not self.sound_effects_muted and name in self.sounds:
            if priority:
                for i in range(self.num_reserved):
                    channel = pygame.mixer.Channel(i)
                    if not channel.get_busy():
                        channel.set_volume(self.sound_effects_volume)
                        channel.play(self.sounds[name])
                        return
            else:
                sound = self.sounds[name]
                sound.set_volume(self.sound_effects_volume)
                sound.play()

    def play_music(self, track, fade_time=0):
        if not self.music_muted and track in self.music:
            if self.current_music != track:
                if fade_time > 0:
                    pygame.mixer.music.fadeout(fade_time)
                    while pygame.mixer.music.get_busy():
                        pygame.time.delay(100)
                pygame.mixer.music.load(self.music[track])
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(-1)
                self.current_music = track

    def play_music_layer(self, name):
        if name in self.music_layers:
            layer_sound = self.music_layers[name]
            layer_sound.play(-1)  # Loop the layer

    def stop_music_layer(self, name):
        if name in self.music_layers:
            layer_sound = self.music_layers[name]
            layer_sound.stop()

    def stop_all_music_layers(self):
        for layer_sound in self.music_layers.values():
            layer_sound.stop()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None

    def mute_music(self):
        if not self.music_muted:
            self.music_muted = True
            pygame.mixer.music.set_volume(0.0)

    def unmute_music(self):
        if self.music_muted:
            self.music_muted = False
            pygame.mixer.music.set_volume(self.music_volume)

    def mute_sound_effects(self):
        if not self.sound_effects_muted:
            self.sound_effects_muted = True
            for sound in self.sounds.values():
                sound.set_volume(0.0)

    def unmute_sound_effects(self):
        if self.sound_effects_muted:
            self.sound_effects_muted = False
            for sound in self.sounds.values():
                sound.set_volume(self.sound_effects_volume)

    def set_music_volume(self, volume):
        self.music_volume = volume
        if not self.music_muted:
            pygame.mixer.music.set_volume(volume)

    def set_sound_effects_volume(self, volume):
        self.sound_effects_volume = volume
        if not self.sound_effects_muted:
            for sound in self.sounds.values():
                sound.set_volume(volume)

    def stop_all(self):
        for i in range(pygame.mixer.get_num_channels()):
            channel = pygame.mixer.Channel(i)
            channel.stop()
        pygame.mixer.music.stop()
        self.current_music = None