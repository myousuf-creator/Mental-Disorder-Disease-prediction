#from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from skmultilearn.problem_transform import ClassifierChain
from sklearn.tree import DecisionTreeClassifier

# from classification_model.processing import preprocessors as pp
# #from classification_model.processing import features
# from classification_model.config import config


import preprocessors as pp
import config

import logging

classification_pipe = Pipeline(
    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS_WITH_NA)),
         
        ('numerical_inputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA)),
         
        # ('temporal_variable',
        #     pp.TemporalVariableEstimator(
        #         variables=config.TEMPORAL_VARS,
        #         reference_variable=config.DROP_FEATURES)),
         
        # ('rare_label_encoder',
        #     pp.RareLabelCategoricalEncoder(
        #         tol=0.01,
        #         variables=config.CATEGORICAL_VARS)),
         
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
         
        # ('log_transformer',
        #     pp.LogTransformer(variables=config.NUMERICALS_LOG_VARS)),
         
        ('drop_features',
            pp.DropUnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),
         
        #('scaler', MinMaxScaler()),
        ('decision_trees', ClassifierChain(DecisionTreeClassifier()))
    ]
)
