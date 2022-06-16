"""
LESSON: RPS Wars Project
WARMUP 4
"""

# CHANGE LETTER LIST FUNCTION
def print_faces(times):
    # Validate input and respond differently if the
    # user's value was 0 or negative
    if times <= 0:
        print("Oh, so you're actually happy? That's great!")
        print("Here, have a smiley for the road anyway: :)")
        return

    # Calculate output
    output_string = ""
    for i in range(times):
        output_string += ":) "

    # Print output
    print("I see. Maybe this will help?")
    print(output_string)

# MAIN PROGRAM
print("You seem to need cheering up.")
sad = int(input("How intense would you rate your sadness? (Please give an integer.) "))
print()
print_faces(sad)
