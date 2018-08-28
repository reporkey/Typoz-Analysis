import brew_distance
import math
import os

# file path
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
dict_rel_path = "data/dict.txt"
dict_abs_path = os.path.join(script_dir, dict_rel_path)
birkbeck_correct_rel_path = "data/birkbeck_correct.txt"
birkbeck_correct_abs_path = os.path.join(script_dir, birkbeck_correct_rel_path)
birkbeck_misspell_rel_path = "data/birkbeck_misspell.txt"
birkbeck_misspell_abs_path = os.path.join(script_dir, birkbeck_misspell_rel_path)
birkbeck_predict_rel_path = "data/birkbeck_predict_ED.txt"
birkbeck_predict_abs_path = os.path.join(script_dir, birkbeck_predict_rel_path)
wiki_correct_rel_path = "data/wiki_correct.txt"
wiki_correct_abs_path = os.path.join(script_dir, wiki_correct_rel_path)
wiki_misspell_rel_path = "data/wiki_misspell.txt"
wiki_misspell_abs_path = os.path.join(script_dir, wiki_misspell_rel_path)
wiki_predict_rel_path = "data/wiki_predict_ED.txt"
wiki_predict_abs_path = os.path.join(script_dir, wiki_predict_rel_path)

# read dict
dictionary = ()
with open(dict_abs_path, "r") as f:
    dictionary = dictionary + (f.read().splitlines(),)

# birkbeck_misspell
fw = open(birkbeck_predict_abs_path, "w")
with open(birkbeck_misspell_abs_path, "r") as fr_misspell:
    with open(birkbeck_correct_abs_path, "r") as fr_correct:

        birkbeck_misspell = fr_misspell.read().splitlines()
        birkbeck_correct = fr_correct.read().splitlines()
        birkbeck_predict = ""
        min_distance = -math.inf

        for each in dictionary:
            try:
                temp = brew_distance.distance(birkbeck_misspell, each, output="distance", cost=(1, -1, -1, -1))
                if temp > min_distance:
                    min_distance = temp
                    birkbeck_predict = each
            except brew_distance.BrewDistanceException as error:
                print(str(error))
        fw.write(str(int(birkbeck_correct == birkbeck_predict)) + '\t\t\t' + birkbeck_misspell + '\t\t\t' + birkbeck_predict + '\t\t\t' + birkbeck_correct + '\t\t\t' + str(min_distance) + '\n')
fw.close()


# read and predict birkbeck_misspell
fw = open(wiki_predict_abs_path, "w")
with open(wiki_misspell_abs_path, "r") as fr_misspell:
    with open(wiki_correct_abs_path, "r") as fr_correct:

        wiki_misspell = fr_misspell.read().splitlines()
        wiki_correct = fr_correct.read().splitlines()
        wiki_predict = ""
        min_distance = -math.inf

        for each in dictionary:
            try:
                temp = brew_distance.distance(wiki_misspell, each, output="distance", cost=(1, -1, -1, -1))
                if temp > min_distance:
                    min_distance = temp
                    wiki_predict = each
            except brew_distance.BrewDistanceException as error:
                print(str(error))
        fw.write(str(int(wiki_correct == wiki_predict)) + '\t\t\t' + wiki_misspell + '\t\t\t' + wiki_predict + '\t\t\t' + wiki_correct + '\t\t\t' + str(min_distance) + '\n')
fw.close()