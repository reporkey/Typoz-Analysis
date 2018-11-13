# Distance = (G1 or G2) / (G1 and G2)

import math
import os
import ngram

# file path
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
dict_rel_path = "data/dict.txt"
dict_abs_path = os.path.join(script_dir, dict_rel_path)
birkbeck_correct_rel_path = "data/birkbeck_correct.txt"
birkbeck_correct_abs_path = os.path.join(script_dir, birkbeck_correct_rel_path)
birkbeck_misspell_rel_path = "data/birkbeck_misspell.txt"
birkbeck_misspell_abs_path = os.path.join(script_dir, birkbeck_misspell_rel_path)
birkbeck_predict2_rel_path = "data/birkbeck_predict_Ngram_2.txt"
birkbeck_predict2_abs_path = os.path.join(script_dir, birkbeck_predict2_rel_path)
birkbeck_predict3_rel_path = "data/birkbeck_predict_Ngram_3.txt"
birkbeck_predict3_abs_path = os.path.join(script_dir, birkbeck_predict3_rel_path)
birkbeck_predict4_rel_path = "data/birkbeck_predict_Ngram_4.txt"
birkbeck_predict4_abs_path = os.path.join(script_dir, birkbeck_predict4_rel_path)
birkbeck_predict5_rel_path = "data/birkbeck_predict_Ngram_5.txt"
birkbeck_predict5_abs_path = os.path.join(script_dir, birkbeck_predict5_rel_path)
wiki_correct_rel_path = "data/wiki_correct.txt"
wiki_correct_abs_path = os.path.join(script_dir, wiki_correct_rel_path)
wiki_misspell_rel_path = "data/wiki_misspell.txt"
wiki_misspell_abs_path = os.path.join(script_dir, wiki_misspell_rel_path)
wiki_predict2_rel_path = "data/wiki_predict_Ngram_2.txt"
wiki_predict2_abs_path = os.path.join(script_dir, wiki_predict2_rel_path)
wiki_predict3_rel_path = "data/wiki_predict_Ngram_3.txt"
wiki_predict3_abs_path = os.path.join(script_dir, wiki_predict3_rel_path)
wiki_predict4_rel_path = "data/wiki_predict_Ngram_4.txt"
wiki_predict4_abs_path = os.path.join(script_dir, wiki_predict4_rel_path)
wiki_predict5_rel_path = "data/wiki_predict_Ngram_5.txt"
wiki_predict5_abs_path = os.path.join(script_dir, wiki_predict5_rel_path)

# read dict
with open(dict_abs_path, "r") as f:
    dictionary_list = f.read().splitlines()

# birkbeck
with open(birkbeck_misspell_abs_path, "r") as fr_misspell:
    with open(birkbeck_correct_abs_path, "r") as fr_correct:

        birkbeck_misspell = fr_misspell.read().splitlines()
        birkbeck_correct = fr_correct.read().splitlines()
        birkbeck_predict2 = ""
        birkbeck_predict3 = ""
        birkbeck_predict4 = ""
        birkbeck_predict5 = ""
        dist2 = -math.inf
        dist3 = -math.inf
        dist4 = -math.inf
        dist5 = -math.inf
        for i in range(0, len(birkbeck_misspell)):
            fw2 = open(birkbeck_predict2_abs_path, "a")
            fw3 = open(birkbeck_predict3_abs_path, "a")
            fw4 = open(birkbeck_predict4_abs_path, "a")
            fw5 = open(birkbeck_predict5_abs_path, "a")
            for each in dictionary_list:
                temp2 = ngram.NGram.compare(birkbeck_misspell[i], each, N=2)
                temp3 = ngram.NGram.compare(birkbeck_misspell[i], each, N=3)
                temp4 = ngram.NGram.compare(birkbeck_misspell[i], each, N=4)
                temp5 = ngram.NGram.compare(birkbeck_misspell[i], each, N=5)
                if temp2 > dist2:
                    dist2 = temp2
                    birkbeck_predict2 = each
                if temp3 > dist3:
                    dist3 = temp3
                    birkbeck_predict3 = each
                if temp4 > dist4:
                    dist4 = temp4
                    birkbeck_predict4 = each
                if temp5 > dist5:
                    dist5 = temp5
                    birkbeck_predict5 = each
            print(birkbeck_misspell[i])
            fw2.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict2))))
            fw2.write('{:<20}'.format(birkbeck_misspell[i]))
            fw2.write('{:<20}'.format(birkbeck_predict2))
            fw2.write('{:<20}'.format(birkbeck_correct[i]))
            fw2.write('{:<10}'.format(str(dist2)))
            fw2.write('\n')
            fw3.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict3))))
            fw3.write('{:<20}'.format(birkbeck_misspell[i]))
            fw3.write('{:<20}'.format(birkbeck_predict3))
            fw3.write('{:<20}'.format(birkbeck_correct[i]))
            fw3.write('{:<10}'.format(str(dist3)))
            fw3.write('\n')
            fw4.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict4))))
            fw4.write('{:<20}'.format(birkbeck_misspell[i]))
            fw4.write('{:<20}'.format(birkbeck_predict4))
            fw4.write('{:<20}'.format(birkbeck_correct[i]))
            fw4.write('{:<10}'.format(str(dist4)))
            fw4.write('\n')
            fw5.write('{:<5}'.format(str(int(birkbeck_correct[i] == birkbeck_predict5))))
            fw5.write('{:<20}'.format(birkbeck_misspell[i]))
            fw5.write('{:<20}'.format(birkbeck_predict5))
            fw5.write('{:<20}'.format(birkbeck_correct[i]))
            fw5.write('{:<10}'.format(str(dist5)))
            fw5.write('\n')
            fw2.close()
            fw3.close()
            fw4.close()
            fw5.close()


