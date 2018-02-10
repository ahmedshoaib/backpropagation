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
			while n > 0 :
				training_x.append([1.0])
				n -= 1
		else:
			word = line.split()
			training_y.extend([float(word.pop(no_attr))])
			for attr in word:
				training_x[counter].extend([float(attr)])
			counter += 1
	bin = training_x.pop(counter)          #removes the extra sample created in training_x
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
	
	
	
	
	
def Back_Prop(alpha,hidden_no,error_threshold,omega,out_no):   #implements back propagation algorithm
	w1=[]      # weight list of first layer
	w2 =[]    # weight list of second layer
	training_x = []   #training sample : x
	training_y =[]     #training sample : y
	no_attr = get_Data(training_x,training_y)
	#print(training_x,"\n",training_y,"\n",no_attr,"\n")
	
	initialize_Weights(w1,w2,no_attr,hidden_no,omega,out_no)
	
	# Forward Pass :
	#input to hidden layer
	sample_no = 0 
	E = 0
	for x in training_x:
		
	
	
	
	
	
	
def main():
	alpha  = float(input("Enter learning rate : "))   #(0.0001  is good)
	if (alpha <= 1 and alpha > 0):
		hidden_no = int(input("\nEnter number of neurons in hidden layer : "))
		out_no = int(input("\nEnter number of neurons in output layer : "))
		error_threshold = float(input("\nEnter threshold error : "))
		omega = float(input("\nEnter initial weight for all : "))
		Back_Prop(alpha,hidden_no,error_threshold,omega,out_no)	
	else:
		print("Wrong learning rate ")

main()