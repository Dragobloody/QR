import numpy as np
import states as st
import transitions as tr
import graph as gr
import pydotplus


# quantities
Q = ['I','V','H','P','O']
# quatity spaces
val_domain = {'I':[0,1],'V':[0,1,2],'H':[0,1,2],'P':[0,1,2],'O':[0,1,2]}
# derivatives
der_domain = {'I':[-1,0,1],'V':[-1,0,1],'H':[-1,0,1],'P':[-1,0,1],'O':[-1,0,1]}
# influence dependencies: 1 = I+, -1 = I-, 0 = nothing
I = np.array([[0,1,0,0,0],
		[0,0,0,0,0],
		[0,0,0,0,0],
		[0,0,0,0,0],
		[0,-1,0,0,0]])
# proportionality dependencies: 1 = P+, -1 = P-, 0 = nothing
P = np.array([[0,0,0,0,0],
		[0,0,1,0,0],
		[0,0,0,1,0],
		[0,0,0,0,1],
		[0,0,0,0,0]])
# max dependencies: 1 = equality, 0 = nothing
Max_eq = np.array([[0,0,0,0,0],
		[0,0,1,0,0],
		[0,1,0,1,0],
		[0,0,1,0,1],
		[0,0,0,1,0]])
# zero dependencies: 1 = equality, 0 = nothing
Zero_eq = np.array([[0,0,0,0,0],
		[0,0,1,0,0],
		[0,1,0,1,0],
		[0,0,1,0,1],
		[0,0,0,1,0]])


# generate all possible states
S = st.generate_all_possible_states(Q,val_domain,der_domain)
# remove the states that cannot be possible
validS = st.remove_invalid_states(S,I,P,Max_eq,Zero_eq)

# printing the valid states 
print("\t  Im  Id  Vm  Vd  Hm  Hd  Pm  Pd  Om  Od")
for key in range(validS.shape[0]):
	my_str = ''
	for i in range(10):
		if validS[key][i] >= 0:
			my_str += ' ' + str(validS[key][i]) + '  '
		else:
			my_str += str(validS[key][i]) + '  '
	print("State %2d: %s"%(key, my_str))
# ask user to input an init state
init_state = int(input('Choose an initial state from the valid states above:'))

# check if user input is valid
if init_state not in range(validS.shape[0]):
	print("Wrong input! Default state used (4)!")
	init_state = 4

# from an initial state (here init_state) generate a file in DOT in order to make it graphical
# the output is the states that are possible from transitions with different label
mapping = gr.states_to_graph(validS, init_state)

# make the state graph from the DOT file
state_graph = pydotplus.graph_from_dot_file('Graph.dot')
# write the graph as avg format
graph_name = 'State_Graph_' + str(init_state) +'.png'
state_graph.write_png(graph_name)

# printing the states of the graph
def print_states():
	print("\t  Im  Id  Vm  Vd  Hm  Hd  Pm  Pd  Om  Od")
	for key in mapping.keys():
		my_str = ''
		for i in range(10):
			if validS[key][i] >= 0:
				my_str += ' ' + str(validS[key][i]) + '  '
			else:
				my_str += str(validS[key][i]) + '  '
		print("State %2d: %s"%(mapping[key], my_str))
print_states()
print('Check "%s" for the transition graph!'%(graph_name))

########################################################################
####################### State details ##################################


# variables used for printing the description
entities = ["Inflow", "Volume", "Height", "Pressure", "Outflow"]
mag = ['zero', 'positive', 'max']
der = ['decreasing', 'constant', 'increasing']

# printing function for the given state
def print_desc(state):
	my_str = ''
	for i in range(5):
		my_str += entities[i]+': Magnitude is ' + mag[state[i*2]] + ' and it is ' + der[state[2*i + 1] + 1] + '\n'
	print(my_str)

# get the key from the value, needed to find the index in the original table(validS)
def get_key(val):
	for key in mapping.keys():
		if mapping[key] == val:
			return key

	raise -1

st = input('\nEnter state number to see description, anything else to exit:\n0 - see states again\n')
# get description until wrong input or out of range index
while( st.isdigit() and int(st) in range(1 + len(mapping))):
	if int(st) == 0:
		print_states()
	else:
		print_desc(validS[get_key(int(st))])
	st = input('\nEnter another state number to see description, anything else to exit:\n0 - see states again\n')

