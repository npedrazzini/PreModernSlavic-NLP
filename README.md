# PreModernSlavic-NLP
Mixed drafts, scripts or data useful for NLP tasks on Pre-Modern Slavic.

## stopwords.py
Working draft containing potential PMSl stop words. These were automatically extracted from the TOROT Treebank ((Old) Church Slavonic, Old East Slavic, and Middle Russian corpus) and include: 
- All forms of _byti_ attested in the corpus.
- All attested forms of specific parts of speech.

<img src="https://github.com/npedrazzini/PreModernSlavic-NLP/blob/images/POS_PROIEL.png" alt="drawing" width="600"/>

The extracted parts of speech is indicated before each group of stop words, and the classification and abbreviations follow the PROIEL convention (see Figure taken from [[1]](#1)). The list so far includes: 

- conjunctions
- relative adverbs
- interrogative adverbs
- subjunctions
- interjections
- cardinal numerals
- demonstrative pronouns
- interrogative pronouns
- personal reflexive pronouns
- personal pronouns
- possessive pronouns
- indefinite pronouns
- prepositions

The list is formatted following spaCy's convention, but it's divided by PoS (which is normally not the case there). If you prefer working with different formats, see §stopwords.csv and §extractstopwords.py.

## stopwords.csv
This contains the raw data extracted from TOROT, divided by columns (lemma_id, pos, form, lemma). Disregard lemma_id for the purpose of extracting stop words (that is just for easier retrieval of a particular lemma in TOROT).

## extractstopwords.py
This is the script used to generate _stopwords.py_. It extracts unique forms attested for each part of speech and organizes them as seen in _stopwords.py_. Change line 3 with the relevant path to stopwords.csv to reproduce.

## References
<a id="1">[1]</a> 
Eckhoff, Hanne & Bech, Kristin & Bouma, Gerlof & Eide, Kristine & Haug, Dag & Haugen, Odd & Jøhndal, Marius. (2018). The PROIEL treebank family: a standard for early attestations of Indo-European languages. _Language Resources and Evaluation_. 52. DOI:10.1007/s10579-017-9388-5. 
