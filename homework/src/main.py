
import argparse

from ._internals.file_reader import filereader
from ._internals.text_processor import TextProcessor 

class ArgumentParser:
    def __init__(self):

        self.input = None
        self.output = None
        self.parser= None
        
        self.crear_parser()

    def crear_parser(self):

        self.parser = argparse.ArgumentParser(description="Count words in files.")
        self.parser.add_argument(
            "input",
            type=str,
            help="Path to the input folder containing files to process",
        )
        self.parser.add_argument(
            "output",
            type=str,
            help="Path to the output folder for results",
        )

def run(self):

   
    parsed_args = self.parser.parse_args()
    self.input = parsed_args.input
    self.output = parsed_args.output

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def print(self):
        print("mi nombre es ", self.nombre, " ", self.apellido)

def main():

    argument_parser = ArgumentParser().run()

    file_reader = filereader(argument_parser.input)
    text_processor = TextProcessor()
    
    lines = file_reader.read_all_lines()
    preprocessed_lines = text_processor.preprocess_lines(lines)
    words = text_processor.split_into_words(preprocessed_lines)

class LinearRegression:
    def __init__(self, fit_intercept=True, positive=False):
        self.fit_intercept = fit_intercept
        self.positive = positive

    def fit(self, x, y):
        pass

    def predict(self, x):
        pass

class MLPClassifier:
    def __init__(self, hidden_layer_sizes = (100,1), learning_rate='constant'):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.learning = self.learning_rate

    def fit(self, x, y):
        pass

modelo_a = LinearRegression(..., positive=False)
modelo_b = LinearRegression(...,positive=True)
modelo_c = MLPClassifier(hidden_layer_sizes=(10,1))
modelo_d = MLPClassifier(hidden_layer_sizes=(20,1))
modelo_e = MLPClassifier(hidden_layer_sizes=(30,1))

modelo_a.fit(x, y)
modelo_b.fit(x, y)
modelo_c.fit(x, y)

modelo_a.predict(x)
modelo_b.predict(x)
modelo_c.predict(x)

###
def crear_regresion_linea(..., positive):
    return {
        'model_type': "linear_regression",
        'coefs': None,
        'intercept': None,
        'positive': positive,

    }
modelo_a = crear_regresion_linea(Positive=False)
# {
#         'model_type': "linear_regression",
#         'coefs': None,
#         'intercept': None,
#         'positive': False,

# }

modelo_b = crear_regresion_linea(Positive=False)
# {
#         'model_type': "linear_regression",
#         'coefs': None,
#         'intercept': None,
#         'positive': True,

# }