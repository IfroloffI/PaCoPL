import main
from operator import itemgetter
import unittest


class TestMainMethods(unittest.TestCase):

    def setUp(self):
        self.prog_langs = [
            main.ProgramLang(1, "C++"),
            main.ProgramLang(2, "Java"),
            main.ProgramLang(3, "Kotlin"),
        ]

        self.libs = [
            main.Library(1, "JUnit4", "https://kotlinlang.org/docs/jvm-test-using-junit.html", 3),
            main.Library(2, "JUnit4", "https://junit.org/junit4/", 2),
            main.Library(3, "JUnit5", "https://junit.org/junit5/", 3),
            main.Library(4, "Cucumber", "https://cucumber.io/docs/installation/java/", 3),
            main.Library(5, "iostream", "https://en.cppreference.com/w/cpp/header/iostream", 1),
            main.Library(6, "stdlib", "https://en.cppreference.com/w/cpp/header/cstdlib", 1)
        ]

        self.pl_libs = [
            main.ProgLangLib(1, 5),
            main.ProgLangLib(1, 6),
            main.ProgLangLib(3, 4),
            main.ProgLangLib(3, 3),
            main.ProgLangLib(2, 2),
            main.ProgLangLib(3, 1),
        ]

        self.one_to_many = [
            ('JUnit5', 'https://junit.org/junit5/', 'Kotlin'),
            ('Cucumber', 'https://cucumber.io/docs/installation/java/', 'Kotlin'),
            ('JUnit4', 'https://junit.org/junit4/', 'Java'),
            ('JUnit4', 'https://kotlinlang.org/docs/jvm-test-using-junit.html', 'Kotlin'),
            ('iostream', 'https://en.cppreference.com/w/cpp/header/iostream', 'C++'),
            ('stdlib', 'https://en.cppreference.com/w/cpp/header/cstdlib', 'C++')
        ]

    def test_first_task_method(self):
        result = main.first_task(self.one_to_many)
        reference = sorted(self.one_to_many, key=itemgetter(0))
        self.assertEqual(result, reference)

    def test_second_task_method(self):
        result = main.second_task(self.one_to_many)
        reference = [('Kotlin', 3), ('C++', 2), ('Java', 1)]
        self.assertEqual(result, reference)

    def test_third_task_method(self):
        many_to_many = [
            ('JUnit4', 'https://kotlinlang.org/docs/jvm-test-using-junit.html', 'Kotlin'),
            ('JUnit4', 'https://junit.org/junit4/', 'Java'),
            ('JUnit5', 'https://junit.org/junit5/', 'Kotlin'),
            ('Cucumber', 'https://cucumber.io/docs/installation/java/', 'Kotlin'),
            ('iostream', 'https://en.cppreference.com/w/cpp/header/iostream', 'C++'),
            ('stdlib', 'https://en.cppreference.com/w/cpp/header/cstdlib', 'C++'),
        ]

        result = main.third_task(many_to_many, '4')
        reference = [('JUnit4', 'Java'), ('JUnit4', 'Kotlin')]
        self.assertEqual(sorted(result), sorted(reference))  # Сравниваем отсортированные списки


if __name__ == '__main__':
    unittest.main()
