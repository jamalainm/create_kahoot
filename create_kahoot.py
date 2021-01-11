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

        copy_of_list = copy.deepcopy(self.word_list)

        counter = 5

        if len(copy_of_list) < 5:
            counter = len(copy_of_list)

        while counter > 1:
            self.quiz_question.append(copy_of_list.pop())
            counter -= 1

class Quiz:
    """
    When given a list of tuples, comprising an entry and a translation,
    this class can produce an excel file compatible with kahoot,
    so that a multiple choice quiz can be uploaded to the website.

    By default, the first selection will be the correct answer and the time
    limit will be 10 seconds.

    Attributes:
    -----------

    glossary : list:
        This list comprises a list of tuples: an entry and a translation

    word_list : list
        This list comprises Quiz_Word objects.

    dict_of_questions : dict
        This dict has Quiz_Question objects as values and the word in question as key

    mc_quiz : list
        This list comprises strings that can be pasted into the kahoot quiz template

    Methods:
    --------

    create_list_of_words
        converts all words in glossary into list of Quiz_Word objects

    create_list_of_questions
        processes a list of Quiz_Words into a list of Quiz_Question objects

    create_mc_quiz
        processes a list of Quiz_Question objects into a list of strings
        that can then be used in the kahoot quiz template

    """

    def __init__(self,glossary):
        self.glossary = glossary
        self.word_list = []
        self.dict_of_questions = {}
        self.mc_quiz = []

    def create_list_of_words(self):
        """ convert all words in glossary into list of objects """

        for g in self.glossary:
            self.word_list.append(Quiz_Word(g))

    def create_dict_of_questions(self):
        """ make questions, ensure they're unique """

        remaining_questions = 10
        
        if len(self.word_list) < 10:
            remaining_questions = len(self.word_list)

        while remaining_questions > 0:
            random.shuffle(self.word_list)
            # Make sure this word hasn't already been asked about
            if self.word_list[-1].entry not in self.dict_of_questions.keys():
                keyname = self.word_list[-1].entry
                question = Quiz_Question(self.word_list)
                question.populate_quiz_question()
                self.dict_of_questions[keyname] = question
                remaining_questions -= 1

    def create_mc_quiz(self):
        """ translate the question list into a multiple choice quiz """

        for key, value in self.dict_of_questions.items():
            if value.entry_to_translation == True:
                self.mc_quiz.append(f"What does '{value.quiz_question[0].entry}' mean in English?")
                for v in value.quiz_question:
                    self.mc_quiz.append(v.translation)
            else:
                self.mc_quiz.append(f"How is '{value.quiz_question[0].translation}' best translated?")
                for v in value.quiz_question:
                    self.mc_quiz.append(v.entry)

def print_quiz(glossary):
    quiz = Quiz(glossary)
    quiz.create_list_of_words()
    quiz.create_dict_of_questions()
    quiz.create_mc_quiz()
    print(quiz.mc_quiz)


if __name__ == '__main__':

    from sample_glossary import sample_glossary

    print_quiz(sample_glossary)
