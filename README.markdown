# OpenTCG: Trading Card API
## A simple way to simulate new and existing Trading Cards.

### Introduction
**OpenTCG** is a _purely_ `Python 3.10+` implementation of object-oriented programming aimed at being a simple API facilitating the creation and use of trading card objects for use in projects such as games, card creation/deck management apps, and more. \
In addition to the basic `open_tcg.Card` class, this API comes with an example using the popular **Yu-Gi-Oh** trading card game.

### How To Use
To use OpenTCG, import it into a Python module:
```python
import open_tcg
```
Alternatively, you can simply import the `Card` class:
```python
from open_tcg import Card
```
Now you have access to the functionality of Python objects.

#### Custom Card Types
To create a custom card type, define it as a sub-class of `Card`:
```python
class CustomCard(Card):
    """Custom card class.
    """
    def __init__(self, _name, _image):
        """The constructor for this sub-class.
        """
        # This runs the code in the constructor of open_tcg.Card
        super().__init__(_name, _image)
        #* You can run additional constructor logic on the line below.

```

#### Adding Card Attributes
To add card attributes, one option is to use dot notation to add them to individual instances:
```python
example_card = CustomCard(<name_string>, <image_path>)
example_card.description = ''
```
If you want every instance of your sub-class to initialize with this attribute, adjust your constructor logic in `CustomCard.__init__`:
```python
class CustomCard(Card):
    """Custom card class.
    """
    def __init__(self, _name, _image, _description):
        """The constructor for this sub-class.
        """
        # This runs the code in the constructor of open_tcg.Card
        super().__init__(_name, _image)
        #* You can run additional constructor logic on the line below.
        self.description = _description
```
