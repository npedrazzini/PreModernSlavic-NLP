# PreModernSlavic-NLP
Mixed drafts, scripts or data useful for NLP tasks on Pre-Modern Slavic.

## Part-of-Speech Tagging and Morphological Analysis

### Scherrer, Mocken & Rabus's *lstmtagger*
State of the art on generic pre-modern Slavic PoS tagging and morphological analysis as of Oct 2021 is still https://github.com/yvesscherrer/lstmtagger [[2]](#2).

### Baranov et al.'s (2007) Old Russian morphological analyzer
Morphological analyzer specifically for Old East Slavic (Old Russian): http://manuscripts.ru/mns/slov.poisk?p_lang=EN [[4]](#4).

### Berdicevskis et al.'s (2011) Middle Russian morphological analyzer
PoS tagger, lemmatizer and morphological analyzer specifically for Middle Russian: http://www.dialog-21.ru/media/3384/berdičevskisaetal.pdf [[6]](#6).

### Meyer (2011) Old Russian morphological analysis via modern-translation projection
Morphological analysis specifically for Old East Slavic (Old Russian), via annotation projection from Modern Russian: https://www.semanticscholar.org/paper/New-wine-in-old-wineskins—Tagging-Old-Russian-via-Meyer/10e0f26bc97bd054cd31546a90de1559f90b944f [[5]](#5)


## Dependency Parsing

### Pedrazzini & Eckhoff's *OldSlavNet*
State of the art on pre-modern Slavic dependency parsing as of Oct 2021 is still https://npedrazzini.github.io/OldSlavNet/. [[3]](#3)

## Stop Words

### extractstopwords.py
This is the script used to generate _stopwords.py_. It extracts unique forms attested for each part of speech and organizes them as seen in _stopwords.py_. Change line 3 with the relevant path to stopwords.csv to reproduce.

### stopwords.csv
This contains the raw data extracted from TOROT, divided by columns (lemma_id, pos, form, lemma). Disregard lemma_id for the purpose of extracting stop words (that is just for easier retrieval of a particular lemma in TOROT).

### stopwords.py
Working draft containing potential PMSl stop words. These were automatically extracted from the TOROT Treebank ((Old) Church Slavonic, Old East Slavic, and Middle Russian corpus) and include: 
- All forms of _byti_ attested in the corpus.
- All attested forms of specific parts of speech.

<img src="https://github.com/npedrazzini/PreModernSlavic-NLP/blob/main/POS_PROIEL.png" alt="drawing" width="600"/>

The extracted part of speech is indicated before each group of stop words, and the classification and abbreviations follow the PROIEL convention (see Figure taken from [[1]](#1)). The list so far includes: 

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

The list is formatted following spaCy's convention, but it's divided by PoS (which is normally not the case there). If you prefer working with different formats, see §[stopwords.csv](https://github.com/npedrazzini/PreModernSlavic-NLP#stopwordscsv) and §[extractstopwords.py](https://github.com/npedrazzini/PreModernSlavic-NLP#extractstopwordspy).

## Gold Standards
Gold standard for morphology and dependency tags for Old Church Slavonic/Later Church Slavonic, Old East Slavic, and Middle Russian can be downloaded from 

## References
<a id="1">[1]</a> Eckhoff, H., Bech, K., Bouma, G. & Eide, K., Haug, D., Haugen, O. & Jøhndal, M. 2018. The PROIEL treebank family: a standard for early attestations of Indo-European languages. _Language Resources and Evaluation_. 52. DOI:10.1007/s10579-017-9388-5. 

<a id="2">[2]</a> Scherrer, Y., Mocken, S. & Rabus, A. 2018. New developments in tagging pre-modern orthodox Slavic texts. *Scripta & e-Scripta* 18.

<a id="3">[3]</a> Pedrazzini, N. & Eckhoff H. 2021. OldSlavNet: A scalable Early Slavic dependency parser trained on modern language data. *Software Impacts* 100063.

<a id="4">[4]</a> Baranov, V., Mironov, A., Lapin, A., Mel’nikova. I., Sokolova. A. & Korepanova, E. 2007. Avtomatičeskij morfologičeskij analizator drevnerusskogo jazyka: lingvističeskie i technologičeskie rešenija. In *10-ja jubilejnaja meždunarodnaja konferencija “EVA 2007 Moskva”*.

<a id="5">[5]</a> Meyer, R. 2011. New wine in old wineskins? Tagging Old Russian via annotation projection from modern translations. *Russian Linguistics* 35/2. 267–281.

<a id="6">[6]</a> Berdičevskis, A., Eckhoff, H. & Gavrilova, T. 2011. The beginning of a beautiful friendship: rule-based and statistical analysis of Middle Russian. In *Computational Linguistics and Intellectual Technologies. Proceedings of Dialogue* 16. 99–111.