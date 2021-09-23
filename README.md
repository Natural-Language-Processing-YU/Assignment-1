Natural Language Processing

Assignment \#1

| Due Date   | Week 5, October 7th, 2022                             |
|------------|-------------------------------------------------------|
| Submission | Individual Submission, Upload your scripts to Canvas  |
| Points     | 200                                                   |

Contents

[](#_Toc83238495)

[](#_Toc83238496)

[](#_Toc83238497)

[](#_Toc83238498)

# Overview

Much of this class relies on the  [D. and Martin J.
(2020)](https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf) text as
well as the [Natural Language Toolkit](https://www.nltk.org/book/) Python
library and text, so it is highly recommended that you read the prescribed
chapters for each assignment and use that as the basis for the exercises.

The first section of the class focuses on computational linguistics, text
processing, basic language models. Before we start "digging deep" into the
neural network processes for NLP -- the most efficient and now commonly used
portion of NLP -- we will learn the predecessor algorithms and approaches to
NLP. Often, you will find that it is important to understand how text is
processed and managed to be fed into algorithms that would have rules to provide
some categorization or classification of the output, assist in document
similarity and searching, facilitate the translation of information, or even
extract information from a corpus.

Thus, most of the body of educational resources with NLP will start with
teaching basic text processing such as regular expressions, stemming and
lemmatizing words, stop words, and tokenization within a corpus. Subsequently,
shallow learning techniques where language modeling is at the fore uses
statistical and tribalistic approaches such as logistic regression, naive Bayes,
and vectorization of words to support models like Continuous Bag of Words
(CBOW), N-grams, GloVe, among other approaches. These are critical techniques
for supporting some of the use cases for NLP mentioned above. As availability of
data became more widely available, and computer processing power both enhanced
technological while simultaneously becoming much less expensive in terms of
availability.

This assignment is an individual assignment in which you will focus primarily on
pre-processing of data and shallow learning techniques.

# Part I: Text Processing and Edit Distance (25 points)

#### Instructions 

-   Read the following [Chapter 2 – Regular Expressions, Text Normalizations,
    Edit Distance](https://web.stanford.edu/~jurafsky/slp3/2.pdf) Speech and
    Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2021.
    All rights reserved. Draft of September 21, 2021. **I have tried to pull out
    relevant notes for you below, but it is encouraged that you read each
    chapter provided.**

-   Complete the Part 1 coding exercise in the Jupyter Notebook under
    ./scripts/Part I/

#### Summary

One of the most relevant components to computer science as it pertains to NLP is
regular expressions. A **regular expression **is a computer language for
specifying text search strings. [1] In your reading, you will find that regular
expressions can be applied to text to extract information – one of the most
common tasks of NLP.

With NLP, part of the complexity is processing or normalizing the corpus or
corpora of words so that they can be analyzed. The basis of **text normalization
**as it pertains to NLP will often include three basic tasks: 1) tokenizing
words; 2) normalizing their formats; and 3) segmenting sentences.

Word tokenization is the task of segmenting running text into discrete words.
See *Figure 1* below in NLTK in which the sentence ‘That U.S.A. poster-print
costs \$12.40…’ can use regex to tokenize the sentence. [1]

![Text Description automatically generated](media/a5e482aec72a5274e7eecc3c9014188b.png)

Figure 1. NLTK Example of Word Tokenization

**Word normalization** is the task of putting words or tokens in an agreeable
structure. Often a choice is made with the word usage and formats for multiple
words. For example, “U.S.A.” could be expressed in several forms such as “USA”,
“US”, “United States”, “United States of America” and so on. [1]

Some types of word normalization tasks include, **case folding, **or
representing all the words in a single case, upper or lower (e.g., “United
States” vs “united states”); lemmatization or understanding whether two words
have the same semantic meaning despite their syntactical difference. For
example, the words “am” and “are*”* have the same lemma as their root meaning is
the same. One basic approach to acquiring the lemma of words, is to **stem
**words to ascertain their fundamental meaning. **Porter Stemmer  **[2]** **is
the most common algorithm for stemming and it involves removing the suffix of a
word to produce their same meaning. For example, “spitting” would be reduced to
“spit”. [1]

Finally, one major task in NLP is to identify the similarity of two words. The
most basic approach to this has been identified as a category of algorithms
called **edit distance **algorithms. The most common edit distance algorithm is
the **Levensthein Distance **algorithm, where a numerical output can be
calculated based on a comparison of the similarity of two words. What do you
think the Levensthein Distance for the words *sitting *and *kitten* would be?
See Figure 2 below. [3]

![](media/b98028f237d9d3f773c70bbdd1122dd1.png)

Figure 2. Levensthein Distance Example -- Sitting and Kitten

Note that every positional difference between the two words results in an
increment to the total distance. Thus, the edit distance between *sitting *and
*kitten* is 3. [4] Mathematically, it can be represented like the following in
Figure 3.

![Diagram, schematic Description automatically generated](media/26b7cbacc4c17264f8d2e65de0b489ad.png)

Figure 3. Levensthein Distance Algorithm

# Part II: N-gram language models (75 points) 

#### Instructions 

-   Read the following [uage
    Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf) Speech and Language
    Processing. Daniel Jurafsky & James H. Martin. Copyright © 2021. All rights
    reserved. Draft of September 21, 2021. **I have tried to pull out relevant
    notes for you below, but it is encouraged that you read each chapter
    provided.**

-   Complete the Part 2 coding exercise in the Jupyter Notebook ./scripts/Part
    II/

#### Summary [1]

Universal grammar is the idea that humans are genetically pre-disposed to a set
of fundamental structural rules that intuit language. Relatedly, I find the
probability-based nature of n-grams language modeling to be an intuitive appeal
to universal grammar. An **n-gram **is a language model in which a probability
is assigned to sequences of words. A **bi-gram** is a sequence of two words in a
corpus, and a **tri-gram ** is a series of three words in a corpus, and so on.
Here is an example of a sentence split into bi-grams:

-   Sentence: *The sky is blue today.*

    -   Bi-gram output: “*The sky”, “sky is, is blue”, “blue today.”*

Thus, *n* words make up the sequence to evaluate and the probability is
determined by the probability of a subsequent word to appear, given a history of
words. This is represented by:

Using a corpus of words, we can use the history to represent the probability of
say the word “blue” to follow the sequence “The sky is”. Represented by:

We can approximate to the probability of the next word in a sequence (i.e.,
P(w1, w2, ….,wn) by using the **conditional probability of the preceding word
using the Markov assumption. **

Finally, we can take the observed frequency of a sequence and divide this by the
observed frequency of the prefix you provide – the relative frequency. We are
comparing the raw probability of a word in a corpus and maximizing the
likelihood that it would appear given *contextual probability or history of a
sequence. *From here, we can train an n-gram language model using the
probability derived from a test corpus. An example of a test corpus is the Brown
Corpus (Brown University Standard Corpus of Present-day American English).
Compiled by W.N. Francis and H. Kucera, it was a first in terms of
machine-readable corpora. [5]

As the probabilities of an n-gram are calculated, you will note that when a new
sequence of words will inevitably in your test corpus or your application of
your language model that did not appear in your training corpus. We do not want
to assign a probability of zero to this novel sequence because that would not be
true in reality! So we implement a modification to the probabilistic approach
called **smoothing or discounting. **The simplest application is Laplacian
smoothing where we essentially add “1” to each probability – counts of 0 become
1, counts of 1 become 2.

![](media/1e78a5616502e9c18542d26c4f69395c.png)

Figure 4. Laplace Smoothing

# Part III: Naïve Bayes and Sentiment Classification and Logistic Regression (100 points)

#### Instructions 

-   Read the following [aive Bayes and Sentiment
    Classification](https://web.stanford.edu/~jurafsky/slp3/4.pdf). Speech and
    Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2021.
    All rights reserved. Draft of September 21, 2021. I have tried to pull out
    relevant notes for you below, but it is encouraged that you read each
    chapter provided.

-   Read the following [Chapter 5: Logistic
    Regression](https://web.stanford.edu/~jurafsky/slp3/5.pdf). Speech and
    Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2021.
    All rights reserved. Draft of September 21, 2021. I have tried to pull out
    relevant notes for you below, but it is encouraged that you read each
    chapter provided.

-   Complete the Part 3 coding exercise in the Jupyter Notebook here
    ./scripts/Part III/

## Submitting your assignment

As part of your submission, please upload 3 Jupyter Notebooks with your name
included in the saved filename to the Canvas assignment for this class.
