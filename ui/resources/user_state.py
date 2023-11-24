
import streamlit as st


class UserState():
    """
    """
    
    def __init__(self):
        """
        """
        
        # global filter
        self.ft_states = []
        
        # train model parameters
        self.train_cohorts = ("2022-01","2022-12")
        self.test_cohorts = ["2023-01","2023-02","2023-03","2023-04",]
        self.features_set = ["Ume",]
        self.target = 0
        self.tag_model = "default"
        self.save = False
        
        # ...
        self.scores_folder = None
        