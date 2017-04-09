# -*- coding: utf-8 -*-

from tkinter import *
import random
import sqlite3

def genTest():
	global n_ans
	global n_questions
	global numsOfAnswers
	global numOfQuestion
	global numsO
	global rus
	global en
	global task
	global answers
	global check
	global bg_butt
	global str_ch
	
	numOfQuestion += 1
	if numOfQuestion == n_questions:
		showScore()
		return
	
	for i in range(n_ans):
		numsOfAnswers[i] = i
	random.shuffle(numsOfAnswers)
	
	task.configure(text = rus[numsOfQuestions[numOfQuestion]])
	for i in range(n_ans):
		answers[i].configure(text = en[numsOfAnswers[i]][numsOfQuestions[numOfQuestion]], bg = bg_butt)
	check.configure(text = str_ch)

def onClick(ans):
	global answers
	global checked
	global bg_butt
	global bg_ch_butt
	
	if not(_next):
		if checked != -1:
			answers[checked].configure(bg = bg_butt)
		checked = ans
		answers[ans].configure(bg = bg_ch_butt)

def onClick1():
	onClick(0)

def onClick2():
	onClick(1)
	
def onClick3():
	onClick(2)

def onCheck():
	global _next
	global n_questions
	global n_ans
	global score
	global checked
	global numsOfAnswers
	global numOfQuestion
	global answers
	global check
	global bg_corr_butt
	global bg_incorr_butt
	global str_next
	global str_last
	
	if _next:
		genTest()
		_next = False
	else:
		if checked != -1:
			_next = True
			if numsOfAnswers[checked] == 0:
				answers[checked].configure(bg = bg_corr_butt)
				score += 1
			else:
				answers[checked].configure(bg = bg_incorr_butt)
				num = -1
				for i in range(n_ans):
					if numsOfAnswers[i] == 0:
						num = i
						break
				answers[num].configure(bg = bg_corr_butt)
			checked = -1
			if numOfQuestion != n_questions:
				check.configure(text = str_next)	
			else:
				check.configure(text = str_last)	
	
def showScore():
	global score
	global root
	global task
	global answers
	global check
	global n_questions
	global n_ans
	global bg_score
	global bg_end
	global str_res
	global str_quit
	global title_score
	global _font
	
	task.destroy()
	for i in range(n_ans):
		answers[i].destroy()
	check.destroy()
	root.title(title_score)
	scoreLab = Label(root, width = _width, height = _height, bg = bg_score, text = str_res + str(score) + " из " + str(n_questions) + ".", font = _font)
	end = Button(root, width = _bwidth, height = _bheight, bg = bg_end, text = str_quit, command = onEnd, font = _font)
	scoreLab.pack(fill = 'both', expand = 'yes')
	end.pack(fill = 'both', expand = 'yes')
	root.mainloop()
	
def onEnd():
	global root
	root.destroy()

_width = 41
_height = 2
_bwidth = 40
_bheight = 2
n_ans = 3
n_questions = 10

bg_task = "LightSkyBlue1"
bg_butt = "SteelBlue1"
bg_ch_butt = "MediumPurple1"
bg_corr_butt = "SpringGreen2"
bg_incorr_butt = "red3"
bg_check = "SteelBlue2"
bg_score = "MediumPurple1"
bg_end = "MediumPurple2"

title_quest = "Переведи фразеологизмы"
title_score = "Результаты"

str_ch = "Проверить"
str_next = "Следующий вопрос"
str_last = "Показать результат"
str_res = "Ваш результат "
str_quit = "Выйти"

_font = "Times 25 bold"

numsOfAnswers = [0] * n_ans
numsOfQuestions = [0] * n_questions
numOfQuestion = -1
score = 0
checked = -1
_next = False

for i in range(n_questions):
	numsOfQuestions[i] = i
random.shuffle(numsOfQuestions)
conn = sqlite3.connect("phraseology.db")
cursor = conn.cursor()

cursor.execute("SELECT rus FROM translates")
rus = cursor.fetchall()
en = [0] * n_ans
for i in range(n_ans):
	cursor.execute("SELECT en" + str(i + 1) + " FROM translates")
	en[i] = cursor.fetchall()
for i in range(len(rus)):
	rus[i] = str(rus[i])[2 : -3]
for j in range(3):
	for i in range(len(en[j])):
		en[j][i] = str(en[j][i])[2 : -3]

root = Tk()
root.title(title_quest)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
task = Label(root, width = _width, height = _height, bg = bg_task, font = _font)
answers = [0] * n_ans
for i in range(n_ans):
	answers[i] = Button(root, width = _bwidth, height = _bheight, bg = bg_butt, font = _font)
answers[0].configure(command = onClick1)
answers[1].configure(command = onClick2)
answers[2].configure(command = onClick3)
check = Button(root, width = _bwidth, height = _bheight, bg = bg_check, text = str_ch, command = onCheck, font = _font)

genTest()

task.pack(fill = 'both', expand = 'yes')
for i in range(n_ans):
	answers[i].pack(fill = 'both', expand = 'yes')
check.pack(fill = 'both', expand = 'yes')

root.mainloop()
