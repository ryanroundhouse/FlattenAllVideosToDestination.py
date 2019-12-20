import unittest
import FlattenUtils

class TestFlattenUtils(unittest.TestCase): 
    def test_getFilesToMigrateThrowsExceptionIfNoPathProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("", [], False)

    def test_getFilesToMigrateThrowsExceptionIfInvalidFolderProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("c:/lkihaghdklhdghklagdklhadgklhakjlgjkladg", [], False)

    def test_getFilesToMigrateThrowsExceptionIfFileNotFolderIsProvided(self):
        with self.assertRaises(Exception):
            FlattenUtils.getFilesToMigrate("./test/1/herewego.mp4", [], False)

    def test_getFilesToMigrateReturnsBothFileWhenProvidedPath(self):
        path = "./test/1/"
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [], False), ["./test/1/herewego.mp4", "./test/1/movie.txt"])

    def test_getFilesToMigrateReturnsOnlyMP4WhenProvidedPathAndMP4Filter(self):
        path = "./test/1/"
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [".mp4"], False), ["./test/1/herewego.mp4"])

    def test_getFilesToMigrateReturnsFilesFromSubfolders(self):
        path = "./test/1/"
        self.assertEqual(FlattenUtils.getFilesToMigrate(path, [".mkv"], True), ["./test/1/season 1/episodes/s01e01.mkv"])