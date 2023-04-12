import py_entitymatching as em
import pandas as pd
import os, sys
import ydata_profiling as yp

PATH_DIR = os.getcwd()
DATASETS_FOLDER = 'datasets'


class MagellanPineline:
    def __init__(self, fileNameA, fileNameB, matched, expected) -> None:
        pathdir = PATH_DIR + os.sep + DATASETS_FOLDER
        self.__Acsv__ = pathdir + os.sep + fileNameA
        self.__Bcsv__ = pathdir + os.sep + fileNameB
        self.__Matched__ = pathdir + os.sep + matched
        self.A = pd.DataFrame()
        self.B = pd.DataFrame()
        self.matched = pd.DataFrame()
        self.expected = expected

    def readFile(self):
        self.A = pd.read_csv(self.__Acsv__)
        self.B = pd.read_csv(self.__Bcsv__)
        self.C = pd.read_csv(self.__Matched__)


    def down_sampling(self):
        pass

    def execute(self):
        self.readFile()
        print(yp.ProfileReport(self.A))


if __name__ == '__main__':
    file1 = 'imdbProfilesNEW.csv'
    file2 = 'tmdbProfiles.csv'
    matched = 'imdbTmdbIdDuplicates.csv'
    problem = MagellanPineline(file1, file2, matched, 0.8)
    problem.execute()
