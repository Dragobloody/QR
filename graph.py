import numpy as np
import transitions as tr
import states as st
import queue as q

# from all valid states and the index of the state that is used as initial 
# generate a graph in DOT format

def states_to_graph(states,init_state_idx):

	# number of valid states
	num_states = states.shape[0]

	# put the states that need to be cheked if a transition exist into a queue
	states_to_check = q.Queue()
	# initial state is the first one in queue
	states_to_check.put(init_state_idx)

	# we do not want to use the same labels for the states as they appear in the
	# states vector so we map them according to their chronological encounter
	state_mapping = {}
	state_mapping[init_state_idx] = 1;
	# next state label
	state_num = 2

	# open a file for writting
	with open("Graph.dot", "w") as file:
		# Dot format syntax
		file.write("digraph state_graph {\n")

		# check all states in queue until it is empty
		while  not states_to_check.empty():
			# pop the first state in the queue
			state_idx = states_to_check.get()

			# find the states that are a valid transition
			for i in np.arange(num_states):
				if tr.valid_transition(states[state_idx], states[i]) == 1 :

					# if it is the first encounter of the transition state then add it to the
					# queue and add a new label
					if i not in state_mapping.keys():
						state_mapping[i] = state_num;
						state_num += 1;
						states_to_check.put(i)
					# write the transition as an edge in the DOT format
					file.write("	%d -> %d;\n"%(state_mapping[state_idx],state_mapping[i]))
					
		# close the Dote format syntax
		file.write("}\n")

	return state_mapping