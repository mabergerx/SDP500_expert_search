# ==========================================================================

# These functions are used for the actual text pre-processing pipeline.
#
# (c) Mark Berger

# ==========================================================================

import spacy
import re

from Utility.data_cleaning import has_links, check_for_mostly_numeric_string, CUSTOM_STOPS

nlp = spacy.load("en_core_web_lg")

def create_text_pipeline(documents):
    """
    Create the full text pre-processing pipeline using spaCy that first cleans the texts
    using the cleaning utility functions and then also removes common stopwords and corpus
    specific stopwords. This function is used specifically on abstracts.
    
    :param documents: A list of textual documents to pre-process.
    
    :return cleaned_docs: Pre-processed textual documents.
    """
    # Load all the documents into a spaCy pipe.
    docs = nlp.pipe(documents, disable=["ner"])
    cleaned_docs = []

    # Lowercase + custom stopwords list + remove one character tokens + remove symbolical and punctuation tokens.
    for doc in docs:
        lowercased_sents_without_stops = []
        for sent in doc.sents:
            lowercased_lemmas_one_sent = []
            for token in sent:
                if not token.pos_ in {"SYM", "PUNCT"} \
                        and len(token) > 1 \
                        and not has_links(token.lower_) \
                        and not check_for_mostly_numeric_string(token.lower_) \
                        and not re.sub(r'[^\w\s]', '', token.lemma_) in CUSTOM_STOPS:
                    lowercased_lemmas_one_sent.append(token.lower_)

            sentence = ' '.join(lowercased_lemmas_one_sent)

            lowercased_sents_without_stops.append(sentence)

        cleaned_docs.append([s for s in lowercased_sents_without_stops])

    return cleaned_docs


def create_text_pipeline_titles(documents):
    """
    Create the full text pre-processing pipeline using spaCy that first cleans the texts
    using the cleaning utility functions and then also removes common stopwords and corpus
    specific stopwords. This function is used specifically on titles.
    
    :param documents: A list of textual documents to pre-process.
    
    :return cleaned_docs: Pre-processed textual documents.
    """
    titles = nlp.pipe(documents, disable=["ner", "parser"])
    cleaned_docs = []
    for doc in titles:
        lowercased_sents_without_stops = []
        for token in doc:
            if not token.pos_ in {"SYM", "PUNCT"} \
                    and len(token) > 1 \
                    and not has_links(token.lower_) \
                    and not check_for_mostly_numeric_string(token.lower_) \
                    and not re.sub(r'[^\w\s]', '', token.lemma_) in CUSTOM_STOPS:
                lowercased_sents_without_stops.append(token.lower_)

        sentence = ' '.join(lowercased_sents_without_stops)

        cleaned_docs.append(sentence)

    return cleaned_docs
