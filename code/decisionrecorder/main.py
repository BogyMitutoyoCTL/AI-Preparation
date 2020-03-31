from CombinationBuilder import CombinationBuilder
from Configuration import Configuration
from SaveCombinations import SaveCombinations
from TrainingDataGui import TrainingDataGui

configuration_file = "configuration.json"
output_file = "output.json"

if __name__ == "__main__":
    configuration = Configuration(configuration_file)

    builder = CombinationBuilder(configuration)

    combinations = builder.get_combinations()

    gui = TrainingDataGui(combinations=combinations,
                          configuration=configuration,
                          save_combinations=SaveCombinations(output_file))
    gui.show()
