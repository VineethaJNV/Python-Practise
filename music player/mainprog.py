import values
import winsound

def play_song(swar,song,duration):
    for i in range (len(song)):
        temp = duration[i]
        temp2 = temp * 300
        winsound.Beep(swar[song[i]],temp2)

print("\nWelcome to Python music\n")
while True:
    print("1:Display songs, 2:Enter your own song, 3:exit")
    choice = int(input("your choice please:"))
    if(choice ==1):
        print("Choose the language, 1:English, 2:Classical, 3:Tamil, 4:Hindi, 5:Patroitic")
        choice1 = int(input("your choice please:"))
        if(choice1 == 1):
            print("Enjoy Happy Birthday song")
            play_song(values.swar,values.hp_song,values.hp_duration)
        if(choice1 == 2):
            print("Enjoy your favourite Classical song from Mohana raga")
            play_song(values.swar,values.classical_song,values.classical_duration)
        if(choice1 == 3):
            print("Enjoy Thuli thuli song from Paiyaa")
            play_song(values.swar,values.thuli_song,values.thuli_duration)
        if(choice1 == 4):
            print("Enjoy latest hindi songs on python music")
            play_song(values.swar,values.r_song,values.r_duration)
        if(choice1 == 5):
            print("1:Vande Mataram, 2:National Anthem")
            preference = int(input("Enter your choice:"))
            if(preference == 1):
                print("Enjoy vandemataram song")
                play_song(values.swar,values.vande_song,values.vande_duration)
            if(preference == 2):
                print("Stand up!, National Anthem is going to start")
                play_song(values.swar,values.na_song,values.na_duration)
            else:
                print("Invalid choice")
                
    if(choice == 2):
        song =[]
        duration = []
        input_swar = " "
        while True:
            input_swar = input("Enter the swaras to play the song:")
            if input_swar == "null":
                break
            song.append(input_swar)
            input_duration =int(input("Enter the duration of each swara"))
            duration.append(input_duration)
        print(song)
        play_song(values.swar,song,duration)
    if(choice == 3):
        break
    else:
        ("Invalid choice")
