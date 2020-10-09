  
# =============================================================================

# These utility functions are used for the cleaning part of text pre-processing.
#
# (c) Mark Berger

# =============================================================================

import re
import unidecode

CUSTOM_STOPS = {"abstract", "background", "background.", "abstract.", "method",
                "result", "conclusion", "conclusions", "discussion", "PRON", "registration", "url"}


def remove_whitespace_chars(text):
    """
    Remove unnecessary (trailing, double, etc.) whitespace characters from a piece of text.
    
    :param text: A piece of text.
    
    :return Text without unnecessary whitespace.
    """
    return " ".join(text.split())


def clean_sentence(sentence):
    """
    Remove unreadable Unicode characters and non-alpha characters from the text.
    
    :param sentence: Sentence to clean.
    
    :return text: Cleaned sentence.
    """
    text = re.sub(r'[^a-zA-Z\']', ' ', sentence)

    # remove Unicode characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    return text


def has_links(token):
    """
    Check whether the token is an URL's or an e-mail address.
    
    :param token: A single text token.
    
    :return A boolean indicating whether the token is an URL's or an e-mail address.
    """
    if any(substring in token for substring in {"link_type", "ref?", "=%", "html", "http", "www", ".com", "access_num"}):
        return True
    else:
        return False


def check_for_mostly_numeric_string(token):
    """
    Check whether the token is numerical.
    
    :param token: A single text token.
    
    :return A boolean indicating whether the token is a numerical.
    """
    int_chars = []
    alpha_chars = []

    for ch in token:
        if ch.isnumeric():
            int_chars.append(ch)
        elif ch.isalpha():
            alpha_chars.append(ch)

    if len(int_chars) > len(alpha_chars):
        return True
    else:
        return False


# We use unidecode to remove accent characters and generally convert chars to their ASCII variant. Although that is not always good in small
# amounts of text or where precision is crucial, I believe that for text similarity tasks this is generally an improvement.
def unidecode_and_no_ws(texts, placeholder="None-placeholder"):
    """
    Remove unnecessary whitespace and decode the chars to their readable variant if possible.
    
    :param texts: A collection of texts.
    
    :return Cleaned texts.
    """
    return [remove_whitespace_chars(unidecode.unidecode(a)) for a in texts if a != placeholder]