# wiki
with open(wiki_misspell_abs_path, "r") as fr_misspell:
    with open(wiki_correct_abs_path, "r") as fr_correct:

        wiki_misspell = fr_misspell.read().splitlines()
        wiki_correct = fr_correct.read().splitlines()
        wiki_predict2 = ""
        wiki_predict3 = ""
        wiki_predict4 = ""
        wiki_predict5 = ""
        dist2 = -math.inf
        dist3 = -math.inf
        dist4 = -math.inf
        dist5 = -math.inf
        for i in range(0, len(wiki_misspell)):
            fw2 = open(wiki_predict2_abs_path, "a")
            fw3 = open(wiki_predict3_abs_path, "a")
            fw4 = open(wiki_predict4_abs_path, "a")
            fw5 = open(wiki_predict5_abs_path, "a")
            for each in dictionary_list:
                temp2 = ngram.NGram.compare(wiki_misspell[i], each, N=2)
                temp3 = ngram.NGram.compare(wiki_misspell[i], each, N=3)
                temp4 = ngram.NGram.compare(wiki_misspell[i], each, N=4)
                temp5 = ngram.NGram.compare(wiki_misspell[i], each, N=5)
                if temp2 > dist2:
                    dist2 = temp2
                    wiki_predict2 = each
                if temp3 > dist3:
                    dist3 = temp3
                    wiki_predict3 = each
                if temp4 > dist4:
                    dist4 = temp4
                    wiki_predict4 = each
                if temp5 > dist5:
                    dist5 = temp5
                    wiki_predict5 = each
            print(wiki_misspell[i])
            fw2.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict2))))
            fw2.write('{:<20}'.format(wiki_misspell[i]))
            fw2.write('{:<20}'.format(wiki_predict2))
            fw2.write('{:<20}'.format(wiki_correct[i]))
            fw2.write('{:<10}'.format(str(dist2)))
            fw2.write('\n')
            fw3.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict3))))
            fw3.write('{:<20}'.format(wiki_misspell[i]))
            fw3.write('{:<20}'.format(wiki_predict3))
            fw3.write('{:<20}'.format(wiki_correct[i]))
            fw3.write('{:<10}'.format(str(dist3)))
            fw3.write('\n')
            fw4.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict4))))
            fw4.write('{:<20}'.format(wiki_misspell[i]))
            fw4.write('{:<20}'.format(wiki_predict4))
            fw4.write('{:<20}'.format(wiki_correct[i]))
            fw4.write('{:<10}'.format(str(dist4)))
            fw4.write('\n')
            fw5.write('{:<5}'.format(str(int(wiki_correct[i] == wiki_predict5))))
            fw5.write('{:<20}'.format(wiki_misspell[i]))
            fw5.write('{:<20}'.format(wiki_predict5))
            fw5.write('{:<20}'.format(wiki_correct[i]))
            fw5.write('{:<10}'.format(str(dist5)))
            fw5.write('\n')
            fw2.close()
            fw3.close()
            fw4.close()
            fw5.close()