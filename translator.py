from googletrans import Translator


class TranslatorToUk:
    """
    class translate russian text to ukraine
     params: max len = 5000 if not cutting to 5000
    """

    def __init__(self, text):
        self.text = text
        self.translator = Translator()

    @property
    def check_len(self):
        if self.text.__len__() > 5000:
            return self.text[:5000]
        return self.text

    def translete(self) -> str:
        return self.translator.translate(self.check_len, src='ru',
                                         dest='uk').text
