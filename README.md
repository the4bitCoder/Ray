# Ray
My second AI attempt using an object oriented approach.
An example of the AI configuration is below :

```
memory = nuerons_intputs_and_weights([],[],0)
node_array = []

for i in range(0,memory.layer_length*memory.layer_num):
    for i in range(0,len(node_array)):
        memory.modify_node_inputs(i,node_array[i])
    node_array.append(nueron(memory.node_weigths(i),memory.node_inputs(i)))

for i in range(len(memory.node_inputs)-memory.layer_length-1,len(memory.node_inputs)):
	print(memory.node_inputs[i])
```

You can either copy and paste this into the file or remove the ''' around the one already in the file 
PLEASE NOTE: that this isn't a very stable AI and is only suitable for basic tasks; the AI configuration MUST be written in the file and AI hasn't been created in the from of a libary, I haven't even tested it as a libary.

# How it works
First of all you need to iniate the nueral netowrk by defining the values for the weigths, inputs and number of layers.
```
memory = nuerons_inputs_and_weights([],[],0)
```
In this example the first set of [] represents the array of the weights in the network;
the second [] represents the inputs into the nueral network;
the 0 holds the value of the number of layers in the network (bear in mind it will return to an error if it is set to 0 so you need to change it).


```
node_array = []
```
The node_array holds the values that the nuerons return.

```
for i in range(0,memory.layer_length*memory.layer_num):
    for i in range(0,len(node_array)):
        memory.modify_node_inputs(i,node_array[i])
    node_array.append(nueron(memory.node_weigths(i),memory.node_inputs(i)))
```
This then inserts all the values from the node_array into the memory and then runs the network and gets the result of the each node in the network
```
for i in range(len(memory.node_inputs)-memory.layer_length-1,len(memory.node_inputs)):
	print(memory.node_inputs[i])
```
Outputs the last values from the last layer of nuerons in the network
