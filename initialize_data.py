import re
import sqlite3

expr = re.compile("[\d]+,")

stjornarskra_data = []
stjornarskra_insert = []
with open('data/stjornarskra.txt', 'r') as infile:
	for line in infile.readlines():
		#stjornarskra_data.append(line.split())
		stjornarskra_data.append((line.split(',')[0], expr.split(line)[1]))
		stjornarskra_insert.append((1,expr.split(line)[1], line.split(',')[0]))

frumvarp_data = []
frumvarp_insert = []
with open('data/frumvarp.txt', 'r') as infile:
	for line in infile.readlines():
		#stjornarskra_data.append(line.split())
		frumvarp_data.append((line.split(',')[0], expr.split(line)[1]))
		frumvarp_insert.append((2,expr.split(line)[1], line.split(',')[0]))

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

#insert sentances
#c.executemany('insert into compare_sentance (origin, text, article_nr) values (?,?,?)', stjornarskra_insert)
#c.executemany('insert into compare_sentance (origin, text, article_nr) values (?,?,?)', frumvarp_insert)
#conn.commit()

#insert articles
#article_nrs = list(set(c.execute('select article_nr from compare_sentance where origin=1').fetchall()))
#article_nrs_sorting = sorted([int(i[0]) for i in article_nrs])
#article_nrs = ([(str(i),) for i in article_nrs_sorting])
#c.executemany('insert into compare_article (nr) values (?)', article_nrs)
#conn.commit()

#insert article to sentance relations

#get all stjornarskra articles
#articles = c.execute('select id, nr from compare_article').fetchall()
#for row in articles:
#	for article_id in c.execute('select id from compare_sentance where article_nr=?', (row[1],)).fetchall():
#		c.execute('insert into compare_article_sentances (article_id, sentance_id) values (?,?)', (row[0], article_id[0]))
#conn.commit()

#insert related


conn.close()