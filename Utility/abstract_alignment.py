# ============================================================================

# These are utility functions used to align textual and embedding data
# following some external data/embedding calculations.
#
# (c) Mark Berger

# ============================================================================

def create_alignment(df):
    """
    Map the sentence position indexes of the abstract sentences for a whole
    papers dataframe. Used later to map the separately calculated sentence 
    embeddings (due to performance gains in SBERT batch embedding) to 
    the correct paper.
    
    :param df: The papers dataframe.
    
    :return alignment: The sentence-to-position alignment dictionary.
    """
    alignment = {}
    current_start = 0
    current_end = 0
    for index, row in df.iterrows():
        abstract = row.abstract_sentences
        current_end += len(abstract)
        alignment[index] = {"start": current_start, "end": current_end}
        current_start = current_end
    return alignment


def reconstruct_batches(alignment, abstract_sentence_embeddings):
    """
    Given the sentence-to-position alignment file and the abstract sentence 
    embeddings batch calculated separately, restores the abstract-to-embeddings
    mapping.
    
    :param alignment: The sentence-to-position alignment file.
    :param abstract_sentence_embedding: The abstract sentence embeddings 
    batch calculated separately
    
    :return reconstructed_batches: Batches of sentence embeddings, where each batch corresponds 
    to a single abstract.
    """
    reconstructed_batches = []
    for k, v in alignment.items():
        start = v["start"]
        end = v["end"]
        one_batch = []
        for i in range(start, end):
            one_batch.append(abstract_sentence_embeddings[i])
        reconstructed_batches.append(one_batch)

    return reconstructed_batches
