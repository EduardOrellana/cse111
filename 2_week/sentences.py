import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:

        words = ["a", "one", "the"]
    else:

        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:

        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    else:

        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)

    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":

        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    elif quantity == 1 and tense == "present":
    
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    
    elif quantity != 1 and tense == "present":
    
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    elif tense == "future":
    
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word = random.choice(words)

    return word

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    #Develope the sentence

    determiner = get_determiner(quantity)

    noun = get_noun(quantity)

    verb = get_verb(quantity, tense)

    preposition = get_prepositional_phrase(quantity)

    adjective = get_adjective()

    adverb = get_adverb()

    sentence = f'{determiner.capitalize()} {adjective} {noun} {preposition} {verb} {adverb}'

    return sentence

def main():
    quantity_list = [1, 1, 1, 2, 2,2]
    verbe_tense = ["past", "present", "future", "past", "present", "future"]

    for i in range(len(quantity_list)):
        quantify = quantity_list[i]
        verb = verbe_tense[i]

        sentence_to_print = make_sentence(quantify, verb)
        preposition_to_print = get_prepositional_phrase(quantify)
        print(f"\n\n{i + 1}\n")
        print(f'         {sentence_to_print} {preposition_to_print}')

def get_preposition ():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions_list = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "into", "out", "over", "past", "to", "under", "with", "without"]

    word = random.choice(prepositions_list)
    return word 


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
    quantity: an integer that determines if the
    determiner and noun in the prepositional
    phrase returned from this function should
    be single or pluaral.
    Return: a prepositional phrase.
    """
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}"

    return prepositional_phrase

def get_adjective():
    """
    Return a Radomly chosen adjective from
    this lst of adjective:
    'Fast','Clear','Easy','Smart','Smooth','Neat',
    'Lightweight','Fun','Quick','Friendly','Agile',
    'Handy','Simple','Cool','Clever','Sleek','Nice','Joyful','Pleasant','Solid'
    
    Return a radomly chosen adjective
    """
    adjective_list = ["fast", "clear", "easy", "smart", "smooth", "neat", "lightweight", "fun", "quick", "friendly", "agile", "handy", "simple", "cool", "clever", "sleek", "nice", "joyful", "pleasant", "solid"]

    word = random.choice(adjective_list)
    return word

def get_adverb ():
    """
    Will return a randomly adber from this list:
    "quickly", "smoothly", "easily", "quietly", "happily"
    """

    adverb_list = ["quickly", "smoothly", "easily", "quietly", "happily"]

    word = random.choice(adverb_list)

    return word

main()
print("\n\n\nCredits Erick Orellana\n\n\n")