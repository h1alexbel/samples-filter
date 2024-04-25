class TextOut:
    def __init__(self, pred):
        self.pred = pred

    def as_text(self):
        if self.pred[0]["label"] == "POSITIVE":
            label = "sample"
        else:
            label = "real"
        return label
