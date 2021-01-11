# create_kahoot

## Overview:

Create_Kahoot will produce an excel file that can be uploaded
to Kahoot.

Each question will randomly ask for definitions of a target language
word or provide a definition and as for the proper target language word.

Each question will have four possible answers, the first of which
is always the correct answer.

## Usage:

`create_kahoot(glossary)`

Where glossary is a list of tuples containing two items, the first
of which is presumed to be the target structure and the second of
which is the translation

It produces `kahoot_quiz.xlsx`
