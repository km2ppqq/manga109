# manga109

**Type-based API client for [Manga109](http://www.manga109.org)**

## Installation

- `Python 3.7+`

```sh
pip install git+https://github.com/km2/manga109.git
```

## Usage

### Basic Usage

#### Initialize

```python
from manga109 import Manga109

client = Manga109("path/to/manga109")

# specific titles
client = Manga109("path/to/manga109", titles=["ARMS", "GakuenNoise", "PrayerHaNemurenai"])
```

#### Access any information

```python
print(client.books[0].title)  # ARMS
print(client.books[0].characters[14].name)  # タイロン
print(client.books[0].pages[80].texts[5].text)  # 返事して
```

#### Get the path to the image

```python
print(client.books[0].pages[17].image_path)  # path/to/manga109/images/ARMS/017.jpg
```

### Advanced Usage

#### Get the number of characters per title

```python
print([{b.title: len(b.characters)} for b in client.books])
# [{'ARMS': 23}, {'AisazuNihaIrarenai': 17}, {'AkkeraKanjinchou': 16}, ...]
```

#### Get a list of texts per page with one or more texts

```python
print([[t.text for t in p.texts] for p in client.books[0].pages if p.texts])
# [['あ'], ['キャーッ', 'はやく逃げないとまきぞえくっちゃう', ...], ...]
```
