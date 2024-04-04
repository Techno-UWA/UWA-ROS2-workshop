import numpy as np
import pickle

class DataLoader:
    def __load_pickle_file(filename):
        with open(filename, 'rb') as f:
            dict = pickle.load(f, encoding='bytes')
            return dict  

    def get_data(filename_prefix, height=32, width=32, Nchannels=3):
          
        batch_no = range(1, 5+1)  # the batch numbers start at 1
	    # Read all the batch pickle files
        batch = [DataLoader.__load_pickle_file(filename_prefix+'_'+str(b)) for b in batch_no]

        batch_size = [len(batch[i][b'labels']) for i in range(5)]
        dataset_size = np.sum(batch_size)

        X = np.zeros((dataset_size, height, width, Nchannels), dtype='float32')
        y = np.zeros(dataset_size, dtype='uint8')
        loc = 0
        for i in range(5):
            X[loc:(loc+batch_size[i])] = np.rollaxis(
		    np.reshape(batch[i][b'data'], (-1,Nchannels,height,width)), 1, 4)
        y[loc:(loc+batch_size[i])] = batch[i][b'labels']
        loc += batch_size[i]
        
        return X/255, y
