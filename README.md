## COMP90049 Knowledge Technologies
### Project 1: Waht kinda typoz do poeple mak?

### Code Files
* 	Edit_distance.py
	It takes dict and misspell as inputs, use editdistance to predict and then ngram refine the predictions. In the end it write all info in /data/wiki(birkbeck)_predict_ED_among.txt.
*	Ngram.py
	I was tried to do ngram with N = 2, 3, 4, and 5 seperately. BUT I found it spend too much of time to execute. There's no output files since uncompleted executing.
*	Count.py
	A simple code used to calculate relavent info for evaluation metrics. Including:
		* num of misspell
		* num of correct predictions
		* total num of predictions
		* total num of predictions after refine(after ngram)
		* num of correct prediction after refine
		* num of misspell with only 1 prediction
		* num of misspell with only 1 prediction after refine
		* num of misspell with GED = 1
		* num of misspell with GED < 3

### Data Files
Data files are under data/
*	wiki(birkbeck)_predict_ED.txt: single output by only GED. The origin code was improved to the GED+Ngram code.
*	wiki(birkbeck)_predict_ED_amoung.txt: the output by Edit_distance.py

### Package usage
*	editdistance
*	ngram
