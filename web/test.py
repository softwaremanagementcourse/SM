import sys
sys.path.append("..")

from atm import ATM

if __name__ == "__main__":
    atm = ATM()
    results = atm.run(train_path='https://atm-data.s3.amazonaws.com/pollution_1.csv')
    #str = results.describe()
    str = results.get_best_classifier().__repr__()
    print str
    print "hello world"
    print "test!!!"