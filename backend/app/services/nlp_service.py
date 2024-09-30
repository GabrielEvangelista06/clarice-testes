import spacy
from functools import lru_cache
from typing import List, Dict, Union, Tuple

@lru_cache()
def get_nlp_model():
    """
    Load the spaCy model with caching.

    This function loads the spaCy model 'pt_core_news_lg' and caches it to avoid reloading it multiple times.
    
    Returns:
        spacy.language.Language: The loaded spaCy model.
    """
    return spacy.load("pt_core_news_lg")

async def process_text(text: str) -> Tuple[List[Dict[str, Union[str, int]]], List[Dict[str, Union[str, int]]]]:
    """
    Process the text and extract entities and multi-word expressions (MWEs).

    Args:
        text (str): The input text to be processed.

    Returns:
        Tuple[List[Dict[str, Union[str, int]]], List[Dict[str, Union[str, int]]]]: A tuple containing a list of extracted entities and a list of extracted MWEs.
    """
    nlp = get_nlp_model()
    doc = nlp(text)
    entities = extract_entities(doc)
    mwes = extract_mwes(doc)

    return entities, mwes

def extract_entities(doc: spacy.tokens.Doc) -> List[Dict[str, Union[str, int]]]:
    """
    Extract entities from the processed text.

    Args:
        doc (spacy.tokens.Doc): The processed spaCy document.

    Returns:
        List[Dict[str, Union[str, int]]]: A list of dictionaries containing the extracted entities.
    """
    return [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        for ent in doc.ents
    ]

def extract_mwes(doc: spacy.tokens.Doc) -> List[Dict[str, Union[str, int]]]:
    """
    Extract multi-word expressions (MWEs) from the processed text.

    Args:
        doc (spacy.tokens.Doc): The processed spaCy document.

    Returns:
        List[Dict[str, Union[str, int]]]: A list of dictionaries containing the extracted MWEs.
    """
    unique_mwes = set()

    for chunk in doc.noun_chunks:
        if len(chunk) > 1:
            unique_mwes.add((chunk.text, chunk.start_char, chunk.end_char))

    for ent in doc.ents:
        if len(ent) > 1:
            unique_mwes.add((ent.text, ent.start_char, ent.end_char))

    return [{"text": text, "start": start, "end": end} for text, start, end in unique_mwes]
