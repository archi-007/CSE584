# Midterm Project
> Archisman Ghosh (apg6127@psu.edu)
> 
Steps to reproduce results.
### **Installation**

```shell
pip install -r requirements.txt
```
### **Dataset**.
Generate ($x_i$)
```shell
python3 truncated.py
```
Run `dataset.ipynb` to generate the completions ($x_j$).

### **Model**
Run `main.ipynb` to generate the LSTM-based classifier results, and `main_bert.ipynb` to generate classifier results based on BERT. 
