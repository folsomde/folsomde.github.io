import numpy as np 

metadata_file = np.load('metadata.npz',allow_pickle=True)
metadata = metadata_file['metadata']

nl='\n'

for y in range(21):
	year = 1998+y
	for m in ["01", "05"]:
		mlett = "J" if m == "01" else "M"
		for snum, s in enumerate(['M','E', 'Q', 'T']):
			subject = {'E': 'E&M', 'M':'Mechanics', 'T': 'Statmech', 'Q': 'QM'}[s]
			for i in range(3):
				problem = i+1
				pstring = f"{mlett}{year%100:02d}{s}{problem}"
				if pstring in metadata:
					file = open(f'./_posts/problems/{year}-{m}-{13-(3*snum+problem)}-{s}{problem}-{metadata[pstring][0].replace(" ", "-") if pstring in metadata else "NEED-TITLE"}.md','w')
					file.write(f'''---
title: "{pstring} &ndash; {metadata[pstring][0] if pstring in metadata else "NEED TITLE"}"
layout: post
categories:
  - Prelims
  - Problems
tags:
  - {subject}
  - {mlett}{year%100:02d}
{''.join(['  - '+tag+nl for tag in metadata[pstring][1]])}
permalink: /:categories/:year/:month/{s}{problem}:output_ext
comments: false
---
<object data="{year}{mlett}{problem}{s}.pdf" type="application/pdf" width="100%" height="500"></object>
<div class="message"><a href='https://princetonprelim.com/prelim/{2*y+(0 if m == '01' else 1) -(1 if y > 11 else 0) -(1 if y > 14 else 0)-(1 if y > 16 else 0)}/'>Check for solutions to this year's exam</a></div>''')
