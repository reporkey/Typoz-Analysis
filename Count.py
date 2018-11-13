import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
wiki_rel_path = "data/birkbeck_predict_ED_among.txt"
wiki_abs_path = os.path.join(script_dir, wiki_rel_path)

misspell = 0
correctPrediction = 0
totalPrediction = 0
onlyOnePrediction = 0
totalPredictionAfterNgram = 0
correctPredictionAfterNgram = 0
onlyOnePredictionAfterNgram = 0
wordsWith1GED = 00
wordsWith3LessGED = 0

with open(wiki_abs_path, "r") as f:
    for line in f:
        if line.split(" | ")[0] == "1":         # accuracy (for each word)
            correctPrediction += 1
        if line.split(" | ")[1] == "1":         # accuracy after N-gram (for each word)
            correctPredictionAfterNgram += 1
        if int(line.split(" | ")[2]) == 1:      # words that only has one prediction
            onlyOnePrediction += 1
        if int(line.split(" | ")[3]) == 1:      # words that only has one prediction after N-gram
            onlyOnePredictionAfterNgram += 1
        if int(line.split(" | ")[6]) == 1:      # number of words with GED = 1
            wordsWith1GED += 1
        if int(line.split(" | ")[6]) < 3:      # number of words with GED = 1
            wordsWith3LessGED += 1
        totalPrediction += int(line.split(" | ")[2])            # predictions length
        totalPredictionAfterNgram += int(line.split(" | ")[3])  # predictions length after ngram
        misspell += 1

print("misspell", misspell)
print("correctPrediction", correctPrediction)
print("totalPrediction", totalPrediction)
print("onlyOnePrediction", onlyOnePrediction)
print("correctPredictionAfterNgram", correctPredictionAfterNgram)
print("totalPredictionAfterNgram", totalPredictionAfterNgram)
print("onlyOnePredictionAfterNgram", onlyOnePredictionAfterNgram)
print("wordsWith1GED", wordsWith1GED)
print("wordsWith3LessGED", wordsWith3LessGED)
