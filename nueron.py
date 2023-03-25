class nueron:
    def __init__(self,node_weigths, node_inputs):
        self.node_weigths = node_weigths
        self.node_inputs = node_inputs

    def run(self):
        output = 0
        for i in range(len(self.node_inputs)):
            output = output + (self.node_inputs[i]*self.node_weigths[i])
        import math
        output = math.tan(output)
        return output 
    
    def modify(self,node_weigths,node_inputs):
        self.node_weigths = node_weigths
        self.node_inputs = node_inputs

class nuerons_intputs_and_weights:
    def __init__(self,network_weigths,network_inputs,layer_num):
        self.network_weigths = network_weigths
        self.network_inputs = network_inputs
        self.layer_num = layer_num
        self.layer_length = len(network_inputs) / layer_num # modify this
    
    def node_inputs(self,node): 
        returnarray = []
        layer_inhabiting = node // self.layer_length
        layer_before = layer_inhabiting - 1
        for i in range(0,self.layer_length):
            returnarray[i] = layer_before + 1
        return returnarray
    
    def node_weigths(self,node):
        returnarray = []
        node_place = len(self.network_weigths) / len(self.layer_length*self.layer_num)
        node_place = node_place*node
        for i in range(node_place-self.layer_length-1,node_place):
            returnarray[i] = self.network_weigths[i]
        return returnarray

    def modify_node_inputs(sel,i,node_output):
        self.network_inputs[i] = node_output
    
class AI_learn:
    def __init__(self,result,ouput,network_weights):
        self.result = result # result contains a boolean whether or not the nueral network generated a correct respose
        self.output = ouput # the answer that the nueral network gave
        self.network_weigths = network_weights
      
    def learn(self):
        print("This isn't working yet")
        # COMING SOON

# main AI (you can create your own bellow) 
# For example     
'''memory = nuerons_intputs_and_weights([],[],0)
node_array = []

for i in range(0,memory.layer_length*memory.layer_num):
    node_array.append(nueron(memory.node_weigths(i),memory.node_inputs(i)))

for i in range(0,len(node_array)):
    memory.modify_node_inputs(i,node_array[i])

print(memory.node_inputs[len(memory.node_inputs)])'''