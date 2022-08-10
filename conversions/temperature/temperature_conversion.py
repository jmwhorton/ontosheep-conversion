def ensureCelsius(measurement_dict):
    if measurement_dict['unitlabel'] == 'http://purl.obolibrary.org/obo/UO_0000027':
        return measurement_dict
    elif measurement_dict['unitlabel'] == 'http://purl.obolibrary.org/obo/UO_0000195':
        degreeF = float(measurement_dict['value'])
        degreeC = round((degreeF - 32) * 5 / 9, 1) 
        measurement_dict['value'] = degreeC
        measurement_dict['unitlabel'] = 'http://purl.obolibrary.org/obo/UO_0000027'
        return measurement_dict
