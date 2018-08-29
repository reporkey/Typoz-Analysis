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
    dictionary_list = f.read().splitlines()
    for i in range(0, len(dictionary_list)):
        dictionary = dictionary + (dictionary_list[i],)

# birkbeck
fw = open(birkbeck_predict_abs_path, "w")
with open(birkbeck_misspell_abs_path, "r") as fr_misspell:
    with open(birkbeck_correct_abs_path, "r") as fr_correct:

        birkbeck_misspell = fr_misspell.read().splitlines()
        birkbeck_correct = fr_correct.read().splitlines()
        birkbeck_predict = ""
        dist = -math.inf
        for i in range(0, len(birkbeck_misspell)):
            for each in dictionary:
                try:
                    temp = brew_distance.distance(birkbeck_misspell[i], each, output="distance", cost=(1, -1, -1, -1))
                    if temp > dist:
                        dist = temp
                        birkbeck_predict = each
                except brew_distance.BrewDistanceException as error:
                    print(str(error))
            fw.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict))))
            fw.write('{:<20}'.format(birkbeck_misspell[i]))
            fw.write('{:<20}'.format(birkbeck_predict))
            fw.write('{:<20}'.format(birkbeck_correct[i]))
            fw.write('{:<10}'.format(str(dist)))
            fw.write('\n')
fw.close()


# wiki
fw = open(wiki_predict_abs_path, "w")
with open(wiki_misspell_abs_path, "r") as fr_misspell:
    with open(wiki_correct_abs_path, "r") as fr_correct:

        wiki_misspell = fr_misspell.read().splitlines()
        wiki_correct = fr_correct.read().splitlines()
        wiki_predict = ""
        dist = -math.inf
        for i in range(0, len(wiki_misspell)):
            for each in dictionary:
                try:
                    temp = brew_distance.distance(wiki_misspell[i], each, output="distance", cost=(1, -1, -1, -1))
                    if temp > dist:
                        dist = temp
                        wiki_predict = each
                except brew_distance.BrewDistanceException as error:
                    print(str(error))
            fw.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict))))
            fw.write('{:<20}'.format(wiki_misspell[i]))
            fw.write('{:<20}'.format(wiki_predict))
            fw.write('{:<20}'.format(wiki_correct[i]))
            fw.write('{:<10}'.format(str(dist)))
            fw.write('\n')
fw.close()
