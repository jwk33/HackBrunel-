import pickle
infile = open('road_networkSM.gpickle','rb')
new_dict = pickle.load(infile)
infile.close()