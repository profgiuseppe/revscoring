"""
.. autoclass:: revscoring.scoring.Statistics
    :members:
    :member-order:
"""
import logging

from ..model_info import ModelInfo

logger = logging.getLogger(__name__)


class Statistics(ModelInfo):

    def __init__(self):
        """
        Construct a set of Statistics.  Instances of this class work like a
        `dict` of statistical values once
        :func:`revscoring.scoring.Statistics.fit` is called.
        """
        super().__init__()
        self.fitted = False

    def fit(self, score_labels):
        """
        Fit to scores and labels.

        :Parameters:
            score_labels : [( `dict`, `mixed` )]
                A collection of scores-label pairs generated using
                :class:`revscoring.Model.score`.  Note that fitting is usually
                done using data withheld during model training
        """
        self.fitted = True

    def format_str(self, path_tree, **kwargs):
        raise NotImplementedError()

    def format_json(self, path_tree, **kwargs):
        raise NotImplementedError()
