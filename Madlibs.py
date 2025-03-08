msg  = """It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation)
The hospital is a/an (Adjective) place, there are a lot of (Adjectivez) (Noun) here There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first I've decorated my room with (Numberz) (Nounz). Today I talked to a doctor and they were wearing a (Noung) on their ( Part of the Body 2) I heard that all doctors (Verb) (Nound) every day for breakfast. The most (Adjectives) thing about being in the hospital is the (Silly Word) (Noun) I """



number = int(input("Input number : "))
measure_of_time = input("Input time: ")
mode_of_transportation = input("Input Mode of Transportation: ")
adjective = input("Input adjective: ")
adjectivez = input("Input adjectivez: ")
noun = input("Input Noun: ")
color = input("Input color:")
Part_of_the_Body = input("Input: Part_of_the_Body ")
Verb = input("Input: Verb ")
Numberz = input("Input: Numberz")
Nounz = input("Input: Nounz")
Noung = input("Input: Noung")
Part_of_the_Body2 = input("Input: Part_of_the_Body ")
Verb1 = input("Input: Verb ")
Nound = input("Input: Nound ")
Adjectives1 = input("Input adjectives: ")
Silly_word = input("Input silly_world ")
Noun = input("Input: Noun ")



msg = f"""It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}
The hospital is a/an {adjective} place, there are a lot of {adjectivez} {noun} here There are nurses here who have {color} {Part_of_the_Body}. If someone wants to come into my room I told them that they have to {Verb} first I've decorated my room with {Numberz} {Nounz}. Today I talked to a doctor and they were wearing a {Noung} on their {Part_of_the_Body2} I heard that all doctors {Verb} {Nound} every day for breakfast. The most {Adjectives1}thing about being in the hospital is the {Silly_word} {Noun} I """

print(msg)
