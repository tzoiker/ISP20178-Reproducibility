import matplotlib
matplotlib.use('Agg')
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import pickle
from sklearn.kernel_ridge import KernelRidge

if __name__ == '__main__':
	
	(t, y, y_noisy) = pickle.load(open('../data/data.pickle', 'rb'))

	kr1 = KernelRidge(kernel='linear')
	kr2 = KernelRidge(kernel='rbf')

	kr1.fit(np.expand_dims(t,1), np.expand_dims(y_noisy,1))
	y1 = kr1.predict(np.expand_dims(t,1)).flatten()
	kr2.fit(np.expand_dims(t,1), np.expand_dims(y_noisy,1))
	y2 = kr2.predict(np.expand_dims(t,1)).flatten()

	plt.figure()
	plt.plot(t, y, '-', label='true')
	plt.plot(t, y_noisy, '.', label='noisy')
	plt.plot(t, y1, '-', label='linear')
	plt.plot(t, y2, '-', label='rbf')
	plt.title('Kernel Ridge Regression')
	plt.legend()
	plt.savefig('../latex/figs/plot.png')