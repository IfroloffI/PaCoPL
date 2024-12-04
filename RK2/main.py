from operator import itemgetter

class ProgramLang:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Library:
    def __init__(self, id, name, doc_lib_href, prog_lang_id):
        self.id = id
        self.name = name
        self.doc_lib_href = doc_lib_href
        self.prog_lang_id = prog_lang_id

class ProgLangLib:
    def __init__(self, prog_lang_id, lib_id):
        self.prog_lang_id = prog_lang_id
        self.lib_id = lib_id

def get_one_to_many(prog_langs, libs):
    return [(lib.name, lib.doc_lib_href, pl.name)
            for pl in prog_langs
            for lib in libs
            if lib.prog_lang_id == pl.id]

def get_many_to_many(pl_libs, libs, prog_langs):
    many_to_many_temp = [(pl.name, ps.prog_lang_id, ps.lib_id)
                         for pl in prog_langs
                         for ps in pl_libs
                         if ps.prog_lang_id == pl.id]

    return [(lib.name, lib.doc_lib_href, pl_name)
            for pl_name, pl_id, lib_id in many_to_many_temp
            for lib in libs if lib.id == lib_id]

def first_task(lib_list):
    return sorted(lib_list, key=itemgetter(0))

def second_task(lib_list):
    res_2 = []
    temp_dict = dict()
    for i in lib_list:
        if i[2] in temp_dict:
            temp_dict[i[2]] += 1
        else:
            temp_dict[i[2]] = 1
    for i in temp_dict.keys():
        res_2.append((i, temp_dict[i]))

    res_2.sort(key=itemgetter(1), reverse=True)
    return res_2

def third_task(lib_list, end_ch):
    return [(i[0], i[2]) for i in lib_list if str(i[0]).endswith(end_ch)]

def main():
    prog_langs = [
        ProgramLang(1, "C++"),
        ProgramLang(2, "Java"),
        ProgramLang(3, "Kotlin"),
    ]

    libs = [
        Library(1, "JUnit4", "https://kotlinlang.org/docs/jvm-test-using-junit.html", 3),
        Library(2, "JUnit4", "https://junit.org/junit4/", 2),
        Library(3, "JUnit5", "https://junit.org/junit5/", 3),
        Library(4, "Cucumber", "https://cucumber.io/docs/installation/java/", 3),
        Library(5, "iostream", "https://en.cppreference.com/w/cpp/header/iostream", 1),
        Library(6, "stdlib", "https://en.cppreference.com/w/cpp/header/cstdlib", 1)
    ]

    pl_libs = [
        ProgLangLib(1, 5),
        ProgLangLib(1, 6),
        ProgLangLib(3, 4),
        ProgLangLib(3, 3),
        ProgLangLib(2, 2),
        ProgLangLib(3, 1),
    ]

    one_to_many = get_one_to_many(prog_langs, libs)
    many_to_many = get_many_to_many(pl_libs, libs, prog_langs)

    print('Задание Б1')
    for lib in first_task(one_to_many):
        print(lib)

    print("\nЗадание Б2")
    print(second_task(one_to_many))

    print("\nЗадание Б3")
    print(third_task(many_to_many, '4'))

if __name__ == '__main__':
    main()
