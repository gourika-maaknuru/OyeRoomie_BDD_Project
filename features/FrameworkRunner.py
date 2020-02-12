import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    # run Behave + BDD + Python code
    featureFilePath = 'features/search.feature'
    commonRunnerOptions = '--no-capture --no-capture-stderr -f plain'
    fullRunnerOptions = featureFilePath + commonRunnerOptions
    runner_with_options.main("--tags=tagCurrent" + fullRunnerOptions)