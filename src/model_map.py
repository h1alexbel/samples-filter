class ModelMap:

    def build(self):
        map = {}
        from src.rf_model import RfModel
        from src.transformer_model import TransformerModel
        map["rf"] = RfModel
        map["transformer"] = TransformerModel
        return map
