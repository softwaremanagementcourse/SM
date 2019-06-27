import sys
sys.path.append("..")

from atm import ATM

if __name__ == "__main__":
    atm = ATM()
    results = atm.run(train_path='data\\17393f30766bf6c307cea1ba211e3561.csv')
    #str = results.describe()
    str = results.get_best_classifier().__repr__()
    print str