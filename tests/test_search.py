import math
import re
from collections import Counter, defaultdict
import pytest
from notebook_helpers import definitions

f=definitions("Mini_Google.ipynb", {"re":re,"math":math,"Counter":Counter,"defaultdict":defaultdict})

def test_boolean_search_and_repeat_tokens():
    idx=f["build_inverted_index"]({"b.txt":"vision camera", "a.txt":"vision vision", "c.txt":"camera"})
    assert f["search"]("VISION!",idx)==[("a.txt",2),("b.txt",1)]
    assert f["multi_word_search"]("vision camera",idx)==[("b.txt",1)]
    assert f["multi_word_search"]("vision vision",idx,"OR")==[("a.txt",2),("b.txt",1)]
    assert f["multi_word_search"]("absent vision",idx)==[]
    with pytest.raises(ValueError): f["multi_word_search"]("",idx,"INVALID")

def test_similarity_and_suggestions():
    assert f["cosine_similarity"](Counter(),Counter(vision=1))==0
    assert f["levenshtein"]("kitten","sitting")==3
    texts={"b.txt":"vision", "a.txt":"vision", "c.txt":"camera"}
    idx=f["build_inverted_index"](texts)
    ranked=f["rank_documents"]("vision",idx,f["build_doc_vectors"](texts))
    assert ranked==[("a.txt",1.),("b.txt",1.)]
