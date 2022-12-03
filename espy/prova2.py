class CSVFile():
    
    def __init__(self, name):
        self.name=name
        try:
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            print('Errore! di tipo "{}"'.format(e))

    def get_data(self):
        data=[]
        file=open(self.name,'r') 
        for line in file:
            elements=line.split(',')
            if elements[0] != 'Date':
                elements[-1]=elements[-1].strip()
                data.append(elements)
        file.close()
        return (data)

class NumericalCSVFile(CSVFile):

    def get_data(self):
        stringa=super.get_data()
        
        
        

mio_file = CSVFile(name='shampoo_sales.txt')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))