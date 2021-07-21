import numpy as np
f = np.load("metadata.npz",allow_pickle=True)
metadata = f['metadata'][()]

topics = {'M': ['Central Force Motion', 'Normal Modes', 'Oscillations', 'Lagrangian Mechanics', 
				'Classical Scattering', 'Continuous Media', 'Fluid Mechanics', 'Rigid Body Motion', 
				'Rolling Constraints', 'Friction', 'Non-Inertial Reference Frames', 'Misc Mechanics'], 
	  	'E': ['EM Waves', 'Vector Potential', 'Waveguides and Cavities', 'Induction', 'EM Fields in Matter', 
			  'Radiation', "Laplace's Equation", 'Multipoles', 'Energy and Momentum of EM Fields', 'Electrostatics',
			  'Curvilinear Coordinates in EM', 'Method of Images', 'Capacitance and Inductance', 'Magnetostatics', 'Misc EM'], 
		'Q': ['Angular Momentum and Spin', 'Eigenstates', 'Quantum Scattering', 'QHO', 'Operators and Pictures', 
			  'Perturbation Theory', '1D QM', '3D QM', 'Atomic QM', 'TDPT', 'Identical Particles', 'WKB Approximation', 
			  'Born Approximation', 'Particles in EM Fields', 'Misc Quantum'], 
		'T': ['Polymers', 'Classical Thermo', 'Bose-Einsten Condensation', 'Ising Model', 'EM Fields in Statmech', 
			  'Brownian Motion', 'Waves', 'Fermi Gas', 'Bose Gas', 'Chemical Potential', 'Heat Engines', 'Crystal Lattice', 
			  'Diatomic Gas in E-Fields', 'Phase Transitions', 'Gas in Container', 'Oscillations', 'Van der Waals Gas', 
			  'Particles on a Line', 'Altitude', 'Hydrogen Formation', 'Misc Statmech']}


current_problem = f['current_problem']

outfile = 'metadata'

# build list of problems
problem_array = []
for y in range(21):
	year = 1998+y
	for m in ["J", "M"]:
		for snum, s in enumerate(['M','E', 'Q', 'T']):
			for i in range(3):
				problem = i+1
				pstring = f"{m}{year%100:02d}{s}{problem}"
				problem_array.append(pstring)


import tkinter as tk
from tkinter import font
from tkPDFViewer import tkPDFViewer as pdf

class Checkbar(tk.Frame):
	def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.W):
		tk.Frame.__init__(self, parent)
		self.vars = []
		for pick in picks:
			var = tk.BooleanVar()
			chk = tk.Checkbutton(self, text=pick, variable=var,width=300,height=2)
			chk.pack(side=side, anchor=anchor)
			self.vars.append(var)
	
	def state(self):
		return np.array(list(map((lambda var: var.get()), self.vars)))

def save_metadata():
	global current_problem
	current_problem = current_problem + 1
	if np.all(bar.state() == False):
		tags = ['untagged']
	else:
		tags = type_topics[bar.state()]
	metadata[problem][1] = tags
	print(f"updated {problem} to have tags {metadata[problem][1]}")
	root.destroy()

def exit_loop():
	print('writing metadata')
	np.savez(outfile, metadata=metadata, topics=topics, current_problem=current_problem)
	exit()

def go_back():
	global current_problem
	current_problem = current_problem -1
	root.destroy()
	raise StopIteration

def report_callback_exception(self, exc, val, tb):
	raise exc

tk.Tk.report_callback_exception = report_callback_exception

# exit()
while True:
	try:
		for problem in problem_array[current_problem:]:
			root = tk.Tk()
			# print(font.families())
			# exit()
			root.option_add('*Font', ('terminus', 10))
			text = tk.Message(root,text="tags: "+(", ".join(metadata[problem][1])),width=300)
			text.pack()
			problem_type = problem[3:4]
			type_topics = np.array(topics[problem_type])

			root.title(problem+': '+metadata[problem][0])
			root.geometry('300x700')
			
			
			
			bar = Checkbar(root, type_topics, side=tk.TOP)
			bar.pack()	

			tk.Button(root, text='Continue', command=save_metadata).pack(side=tk.RIGHT)
			tk.Button(root, text='Quit', command=exit_loop).pack(side=tk.RIGHT)
			tk.Button(root, text='Go Back', command=go_back).pack(side=tk.RIGHT)

			root.mainloop()
	except StopIteration:
		pass

print('writing metadata')
np.savez(outfile, metadata=metadata, topics=topics, current_problem=current_problem)