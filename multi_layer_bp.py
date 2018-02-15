import numpy as np
def get_Data(training_x,training_y):            #extracts training data from input file and returns no. of training samples
	inp = input("enter training file name :\n")
	input_file = open(inp,'r')
	flag = 0
	counter = 0
	for line in input_file:
		if(flag == 0):
			no_attr = int(line)
			flag += 1
			n = no_attr
		else:
			word = line.split()
			count = 1
			training_y.append([])
			training_x.append([1.0])
			for attr in word:
				if(count <= no_attr):
					training_x[counter].extend([float(attr)])
				else:
					training_y[counter].extend([float(attr)])
				count +=1
			counter += 1

	return no_attr
	
def initialize_Weights(w1,w2,no_attr,hidden_no,omega,out_no):
	for i in range(hidden_no): 
		w1.append([]) 
		for j in range(no_attr+1):
			w1[i].extend([omega])
	for i in range(out_no): 
		w2.append([])
		for j in range(hidden_no+1):
			w2[i].extend([omega])
			
def sigmoid(x):
    return (float(1 / (1 + np.exp(-x))))

def exp_value(input_list,weight_list):
	exp_list = []
	for o_node in weight_list:
		h = 0.0
		for i in range(len(o_node)):
			h += (input_list[i]*o_node[i])
		exp_list.extend([sigmoid(h)])
	
	return exp_list

def Back_Prop(alpha,hidden_no,error_threshold,omega):   #implements back propagation algorithm
	w1=[]      # weight list of first layer
	w2 =[]    # weight list of second layer
	training_x = []   #training sample : x
	training_y =[]     #training sample : y
	no_attr = get_Data(training_x,training_y)
	out_no = len(training_y[0])
	initialize_Weights(w1,w2,no_attr,hidden_no,omega,out_no)
	Eprev = 0
	E=100000
	
	while ( abs(E-Eprev) > error_threshold):
		print("training : ",abs(E-Eprev))
		Eprev = E
		E = 0       # error value
		
		for i in range(len(training_x)):   #each training sample
			h = [1.0]           #output value list of layer1 add h0
			d = []     #output value list of layer2
			
			# Forward Pass :
			#input to hidden layer
		
	
			h.extend(exp_value(training_x[i],w1))    #calculate expected value and then feeds activation function and returns list with expected values of layer 1
			d.extend(exp_value(h,w2))
			
			#h2 contains final outputs
		
			#Backward Pass:
		
			e=[]
			for j in range(len(d)):
				e.extend([training_y[i][j] - d[j]])
			local_g1 =[]    #local gradient lists for both layers
			local_g2 =[]
			j = 0
			temp = 0
			
			for er in e:
				temp += (er*er)
				local_g2.extend([er*d[j]*(1-d[j])])
				j += 1
			temp = temp/2
			
			E += temp
			for j in range(len(w1)) :
				temp = 0 
				for k in range(len(w2)):
					temp += (w2[k][j+1] * local_g2[k])
				local_g1.extend([temp])
			

		
			# Updation:
			for j in range(len(w2)):
				for k in range(len(h)): #update weights of layer 1
					w2[j][k] = w2[j][k] + (alpha*local_g2[j]*h[k])
			for j in range(len(w1)):   #update weights of layer 1
				for k in range(len(training_x[i])):
					w1[j][k] = w1[j][k] + (alpha*local_g1[j]*training_x[i][k])
			
		
	'''		
		print("\nlocal_g1 : ",local_g1,"\nlocal_g2 : ",local_g2,)
		if(Eprev != 100):
			break
		
	'''

	while(1):
		print("enter test sample\n")
		x=[1.0]
		m=[1.0]
		n=[]
		for j in range(len(training_x[0])-1):
			x.extend([float(input("\nenter attribute : "))])
		m.extend(exp_value(x,w1))    #calculate expected value and then feeds activation function and returns list with expected values of layer 1
		n.extend(exp_value(m,w2))
#		max_value = max(n)
#		max_index = n.index(max_value)
		print("\n n : ",n)
		

def main():
	alpha  = float(input("Enter learning rate : "))   #(0.0001  is good)
	if (alpha <= 1 and alpha > 0):
		hidden_no = int(input("\nEnter number of neurons in hidden layer : "))
		error_threshold = float(input("\nEnter threshold error : "))
		omega = float(input("\nEnter initial weight for all : "))
		Back_Prop(alpha,hidden_no,error_threshold,omega)	
	else:
		print("Wrong learning rate ")

main()