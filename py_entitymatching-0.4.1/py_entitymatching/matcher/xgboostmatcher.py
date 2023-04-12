from py_entitymatching.matcher.mlmatcher import MLMatcher
from py_entitymatching.matcher.matcherutils import get_ts
# from sklearn.svm import SVC
try:
    from xgboost.sklearn import XGBClassifier
except ImportError:
    raise ImportError('Check if xgboost library is installed. You can install xgboost '
                      'by following the instructions at http://xgboost.readthedocs.io/en/latest/build.html')


class XGBoostMatcher(MLMatcher):
    """
    XGBoost matcher.

    Args:
        *args,**kwargs: The arguments to XGBoost
            classifier.
        name (string): The name of this matcher (defaults to None). If the
             matcher name is None, the class automatically generates a string
             and assigns it as the name.


    """
    def __init__(self, *args, **kwargs):
        super(XGBoostMatcher, self).__init__()
        # If the name is given, then pop it
        name = kwargs.pop('name', None)
        if name is None:
            # If the name of the matcher is give, then create one.
            # Currently, we use a constant string + a random number.
            self.name = 'xgboost'+ '_' + get_ts()
        else:
            # Set the name of the matcher, with the given name.
            self.name = name
        # Set the classifier to the scikit-learn classifier.
        try:
            from xgboost.sklearn import XGBClassifier
        except ImportError:
            raise ImportError(
                'Check if xgboost library is installed. You can install xgboost '
                'by following the instructions at http://xgboost.readthedocs.io/en/latest/build.html')
        self.clf = XGBClassifier(*args, **kwargs)

