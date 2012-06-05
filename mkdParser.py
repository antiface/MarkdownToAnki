# Markdown to Anki Parser
# Author: Peter Dailey
# The following program takes markdown files and parses them by headings.
# This program was written so that I could parse class notes into plain text files and export them into the flashcard program Anki, automatically generating decks of flashcards.
# Note, this program assumes that notes are written in question-answer formats. Questions are indicated with ##, and anything after is interpreted as part of the answer. 

# Anki determines the number of fields in the f by looking at the first (non-commented) line. Any other lines in the f which dont match this number will be ignored. The first line also defines the separating character - if Anki finds a ; on the first line it will use that - if it finds a comma it'll use that, etc.


def write_file_deck(list_notes, question_header, file_deck):
    for line in list_notes:
    # insert line breaks between sections
        if line.startswith('# '): # Strip the "#" and leading and trailing whitespace from the line
            # This is read as a comment by Anki
            line = line.strip('#')
            line = line.strip()
            file_deck.write('\n# Section: ' + line)
        elif line.startswith(question_header + ' '):
            line = line.strip(question_header)
            line = line.strip()
            file_deck.write("\n\n" + line + '\t')
        else:
            file_deck.write(line + '<br>') # find the first occurence of a question
    
    return line

def read_file(name_file):
    try:
        f = open(name_file + ".mkd")
        # reads the lines to a list and strips the newline characters
        raw_list = f.read().splitlines()
        mkd_list = filter(None, raw_list)
        return mkd_list
    except:
        print('Exception, cannot open f.')
    finally:
        f.close()


print("\nmkdParser converts markdown files into text files that can be imported into the flashcard application Anki.")
name_notes = raw_input("\nEnter the name of the markdown f you would like to convert to an .txt f\n>> ")
list_notes = read_file(name_notes)

#  Ask the user to define the character they use to begin questions, or have a question mark denote the presence of questions
question_header = raw_input("\nWhat character(s) in the question header in your notes?\n>> ")

# Create file to be converted to an anki name_deck
name_deck = (name_notes + '.txt')
file_deck = open(name_deck, 'file_deck')

# In this program [tab] is used to denote a field, and we will default two fields, one for the question and one for the answer.
print("Writing f " + name_deck + ".")
file_deck.write("Dummy question to guarantee \t Only two fields\n")

# Iterate over the list of strings from the markdown f
line = write_file_deck(list_notes, question_header, file_deck)

# Creates a series of text files that can be converted to audio tracks and imported into itunes. 
#counter = 0
#for line in name_notes:
#    if line.startswith("# "):
#        counter = counter + 1
#        track = (name_notes + '.txt')
#        track.append(counter.toString)
#        f = open(track , 'file_deck')
#        f.write(line)
#        f.close()


file_deck.close()
print('Deck written.')
