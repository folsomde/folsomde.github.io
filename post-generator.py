import numpy as np 

metadata_file = np.load('metadata.npz',allow_pickle=True)
metadata = metadata_file['metadata'][()]

nl='\n'
data_list = []
for y in range(21):
	year = 1998+y
	for m in ["01", "05"]:
		mlett = "J" if m == "01" else "M"
		for snum, s in enumerate(['M','E', 'Q', 'T']):
			subject = {'E': 'E&M', 'M':'Mechanics', 'T': 'Statmech', 'Q': 'QM'}[s]
			for i in range(3):
				problem = i+1
				pstring = f"{mlett}{year%100:02d}{s}{problem}"
				fname = f'{year}-{m}-{13-(3*snum+problem)}-{s}{problem}-{metadata[pstring][0].replace(" ", "-") if pstring in metadata else "NEED-TITLE"}'
				exam_num = 2*y+(0 if m == '01' else 1) -(1 if y > 13 else 0) -(1 if y > 16 else 0)-(1 if y > 18 else 0)
				exam_str = f"{mlett}{year%100:02d}"
				prob_str = f"{s}{problem}"
				pdf_location = f"{year}{mlett}{problem}{s}"

				data = {"fname":fname,
						"pstring":pstring,
						"subject":subject,
						"exam_str":exam_str,
						"pdf_location":pdf_location,
						"exam_num":exam_num,
						"prob_str":prob_str,
						}
				data_list.append(data)


for i, data in enumerate(data_list):
	if data['pstring'] in metadata:
		file = open(f'./_posts/problems/{data["fname"]}.md','w')
		file.write(f'''---
title: "{data["pstring"]} &ndash; {metadata[data["pstring"]][0] if data["pstring"] in metadata else "NEED TITLE"}"
layout: post
categories:
  - Prelims
  - Problems
tags:
  - {data["subject"]}
  - {data["exam_str"]}
{''.join(['  - '+tag+nl for tag in metadata[data["pstring"]][1]])}
permalink: /:categories/:year/:month/{data["prob_str"]}:output_ext
comments: false
---
<object data="{data['pdf_location']}.pdf" type="application/pdf" width="100%" height="500"></object>

<div class='navbar'>
	<div float='left'><button onclick="window.location='{"" if i == 0 else data_list[i-1]['prob_str']}.html'" {"style='visibility: hidden;'" if data['prob_str'] == 'M1' else ""}>Previous Problem</button></div>
	<div float='center'><button onclick="window.location='https://princetonprelim.com/prelim/{data["exam_num"]}/'">Check for solutions</button></div>
	<div float='right'><button onclick="window.location='{"" if i+1 >= len(data_list) else data_list[i+1]['prob_str']}.html'" {"style='visibility: hidden;'" if data['prob_str'] == 'T3' else ""}> Next Problem</button></div>
</div>
''')
