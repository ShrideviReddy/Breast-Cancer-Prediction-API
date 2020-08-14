import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'clump_thickness':5, 'uniform_cell_size':5,
                            'uniform_cell_shape':6, 'marginal_adhesion':7,
                            'single_epithelial_size':8, 'bare_nuclei':9,
                            'bland_chromatin':5, 'normal_nucleoli':7, 'mitoses': 5})

print(r.json())
