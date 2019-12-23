import unittest
import FlattenUtils
import os

class TestFlattenUtils(unittest.TestCase): 

    def test_getFilesToMigrateThrowsExceptionIfNoPathProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("", [])

    def test_getFilesToMigrateThrowsExceptionIfInvalidFolderProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("c:/lkihaghdklhdghklagdklhadgklhakjlgjkladg", [])

    def test_getFilesToMigrateThrowsExceptionIfFileNotFolderIsProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("./test/1/herewego.mp4", [])

    def test_getFilesToMigrateReturnsAllFilesWhenProvidedPath(self):
        path = "./test/"
        pwd = os.path.abspath(os.path.curdir)
        expectedOutput = [
            os.path.join(pwd, "test/1/herewego.mp4"),
            os.path.join(pwd, "test/1/movie.txt"),
            os.path.join(pwd, "test/1/season 1/episodes/s01e01.mkv"),
            os.path.join(pwd, "test/2/movie.mkv")
        ]
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, []), expectedOutput)

    def test_getFilesToMigrateReturnsOnlyMP4WhenProvidedPathAndMP4Filter(self):
        path = "./test/1/"
        pwd = os.path.abspath(os.path.curdir)
        expectedOutput = [
            os.path.join(pwd, "test/1/herewego.mp4")
        ]
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [".mp4"]), expectedOutput)

    def test_getFilesToMigrateReturnsFilesFromSubfolders(self):
        path = "./test/1/"
        pwd = os.path.abspath(os.path.curdir)
        expectedOutput = [
            os.path.join(pwd, "test/1/season 1/episodes/s01e01.mkv")
        ]
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [".mkv"]), expectedOutput)

    def test_getFilesToMigrateReturnsTwoFilesFromSubfolders(self):
        path = "./test/"
        pwd = os.path.abspath(os.path.curdir)
        expectedOutput = [
            os.path.join(pwd, "test/1/season 1/episodes/s01e01.mkv"),
            os.path.join(pwd, "test/2/movie.mkv")
        ]
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [".mkv"]), expectedOutput)