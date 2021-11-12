# DWCM
a word cloud of data visualization base on D3.js

# Who are we?

Hello everyone. I am Sunny. I graduated with an HD in Data Science and Analytics. My alma mater has a series of good practices in developing the practical application of dynamic data visualization/interactive dashboards. We are continuously concentrating on simplifying the data visualization process. Word cloud is one of our essential parts of data visualization in NLP. We found that the existing python package is challenging to complete an interactive word cloud dashboard. Therefore, the python package is based on D3.js/react.js/DASH, which can be executed in python or cooperate with Dash for word cloud development.

# Keyword arguments:

- id (string; optional):
    the id of word cloud in the html DOM.

- data (list; required):
    dataset of word cloud. datatype is array. on the array you need a
    words columns and the freq columns of each word.

- filterString (list; optional):
    the user clicked word list,use on dashboard for user to filter
    data. you should not set/input this parameter.

- freqs (string; required):
    your column name of freq columns in your dataset.

- height (string; optional):
    the height of word cloud.

- value (string; optional):
    just for future may be to use.

- width (string; optional):
    the width of word cloud.

