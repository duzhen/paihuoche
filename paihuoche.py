import sys, os
import random

sys.setrecursionlimit(2000)

pokerA = []
pokerB = []
huoche = []

count = 0
PLAY = sys.argv[1] if len(sys.argv) > 1 else 'A'

def tui(pokerX, che):
	global count
	print(count, "tuiche", che, "index", huoche.index(che))
	pokerX.extend(huoche[huoche.index(che):])
	pokerX.append(che)
	del(huoche[huoche.index(che):])

def paihuoche(play):
	global count
	with open('metrics.csv', 'a') as f:
		f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(count,len(pokerA),len(pokerB),len(huoche),'-'.join(map(str,pokerA)),'-'.join(map(str,pokerB)),'-'.join(map(str,huoche))))
	if len(pokerA) == 0:
		print(count, "Player B is win!", len(pokerB), pokerB, pokerA, huoche)
		return
	elif len(pokerB) == 0:
		print(count, "Player A is win!", len(pokerA), pokerA, pokerB, huoche)
		return
	count+=1
	if play == 'A':
		che = pokerA.pop(0)
		print("A", che, "paihuoche", huoche)
		if che in huoche:
			#A tuiche
			#print("A tuiche", che, "index", huoche.index(che))
			tui(pokerA, che)
			#print("huoche", huoche)
			#print(pokerA, pokerB)
			#return
			paihuoche('A')
		else:
			huoche.append(che)
			#B pai
			che = pokerB.pop(0)
			print("B", che, "paihuoche", huoche)
			if che in huoche:
				#B tuiche
				tui(pokerB, che)
				paihuoche('B')
			else:
				huoche.append(che)
				paihuoche(play)
	else:
		che = pokerB.pop(0)
		print("B", che, "paihuoche", huoche)
		if che in huoche:
			#B tuiche
			tui(pokerB, che)
			paihuoche('B')
		else:
			huoche.append(che)
			#A pai
			che = pokerA.pop(0)
			print("A", che, "paihuoche", huoche)
			if che in huoche:
				#A tuiche
				tui(pokerA, che)
				paihuoche('A')
			else:
				huoche.append(che)
				paihuoche(play)


if not len(pokerA) and not len(pokerB):
	SERVE = sys.argv[2] if len(sys.argv) > 2 else 'A'
	DEAL = sys.argv[3] if len(sys.argv) > 3 else '0'
	poker = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,
			 1,2,3,4,5,6,7,8,9,10,11,12,13,14,
			 1,2,3,4,5,6,7,8,9,10,11,12,13,
			 1,2,3,4,5,6,7,8,9,10,11,12,13]
	random.shuffle(poker)
	print("HEAP", poker)
	if DEAL == '0':
		if SERVE == 'A':		
			pokerA = poker[0::2]
			pokerB = poker[1::2]
		else:	
			pokerA = poker[1::2]
			pokerB = poker[0::2]
	else:
		if SERVE == 'A':
			pokerA = poker[0:int(len(poker)/2)]
			pokerB = poker[int(len(poker)/2):]
		else:
			pokerA = poker[int(len(poker)/2):]
			pokerB = poker[0:int(len(poker)/2)]

	print("POKER A", pokerA, len(pokerA))
	print("POKER B", pokerB, len(pokerB))
	
else:
	print("POKER A", pokerA, len(pokerA))
	print("POKER B", pokerB, len(pokerB))
	
with open('metrics.csv', 'w') as f:
    f.write('time,A,B,huochechang,pokerA,pokerB,huoche\n')
paihuoche(PLAY)

os.system('gnuplot -p metrics.gnuplot')
os.system('xdg-open metrics.png')

