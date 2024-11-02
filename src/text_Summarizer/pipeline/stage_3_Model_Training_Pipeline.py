from src.text_Summarizer.components.model_trainer import ModelTrainer
from src.text_Summarizer.config.configuration import ConfigurationManager_Training

class Train_Model():
    def __init__ (self):
        pass
    def initiate_model_Trainer(self):
        config = ConfigurationManager_Training()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()