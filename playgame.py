import pygame
import time


def play_midi_file(midi_file_path):
    """
    Plays a MIDI file using pygame.mixer.music.
    """
    pygame.init()
    # Initialize the mixer with default values
    # The frequency can sometimes affect MIDI playback quality/timing
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 1024
    pygame.mixer.init(freq, bitsize, channels, buffer)

    try:
        # Load the MIDI file
        pygame.mixer.music.load(midi_file_path)

        # Set optional volume
        pygame.mixer.music.set_volume(0.7)

        print(f"Playing {midi_file_path}...")

        # Start playing the music (-1 means loop indefinitely, 0 means play once)
        pygame.mixer.music.play(0)

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Error playing MIDI file: {e}")
    finally:
        # Stop the music and quit the mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()


if __name__ == "__main__":
    # Replace 'your_song.mid' with the path to your actual MIDI file
    midi_file = "/Users/chrislomeli/Source/PROJECTS/music21/music21-sandbox/output.mid"
    try:
        # You would need an actual midi file at this path
        # Example of running the function:
        play_midi_file(midi_file)
        # print(f"Please ensure a MIDI file named '{midi_file}' is in the script directory or provide the full path.")

    except FileNotFoundError:
        print(f"File '{midi_file}' not found. Please check the file path.")

