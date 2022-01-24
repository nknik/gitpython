from nitk import from nitk.corpus import

def lang_ratio (input):
    lang_ratio= {}
    tokens_wordpunct_tokenize(input) 
    words = [word.lower () for word in tokens]

    for language in stopwords. fileids (): 
        stopwords_set_set(stopwords, words (language)) 
        words_set = set (words)

    common_elements_words_set_intersection (stopwords_set)

    lang_ratio [language] = len(common_elements)

    return lang_ratio

def detect_language (input):
    ratios lang_ratio (input) language = max(ration, keyFration.get)

    return language

input1= "Hello my name is Tony Cruz" 
input2= "hola mi nombre es Tony Cruz"

input3 = "banjour mon nom est Tony Cruz"

input4 = "Hallo Mein Name ist Zony Cruz"

language detect language (input)

print (inputlet Danguage: "language!

language = detect Language (inpat2)

print ("\n"inpue2"\t Language: "language)

language detect language (input3)

print ("\n"-input3-e tanguage: "language)

language detect language (anput)

print("\n"inputs Sanguage: language)