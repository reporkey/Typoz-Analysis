import editdistance
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
birkbeck_predict_rel_path = "data/birkbeck_predict_ED_among.txt"
birkbeck_predict_abs_path = os.path.join(script_dir, birkbeck_predict_rel_path)
# birkbeck_predict_rel_path = "data/birkbeck_predict_ED_among.txt"
# birkbeck_predict_abs_path = os.path.join(script_dir, birkbeck_predict_rel_path)

# read dict
with open(dict_abs_path, "r") as f:
    dictionary_list = f.read().splitlines()

# birkbeck
with open(birkbeck_misspell_abs_path, "r") as fr_misspell:
    with open(birkbeck_correct_abs_path, "r") as fr_correct:
        birkbeck_misspell = fr_misspell.read().splitlines()
        birkbeck_correct = fr_correct.read().splitlines()
        for i in range(0, len(birkbeck_misspell)):
            birkbeck_predict = []
            dist = math.inf
            for each in dictionary_list:
                temp = editdistance.eval(birkbeck_misspell[i], each)
                if temp < dist:
                    dist = temp
                    birkbeck_predict = [each]
                if temp == dist:
                    if (each not in birkbeck_predict):
                        birkbeck_predict.append(each)
            birkbeck_predict_new = []
            dist_ngram = -math.inf
            for predict in birkbeck_predict:
                temp_ngram = ngram.NGram.compare(predict, birkbeck_misspell[i], N=2)
                if temp_ngram > dist_ngram:
                    dist_ngram = temp_ngram
                    birkbeck_predict_new = [predict]
                if temp_ngram == dist_ngram:
                    if (predict not in birkbeck_predict_new):
                        birkbeck_predict_new.append(predict)
            print(birkbeck_predict_new)
            
            fw = open(birkbeck_predict_abs_path, "a")
            fw.write(str(int(any(birkbeck_correct[i] in s for s in birkbeck_predict))) + " | ")      # accuracy (for each word)
            fw.write(str(int(any(birkbeck_correct[i] in s for s in birkbeck_predict_new))) + " | ")  # accuracy after ngram
            fw.write(str(len(birkbeck_predict)) + " | ")       # predictions length
            fw.write(str(len(birkbeck_predict_new)) + " | ")   # predictions length after ngram
            fw.write(birkbeck_misspell[i] + " | ")             # misspell
            fw.write(birkbeck_correct[i] + " | ")              # correct
            fw.write(str(dist) + " | ")                    # GED distance
            fw.write(str(dist_ngram) + " | ")              # ngram distance
            fw.write(', '.join(birkbeck_predict))            # all predictions
            fw.write('\n')
            fw.close()
            