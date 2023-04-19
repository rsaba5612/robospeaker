import os


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 created by Sab")
    while True:
     x = input("Enter what you want me to speak: ")
     if x== "q":
        break
     if os.name == 'nt':  # for Windows
         os.system(f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\"")
    else:  # for Linux and macOS
        os.system(f"say {x}")
