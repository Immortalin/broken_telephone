# Broken Telephone (WIP)

This is a simulation for exploring the effects of noise on neural network communication models and to visualise the effects of noisy channels on text. 

- install [Poetry](https://python-poetry.org/) and download the appropriate version of [PyTorch](https://pytorch.org/get-started/locally/)
```
poetry install 
poetry shell
streamlit main.py
```

## Attributions and Citations


### CommPy et al.
```
V. Taranalli, B. Trotobas, and contributors, “CommPy: Digital Communication with Python”. [Online]. Available: github.com/veeresht/CommPy
```
[veeresht/CommPy](https://github.com/veeresht/CommPy)

### Hugging Face et al.
```bibtex
@inproceedings{wolf-etal-2020-transformers,
    title = "Transformers: State-of-the-Art Natural Language Processing",
    author = "Thomas Wolf and Lysandre Debut and Victor Sanh and Julien Chaumond and Clement Delangue and Anthony Moi and Pierric Cistac and Tim Rault and Rémi Louf and Morgan Funtowicz and Joe Davison and Sam Shleifer and Patrick von Platen and Clara Ma and Yacine Jernite and Julien Plu and Canwen Xu and Teven Le Scao and Sylvain Gugger and Mariama Drame and Quentin Lhoest and Alexander M. Rush",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = oct,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-demos.6",
    pages = "38--45"
}
```