import random
import copy
from sample_glossary import sample_glossary

class Quiz_Word:
    """
    This class converts a tuple into a quiz word object
    that has two attributes: entry and definition

    Attributes
    ----------

    entry : str
        The target language structure

    translation : str
        A translation of the target language structure
    """

    def __init__(self,word_pair):
        self.entry = word_pair[0]
        self.translation = word_pair[1]

    def __str__(self):
        return self.entry

class Quiz_Question:
    """
    This class processes a list comprising instances of the
    Quiz_Word class. Whether the question will ask for the
    translation of a target language word or as for the
    target language word that best matches the translation
    is determined randomly.

    This creates a multiple choice question with a maximum of
    4 different answers

    Attributes:
    -----------

    word_list : list
        A list of instances of the Quiz_Word object
        
    entry_to_translation : bool
        Determines whether a translation will be the answer

    quiz_question : list
        A random selection from the word_list of 4 items,
        the first of which will be the entry/translation
        asked about

    Methods
    -------

    populate_quiz_question(word_list)
        Adds 4 random Quiz Words to the list quiz_question
    """
    def __init__(self,word_list):
        self.word_list = word_list
        self.entry_to_translation = bool(random.getrandbits(1))
        self.quiz_question = []

    def populate_quiz_question(self):
        """ Add up to 4 items to the list """

#        random.shuffle(word_list)

        copy_of_list = copy.deepcopy(word_list)

        counter = 5

        if len(copy_of_list) < 5:
            counter = len(copy_of_list)

        while counter > 1:
            self.quiz_question.append(copy_of_list.pop())
            counter -= 1

def create_list_of_words(glossary):
    """ convert all words in glossary into list of objects """

    word_list = []

    for g in glossary:
        word_list.append(Quiz_Word(g))

    return word_list

def create_list_of_questions(word_list):
    """ make questions, ensure they're unique """

    remaining_questions = 10
    
    if len(word_list) < 10:
        remaining_questions = len(word_list)

    question_list = {}

    while remaining_questions > 0:
        random.shuffle(word_list)
        # Make sure this word hasn't already been asked about
        if word_list[-1].entry not in question_list.keys():
            keyname = word_list[-1].entry
            question = Quiz_Question(word_list)
            question.populate_quiz_question()
            question_list[keyname] = question
            remaining_questions -= 1

    return question_list

def create_mc_quiz(question_list):
    """ translate the question list into a multiple choice quiz """
    mc_quiz = []
    for key, value in list_of_questions.items():
        if value.entry_to_translation == True:
            mc_quiz.append(f"What does '{value.quiz_question[0].entry}' mean in English?")
            for v in value.quiz_question:
                mc_quiz.append(v.translation)
        else:
            mc_quiz.append(f"How is '{value.quiz_question[0].translation}' best translated?")
            for v in value.quiz_question:
                mc_quiz.append(v.entry)
            
    return mc_quiz
            

if __name__ == '__main__':

    from sample_glossary import sample_glossary

    word_list = create_list_of_words(sample_glossary)

    list_of_questions = create_list_of_questions(word_list)
    mc_quiz = create_mc_quiz(list_of_questions)
    [print(q) for q in mc_quiz]
