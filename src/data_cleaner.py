from abc import ABC, abstractmethod

class BaseImputer(ABC):
    @abstractmethod
    def impute():
        pass

class MeanImputer(BaseImputer):
    def impute():
        pass

class MedianImputer(BaseImputer):
    def impute():
        pass

class KNNImputer(BaseImputer):
    def impute():
        pass

class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle():
        pass

class IQROutlierHandler(BaseOutlierHandler):
    def handle():
        pass

class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle():
        pass
