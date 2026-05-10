from os import listdir
import wave

test_string = "Pociąg ze stacji Warszawa Wschodnia do stacji Poznań Głowny przez stacje Kutno, Konin, odjedzie z toru drugiego przy peronie trzecim"

def string_converter(text):
    text = text.lower()
    result = ""

    polish_letters = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }

    for l in text:
        if l in polish_letters:
            result += polish_letters[l]
        elif l == " ":
            result += "_"
        else:
            result += l

    return result


def file_finder(text):
    wav_files = {}
    for file in listdir("do_z_stacji"):
        if file.endswith(".wav"):
            file_name_text = file.replace(".wav", "")
            if file_name_text in text:
                wav_files[file_name_text] = "do_z_stacji/" + file

    for file in listdir("perony_i_tory"):
        if file.endswith(".wav"):
            file_name_text = file.replace(".wav", "")
            if file_name_text in text:
                wav_files[file_name_text] = "perony_i_tory/" + file

    for file in listdir("stacje"):
        if file.endswith(".wav"):
            file_name_text = file.replace(".wav", "")
            if file_name_text in text:
                wav_files[file_name_text] = "stacje/" + file

    return wav_files


def wav_create(text, wav_files, file_name):
    audio_files = {}
    current_text = ""
    parameters = None
    for l in text:
        if current_text == "" and l == "_" or l == ",":
            continue

        current_text += l
        if current_text in wav_files:
            audio_files[wav_files[current_text]] = ""
            current_text = ""

    for audio in audio_files:
        try:
            with wave.open(audio, "rb") as w:
                if parameters is None:
                    parameters = w.getparams()
                audio_files[audio] = w.readframes(w.getnframes())
        except Exception as e:
            print(f"Error with file {audio}: {e}")

    if parameters:
        try:
            with wave.open(file_name, "wb") as output:
                output.setparams(parameters)
                for file in audio_files:
                    output.writeframes(audio_files[file])

            print("Stworzono nowe nagranie:", file_name)
        except Exception as e:
            print(f"Error with creating audio file {file_name}: {e}")


converted_string = string_converter(test_string)

files = file_finder(converted_string)

print(files)

wav_create(converted_string, files, "test.wav")
