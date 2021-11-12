# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args
from jupyter_dash import JupyterDash
import dash_html_components as html

class Wordcloud(Component):
    """A Wordcloud component.


Keyword arguments:

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

- words (string; required):
    your column name of words columns in your dataset."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, filterString=Component.UNDEFINED, data=Component.REQUIRED, words=Component.REQUIRED, freqs=Component.REQUIRED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'filterString', 'freqs', 'height', 'value', 'width', 'words']
        self._type = 'Wordcloud'
        self._namespace = 'dwcm'

        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'filterString', 'freqs', 'height', 'value', 'width', 'words']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        self.args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['data', 'words', 'freqs']:
            if k not in self.args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Wordcloud, self).__init__(**self.args)
    def show(self):
        app = JupyterDash(__name__)
        app.layout = Wordcloud(**self.args)
        app.run_server(mode='inline')