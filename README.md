# Mini Google Search

A notebook-based search engine for a local collection of UTF-8 text documents. It implements an inverted index, term-frequency search, AND/OR queries, edit-distance spelling suggestions and cosine-similarity document ranking using Python's standard library. The optional Gradio interface exposes those operations in tabs.

## Try the included corpus

Python 3.11+:

```sh
python -m venv .venv
# Activate .venv before installing.
python -m pip install -r requirements.txt
# Optional browser UI:
python -m pip install -r requirements-ui.txt
jupyter lab Mini_Google.ipynb
```

Run cells in order. Two short original sample documents are included in `examples/documents/`. To use your own corpus, set `SEARCH_CORPUS` to a directory of `.txt` files before launching Jupyter. In Colab, mount Drive manually and set the same variable. Directories and non-text files are skipped. The UI launches locally with sharing disabled by default; queries and filenames are HTML-escaped before display.

For example, after building `inverted_index`, run `multi_word_search("computer vision", inverted_index, mode="AND")`; the sample corpus returns `engineering.txt`. Scores count token occurrences; cosine ranking uses bag-of-words vectors. Equal scores use filename ordering for repeatable results, and repeated query terms do not inflate AND/OR scores.

## Checks and boundaries

```sh
python -m pip install pytest
python -m pytest -q
```

Tests exercise the notebook's actual index, Boolean retrieval, deterministic ranking, spelling distance and zero-vector behavior without launching a server. The tokenizer handles English letters and digits with a small stopword list; it has no stemming, TF-IDF weighting, crawler or semantic model. The historical personal corpus is not bundled. Saved notebook outputs may refer to that older corpus.
