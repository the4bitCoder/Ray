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
    def __init__(self,network_weigths, network_inputs,layer_num):
        self.network_weigths = network_weigths
        self.network_inputs = network_inputs
        self.layer_num = layer_num
        self.layer_length = len(network_inputs) / layer_num
    
    def node_stuff(self,node):
        returnarray = []
        layer_inhabiting = node // self.layer_length
        layer_before = layer_inhabiting - 1
        for i in range(0,self.layer_length):
            

