## SemSketches
Our competition is an opportunity to work with a semantic sketch. Semantic sketches represent most frequent collocations of a word, sorted according to the semantic relations between the core word and its dependencies. The goal of the competition is to evaluate how representative and illustrative the sketches are by trying to find the necessary sketches in the given set using the context of a word without seeing the word itself.

### Results
[**dev.gold**](https://github.com/dialogue-evaluation/SemSketches/blob/main/data/dev/dev.gold) - mapping between 44750 sentences and 895 sketches  
[**manual_dev.gold**](https://github.com/dialogue-evaluation/SemSketches/blob/main/data/dev/manual_dev.gold) - manually selected subset of dev.gold, mapping between  4347 sentences and 100 sketches

|              |            |            |
| :---         |           ---: |          ---: |
|**team** |  **dev.gold**  |   **manual_dev.gold**   |
|paleksandrova |    0.309      |     0.277       |
|good501 |   0.104    |      0.127      |
| smpl|     0.182       |    0.121        |

### Important links
Contact the organizers and other participants via Telegram, do not hesitate to join the SemSketches chat https://t.me/SemSketches.  
SemSketches Codalab page [here](https://competitions.codalab.org/competitions/29992).

### Timeline
__!Deadline extended!__
|              |            |
| :---         |           ---: |
| Release of the Trial Data  | Feb 12th 2021  | 
| 1st Task Data release    | Feb 17th 2021  |
| 2nd Task Data release    | Mar 5th 2021  |
| **System submission due**    | ~~Mar 14th  2021~~ Mar 27th  2021|
| Final results announcement   | ~~Mar 16th 2021~~  Mar 29th  2021|
| Paper submission due   | ~~Mar 23rd 2021~~  Apr 5th  2021|

### What is a semantic sketch
In this competition, a semantic sketch is understood as a generalized lexicographic portrait of a word. In other words, it is a way of representing the compatibility of words, where the description of each word includes a set of its most frequent semantic dependencies classified according to their semantic roles (Agent, Object, Locative). For each role a number of relevant “fillers” (words and phrases) are given, and the fillers are ranked according to the frequency of their compatibility with the core. Each sketch here illustrates a word in a certain meaning.

### Data
The competition data consist of three parts:
* set of contexts for the most frequent predicates in Russian (Task 1)
* set of sketches, which illustrates these Russian predicates (Task 1, Task 2)
* set of sketches for the predicates with the same meanings in English (Task 2)

***Task 1: Matching a sketch to a predicate in context***
A set of contexts is given for different predicates. The selected predicate in the context has to be matched with one of the anonymized sketches (the roles and collocations are known for each of them, but the predicate itself is masked). In the case of ambiguous predicates, the WSD problem can be stated.


***Task 2: Multilingual sketch mapping***
Two sets of sketches are given in two languages for the same meanings. The task is to match the multilingual pairs of sketches, thereby performing cross-lingual sense linking. 
Solving the first problem can help solve the second, but it is not necessary.
The main metric in both tasks is accuracy.




### Organizers
Maria Ponomareva - ABBYY, HSE  
Maria Petrova - ABBYY  
Maria Yarova - MIPT  
Julia Detkova - ABBYY  
Oleg Serikov - DeepPavlov, HSE  
