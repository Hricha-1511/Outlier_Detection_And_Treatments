{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "60f38eaa",
   "metadata": {},
   "source": [
    "# Finding an outlier in a Dataset using z-score"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b332a14",
   "metadata": {},
   "source": [
    "#what is an outlier \n",
    "An outlier is a data point in a dataset that is distant from all other observations.\n",
    "A data point that lies outside the overall distribution of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fdc7bd2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt \n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "023d30b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5522071",
   "metadata": {},
   "source": [
    "# Detecting outliers using z-score\n",
    "formula for z-score = (Observation - Mean)/standard Deviation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "55ba0e37",
   "metadata": {},
   "outputs": [],
   "source": [
    "outliers=[]\n",
    "def detect_outliers(data):\n",
    "    \n",
    "    threshold=3\n",
    "    mean = np.mean(data)\n",
    "    std =np.std(data)\n",
    "    \n",
    "    \n",
    "    for i in data:\n",
    "        z_score= (i - mean)/std \n",
    "        if np.abs(z_score) > threshold:\n",
    "            outliers.append(i)\n",
    "    return outliers\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c5626e39",
   "metadata": {},
   "outputs": [],
   "source": [
    "outlier_pt=detect_outliers(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0b276bcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[102, 107, 108]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "outlier_pt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "069b237c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10,\n",
       " 10,\n",
       " 10,\n",
       " 10,\n",
       " 10,\n",
       " 11,\n",
       " 11,\n",
       " 12,\n",
       " 12,\n",
       " 12,\n",
       " 12,\n",
       " 12,\n",
       " 12,\n",
       " 12,\n",
       " 13,\n",
       " 13,\n",
       " 13,\n",
       " 13,\n",
       " 14,\n",
       " 14,\n",
       " 14,\n",
       " 14,\n",
       " 14,\n",
       " 14,\n",
       " 15,\n",
       " 15,\n",
       " 15,\n",
       " 15,\n",
       " 15,\n",
       " 17,\n",
       " 19,\n",
       " 102,\n",
       " 107,\n",
       " 108]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Perform all the steps of IQR\n",
    "sorted(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1a632e53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12.0 15.0\n"
     ]
    }
   ],
   "source": [
    "quantile1, quantile3= np.percentile(dataset,[25,75])\n",
    "print(quantile1,quantile3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f04ebb3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.0\n"
     ]
    }
   ],
   "source": [
    "## Find the IQR\n",
    "iqr_value=quantile3-quantile1\n",
    "print(iqr_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d6899871",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Find the lower bound value and the higher bound value\n",
    "\n",
    "lower_bound_val = quantile1 -(1.5 * iqr_value) \n",
    "upper_bound_val = quantile3 +(1.5 * iqr_value) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2d17a9b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7.5 19.5\n"
     ]
    }
   ],
   "source": [
    "print(lower_bound_val,upper_bound_val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38d8bcbc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
