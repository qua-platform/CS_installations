
def play_sequence(sequence_list, depth):
i = declare(int)
with for_(i, 0, i <= depth, i + 1):
    with switch_(sequence_list[i], unsafe=True):
        with case_(0):
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(1):
            play("y90", "qubit")
        with case_(2):
            play("x90", "qubit")
        with case_(3):
            play("y90", "qubit")
            play("x90", "qubit")
        with case_(4):
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(5):
            play("y90", "qubit")
            play("y90", "qubit")
        with case_(6):
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(7):
            play("y90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(8):
            play("y90", "qubit")
            play("y90", "qubit")
            play("x90", "qubit")
        with case_(9):
            play("y90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(10):
            play("y90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
        with case_(11):
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(12):
            play("x90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(13):
            play("x90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
        with case_(14):
            play("y90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
        with case_(15):
            play("y90", "qubit")
            play("y90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(16):
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(17):
            play("y90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(18):
            play("y90", "qubit")
            play("y90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
        with case_(19):
            play("x90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
        with case_(20):
            play("y90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
            play("x90", "qubit")
        with case_(21):
            play("y90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(22):
            play("y90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
        with case_(23):
            play("y90", "qubit")
            play("x90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")
            play("y90", "qubit")



# Macro to calculate exact duration of generated sequence at a given depth
def generate_sequence_time(sequence_list, depth):
j = declare(int)
duration = declare(int)
assign(duration, 0)  # Ensures duration is reset to 0 for every depth calculated
with for_(j, 0, j <= depth, j + 1):
    with switch_(sequence_list[j], unsafe=True):
        with case_(0):
            # wait(x180_len // 4, "qubit")
            assign(duration, duration + x90_len+x90_len+x90_len+x90_len)
        with case_(1):
            # play("x180", "qubit")
            assign(duration, duration + y90_len)
        with case_(2):
            # play("y180", "qubit")
            assign(duration, duration + x90_len)
        with case_(3):
            # play("y180", "qubit")
            # play("x180", "qubit")
            assign(duration, duration + y90_len + x90_len)
        with case_(4):
            # play("x90", "qubit")
            # play("y90", "qubit")
            assign(duration, duration + x90_len + y90_len)
        with case_(5):
            # play("x90", "qubit")
            # play("-y90", "qubit")
            assign(duration, duration + y90_len + y90_len)
        with case_(6):
            # play("-x90", "qubit")
            # play("y90", "qubit")
            assign(duration, duration + x90_len + x90_len)
        with case_(7):
            # play("-x90", "qubit")
            # play("-y90", "qubit")
            assign(duration, duration + y90_len + x90_len+x90_len)
        with case_(8):
            # play("y90", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + y90_len + y90_len+x90_len)
        with case_(9):
            # play("y90", "qubit")
            # play("-x90", "qubit")
            assign(duration, duration + y90_len + x90_len+y90_len)
        with case_(10):
            # play("-y90", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + y90_len + y90_len+y90_len)
        with case_(11):
            # play("-y90", "qubit")
            # play("-x90", "qubit")
            assign(duration, duration + x90_len + x90_len+x90_len)
        with case_(12):
            # play("x90", "qubit")
            assign(duration, duration + x90_len+x90_len+y90_len)
        with case_(13):
            # play("-x90", "qubit")
            assign(duration, duration + x90_len+y90_len+y90_len)
        with case_(14):
            # play("y90", "qubit")
            assign(duration, duration + y90_len+x90_len+y90_len+y90_len)
        with case_(15):
            # play("-y90", "qubit")
            assign(duration, duration + y90_len+y90_len+x90_len+y90_len)
        with case_(16):
            # play("-x90", "qubit")
            # play("y90", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + x90_len + x90_len + x90_len+y90_len)
        with case_(17):
            # play("-x90", "qubit")
            # play("-y90", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + y90_len + x90_len + x90_len+x90_len)
        with case_(18):
            # play("x180", "qubit")
            # play("y90", "qubit")
            assign(duration, duration + y90_len + y90_len+x90_len+x90_len)
        with case_(19):
            # play("x180", "qubit")
            # play("-y90", "qubit")
            assign(duration, duration + x90_len + y90_len+y90_len+y90_len)
        with case_(20):
            # play("y180", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + y90_len + y90_len+y90_len+x90_len)
        with case_(21):
            # play("y180", "qubit")
            # play("-x90", "qubit")
            assign(duration, duration + y90_len + y90_len+y90_len+x90_len+y90_len)
        with case_(22):
            # play("x90", "qubit")
            # play("y90", "qubit")
            # play("x90", "qubit")
            assign(duration, duration + y90_len + x90_len + x90_len+x90_len+y90_len)
        with case_(23):
            # play("-x90", "qubit")
            # play("y90", "qubit")
            # play("-x90", "qubit")
            assign(duration, duration + y90_len + x90_len + y90_len+y90_len+y90_len)
return duration
