#!/usr/local/bin/python
import os
import sys
import cgi, cgitb
import StringIO
import h5py
import numpy as np
from pyplatypus import reduce
from pyplatypus import processplatypusnexus
from pyplatypus import platypusspectrum
import gviz_api

cgitb.enable()

#specify where the files are to originate from
FILEPATH = './'

def main():
    form = cgi.FieldStorage()
    keys = form.keys()
    print "Content-type: text/plain\n"
    
    if 'spectrum' in keys:
        spectrum_list = reduce.sanitize_string_input(form['spectrum'].value)
        
        background = True
        if 'rebinpercent' in keys:
            if 0. < float(form['rebinpercent'].value) < 10.:
                rebinpercent = float(form['rebinpercent'].value)
            else:
                rebinpercent = 4.
		
        red = processplatypusnexus.ProcessPlatypusNexus()
        specname = ''
        
        spectra = []
        description = [('lamda', 'number')]
        points = []
        
        for specnumber in spectrum_list:
            sn = 'PLP{0:07d}.nx.hdf'.format(int(abs(specnumber)))
            for root, dirs, files in os.walk(FILEPATH):
                if sn in files:
                    specname = os.path.join(root, sn)
                    break
			
            if not len(specname):
                print ''
                return None
                
            with h5py.File(specname, 'r') as h5data:
                spectrum = red.process(h5data)
        
            description.append((sn, 'number'))	
            spectra.append(spectrum)
            points.append(np.size(spectrum.M_spec[0], axis=1))

#        description = [('lamda', 'number'), ('I', 'number')]
#        ydata = np.log10(spectrum.M_spec[0])     
#        data = zip(spectrum.M_lambda[0], ydata)

        
			
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)
        
        json = data_table.ToJSon()
        print json
    
if __name__ == '__main__':
    main()