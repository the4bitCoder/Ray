# Ray
My second AI attempt using an obejct oriented approach.
An Example of the AI configuration is bellow 

memory = nuerons_intputs_and_weights([],[],0)
node_array = []

for i in range(0,memory.layer_length*memory.layer_num):
    node_array.append(nueron(memory.node_weigths(i),memory.node_inputs(i)))

for i in range(0,len(node_array)):
    memory.modify_node_inputs(i,node_array[i])

print(memory.node_inputs[len(memory.node_inputs)])

You can either copy and paste this into the file or remove the ''' around the one already in the file 
PLEASE NOTE: that this isn't a very stable AI and is only suitable for basic tasks; the AI configuration MUST be written in the file and AI hasn't been created in the from of a libary, I haven't even tested it as a libary.