import editdistance
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
# birkbeck_predict_rel_path = "data/birkbeck_predict_ED.txt"
# birkbeck_predict_abs_path = os.path.join(script_dir, birkbeck_predict_rel_path)
wiki_correct_rel_path = "data/wiki_correct.txt"
wiki_correct_abs_path = os.path.join(script_dir, wiki_correct_rel_path)
wiki_misspell_rel_path = "data/wiki_misspell.txt"
wiki_misspell_abs_path = os.path.join(script_dir, wiki_misspell_rel_path)
# wiki_predict_rel_path = "data/wiki_predict_ED.txt"
# wiki_predict_abs_path = os.path.join(script_dir, wiki_predict_rel_path)

# read dict
with open(dict_abs_path, "r") as f:
    dictionary_list = f.read().splitlines()

# birkbeck
# with open(birkbeck_misspell_abs_path, "r") as fr_misspell:
#     with open(birkbeck_correct_abs_path, "r") as fr_correct:
#         birkbeck_misspell = fr_misspell.read().splitlines()
#         birkbeck_correct = fr_correct.read().splitlines()
#         for i in range(0, len(birkbeck_misspell)):
#             birkbeck_predict = ""
#             dist = math.inf
#             for each in dictionary_list:
#                 temp = editdistance.eval(birkbeck_misspell[i], each)
#                 if temp < dist:
#                     dist = temp
#                     birkbeck_predict = each
#             print(birkbeck_misspell[i])
#             fw = open(birkbeck_predict_abs_path, "a")
#             fw.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict))))
#             fw.write('{:<20}'.format(birkbeck_misspell[i]))
#             fw.write('{:<20}'.format(birkbeck_predict))
#             fw.write('{:<20}'.format(birkbeck_correct[i]))
#             fw.write('{:<10}'.format(str(dist)))
#             fw.write('\n')
#             fw.close()


# wiki
with open(wiki_misspell_abs_path, "r") as fr_misspell:
    with open(wiki_correct_abs_path, "r") as fr_correct:
        wiki_misspell = fr_misspell.read().splitlines()
        wiki_correct = fr_correct.read().splitlines()
        for i in range(0, len(wiki_misspell)):
            wiki_predict = ""
            dist = math.inf
            for each in dictionary_list:
                temp = editdistance.eval(wiki_misspell[i], each)
                if temp < dist:
                    dist = temp
                    wiki_predict = each
            print(wiki_misspell[i])
            fw = open(wiki_predict_abs_path, "a")
            fw.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict))))
            fw.write('{:<20}'.format(wiki_misspell[i]))
            fw.write('{:<20}'.format(wiki_predict))
            fw.write('{:<20}'.format(wiki_correct[i]))
            fw.write('{:<10}'.format(str(dist)))
            fw.write('\n')
            fw.close()
