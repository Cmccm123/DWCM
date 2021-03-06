
DWCM(D3 Word Cloud M)
=============

a word cloud of data visualization base on D3.js

Who are we?
=============

Hello everyone. I am Sunny. I graduated with an HD in Data Science and Analytics. My alma mater has a series of good practices in developing the practical application of dynamic data visualization/interactive dashboards. We are continuously concentrating on simplifying the data visualization process. Word cloud is one of our essential parts of data visualization in NLP. We found that the existing python package is challenging to complete an interactive word cloud dashboard. Therefore, the python package is based on D3.js/react.js/DASH, which can be executed in python or cooperate with Dash for word cloud development.

Keyword arguments:
=============

- id (string; optional):
   the unique identity of keyword in word cloud html DOM.

- data (list; required):
    dataset for word cloud visualising. datatype is array. on the array you need a
    words columns and the freq columns of each word.
    for example {'keyword': 10}.

- filterString (list; optional):
   the word cloud filtrate the selected keyword(s). you should not set/input this parameter.

- freqs (string; required):
    frequency or concurrency of each keyword

- height (string; optional):
    the height of the boundary of the word cloud.

- width (string; optional):
    the width of the boundary of the word cloud.

- value (string; optional):
    just for future may be to use.

Example
=============

.. code:: python

   import Dwcm
   data = [{'word': 'A', 'freq': 15},{'word': 'B', 'freq': 22}],
   Dwcm.Wordcloud(data = data,words = 'word',freqs = 'freq').show()
