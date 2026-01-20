import numpy as np 
 
# Function to print the transition table 
def print_transition_table(states, symbols, transitions): 
    # Calculate the width of each column for better formatting 
    max_state_length = max(len(state) for state in states) + 2 
    max_symbol_length = max(len(symbol) for symbol in symbols) + 4 
    max_transition_length = max(len(",".join(trans)) for state in transitions.values() for trans in 
state.values()) + 2 
     
    col_width = max(max_state_length, max_transition_length, max_symbol_length) 
 
    # Header row 
    print("\n" + "Transition Table".center(col_width * (len(symbols) + 1) + len(symbols) * 3, 
"=")) 
    print("State".ljust(col_width) + " | " + " | ".join(symbol.ljust(col_width) for symbol in 
symbols)) 
    print("-" * (col_width * (len(symbols) + 1) + len(symbols) * 3)) 
 
    # Table body 
    for state in states: 
        row = [state.ljust(col_width)] 
        for symbol in symbols: 
            if state in transitions and symbol in transitions[state]: 
                row.append(",".join(sorted(transitions[state][symbol])).ljust(col_width)) 
            else: 
                row.append("-".ljust(col_width)) 
        print(" | ".join(row)) 
    print("=" * (col_width * (len(symbols) + 1) + len(symbols) * 3) + "\n") 
# Input for NFA 
num_states = int(input("Enter the number of states in the NFA: ")) 
states = ['q' + str(i) for i in range(num_states)] 
num_symbols = int(input("Enter the number of symbols: ")) 
symbols = [input(f"Enter symbol {i + 1}: ") for i in range(num_symbols)] 
# Asking for starting and accepting states 
start_state = input(f"Enter the starting state (from {states}): ") 
accepting_states = input(f"Enter the accepting states (comma separated from {states}): 
").split(',') 
# Initialize the transition dictionary for NFA 
nfa_transitions = {} 
# Input the transitions for the NFA 
for state in states: 
nfa_transitions[state] = {} 
for symbol in symbols: 
trans_states = input(f"Enter the states (comma separated) for transition from {state} on 
{symbol} (if none, leave blank): ") 
nfa_transitions[state][symbol] = trans_states.split(',') if trans_states else [] 
# Display the NFA transition table 
print("\nNFA Transition Table:") 
print_transition_table(states, symbols, nfa_transitions) 
# Function to convert NFA to DFA 
def nfa_to_dfa(nfa_transitions, states, symbols, start_state): 
    dfa_transitions = {} 
    dfa_states = [] 
 
    # Start from the user-provided initial state 
    unmarked_states = [frozenset([start_state])] 
    marked_states = [] 
 
    while unmarked_states: 
        current_dfa_state = unmarked_states.pop(0) 
        marked_states.append(current_dfa_state) 
         
        current_state_name = ",".join(sorted(current_dfa_state)) 
        dfa_transitions[current_state_name] = {} 
 
        for symbol in symbols: 
            next_states = set() 
            for nfa_state in current_dfa_state: 
                # Ensure we are using the correct state name when accessing nfa_transitions 
                if nfa_state in nfa_transitions and symbol in nfa_transitions[nfa_state]: 
                    next_states.update(nfa_transitions[nfa_state][symbol]) 
             
            next_state_frozen = frozenset(next_states) 
             
            if next_state_frozen not in marked_states and next_state_frozen not in 
unmarked_states: 
                unmarked_states.append(next_state_frozen) 
             
            dfa_transitions[current_state_name][symbol] = sorted(next_states) 
 
    return dfa_transitions, marked_states 
 
# Convert NFA to DFA 
dfa_transitions, dfa_states = nfa_to_dfa(nfa_transitions, states, symbols, start_state) 
 
# Display the DFA transition table 
print("DFA Transition Table:") 
dfa_states_names = list(dfa_transitions.keys()) 
print_transition_table(dfa_states_names, symbols, dfa_transitions) 
 
# Correct the format for DFA final states by removing empty entries and duplicates 
dfa_accepting_states = [ 
    ",".join(sorted(set(state.split(',')))) for state in dfa_states_names  
    if any(s in accepting_states for s in state.split(',')) 
] 
dfa_accepting_states = [state for state in dfa_accepting_states if state]  # Remove empty 
states if any 
 
# Print the final DFA states 
print(f"DFA Final States: {dfa_accepting_states}") 
 
# Function to find dead states based on reachability from the start state 
def find_dead_states(dfa_transitions, dfa_states_names, start_state): 
    reachable_states = set() 
    stack = [start_state] 
 
    # Perform a DFS from the starting state to find all reachable states 
    while stack: 
        current_state = stack.pop() 
        reachable_states.add(current_state) 
         
        for symbol in symbols: 
            if current_state in dfa_transitions and symbol in dfa_transitions[current_state]: 
                next_state = ",".join(dfa_transitions[current_state][symbol]) 
                if next_state and next_state not in reachable_states: 
                    stack.append(next_state) 
 
    # Dead states are those that are not reachable from the start state 
    dead_states = [state for state in dfa_states_names if state not in reachable_states] 
 
    return dead_states 
 
# Call the function to find dead states 
dead_states = find_dead_states(dfa_transitions, dfa_states_names, 
",".join(sorted(set(dfa_states_names[0].split(','))))) 
 
# Update the DFA transition table to include dead states 
for dead_state in dead_states: 
    dfa_transitions[dead_state] = {symbol: [] for symbol in symbols} 
 
# Include dead states in the DFA states list 
dfa_states_names += dead_states 
 
# Re-display the updated DFA transition table with dead states included 
print("Updated DFA Transition Table (including Dead States):") 
print_transition_table(dfa_states_names, symbols, dfa_transitions) 
 
# Output the dead states 
if dead_states: 
    print(f"Dead States: {sorted(dead_states)}") 
else: 
print("No Dead States") 
