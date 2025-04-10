import random
import copy

nouns = ["badger", "horse", "aardvark", "mouse", "gorrila", "elephant", "eagle", "sparrow"]
verbs = ["hugs", "bounces", "meows", "whispers", "flutters", "gallops", "shimmers"]
adjectives = ["furry", "incredulous", "fragrant", "exuberant", "glistening", "melancholic", "serene"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "graciously", "reluctantly", "meticulously", "vigorously"]

words = (nouns, verbs, adjectives, prepositions, adverbs)

def make_poem(words):
    # Create a deep copy of the words tuple
    words = copy.deepcopy(words)
    # 3 Random Nouns
    nouns = []
    for _ in range(3):
        noun = random.choice(words[0])
        words[0].remove(noun)
        nouns.append(noun)

    # 3 Random Verbs
    verbs = []
    for _ in range(3):
        verb = random.choice(words[1])
        words[1].remove(verb)
        verbs.append(verb)

    # 3 Random Adjectives using list comprehension
    random.shuffle(words[2])
    adjectives = [words[2].pop() for _ in range(3)]
    
    # 2 Random Prepositions
    prepositions= random.sample(words[3], k=2)

    # 1 Random Adverb
    adverb = random.choice(words[4])

    # Decide whether to use A or An as the article
    if adjectives[0][0] in "aeiou":
        article = "An"
    else:
        article = "A"

    # Create the poem
    poem = (
        f"{article} {adjectives[0]} {nouns[0]}\n\n"
        f""
        f"{article} {adjectives[0]} {nouns[0]} "
        f"{verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}\n\n"
        f"{adverbs[0]}, the {nouns[0]} {verbs[1]}\n"
        f"the {nouns[1]} {verbs[2]} {prepositions[1]} the {adjectives[2]} {nouns[2]}"
        )
        
    return poem



print(make_poem(words))
