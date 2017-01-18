import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# local imports
from conf import *

class Recpt():
	def __init__(self):
		# mid-cpt file
		self.recpt = pd.read_csv(RECPT_PATH, sep=',')
		# mappings for mid and cpt
		self.mids_key = pd.read_csv(MIDS_KEY_PATH, sep=',')
		self.cpts_key = pd.read_csv(CPTS_KEY_PATH, sep=',')

		self.occurances = None

		self.meta()

	def meta(self):
		# 165
		self.n_MID = self.recpt.MID.unique().shape[0]
		# 138
		self.n_CPT = self.recpt.CPT.unique().shape[0]

		if self.occurances is None:
			self.occurances = np.zeros((self.n_MID, self.n_CPT))
			self.populate()

		self.sparsity = float(len(self.occurances.nonzero()[0]))
		self.sparsity /= (self.occurances.shape[0] * self.occurances.shape[1])
		self.sparsity *= 100

		print str(self.n_MID) + ' members'
		print str(self.n_CPT) + ' procedures'
		print 'Sparsity: {:4.2f}%'.format(self.sparsity)

	def populate(self):
		# flagging all zero values as 1 for MID and CPT co-ordinates
		for row in self.recpt.itertuples():
			self.occurances[row.MID, row.CPT] = 1

	def learn(self):
		# To calculate similarity cosine matrix
		self.mid_cos = cosine_similarity(self.occurances)
		self.cpt_cos = cosine_similarity(self.occurances.T)

		# To fill in the mising values
        # axis=0 : sum over columns
        # axis=1 : sum over rows
		self.mid_similarity = self.mid_cos.dot(self.occurances) / np.array([np.abs(self.mid_cos).sum(axis=1)]).T
		self.cpt_similarity = self.occurances.dot(self.cpt_cos) / np.array([np.abs(self.cpt_cos).sum(axis=1)])

	def similar_procedures(self, mid, k=6):
        # -> what is argsort?
        # argsort returns the 'indices' that would sort an array
        # default sorting is ascending (lowest at the start)
        # since our indices and mapped cpt are the same, we can return only the indices

        # -> why [:-k-1:-1]
        # since argsort returns an ascending index order,
        # getting the last k terms would return the highest similar elements
		cpts = np.argsort(self.mid_similarity[mid])[:-k-1:-1]
		return self.resolve_cpts(cpts)

	def similar_procedures_via_member_behaviour(self, mid, k=6):
		cpts = np.argsort(self.cpt_similarity[mid])[:-k-1:-1]
		return self.resolve_cpts(cpts)

	def resolve_cpts(self, arr):
		for a in arr:
			print self.cpts_key.cpt.loc[a]
