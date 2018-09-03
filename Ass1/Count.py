import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
wiki_rel_path = "data/wiki_predict_ED_among.txt"
wiki_abs_path = os.path.join(script_dir, wiki_rel_path)

misspell = 0
correctPrediction = 0
totalPrediction = 0
onlyOnePrediction = 0
totalPredictionAfterNgram = 0
correctPredictionAfterNgram = 0
onlyOnePredictionAfterNgram = 0


with open(wiki_abs_path, "r") as f:
    for line in f:
        if line.split(" | ")[0] == "1":      # accuracy (for each word)
            correctPrediction += 1
        if line.split(" | ")[1] == "1":      # accuracy after N-gram (for each word)
            correctPredictionAfterNgram += 1
        if int(line.split(" | ")[2]) == 1:
            onlyOnePrediction += 1
        if int(line.split(" | ")[3]) == 1:
            onlyOnePredictionAfterNgram += 1
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