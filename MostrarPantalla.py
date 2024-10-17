import xml.etree.ElementTree as ET


open('Solicitud de Asistencia Técnica (respostes).xml')
ET.parse('Solicitud de Asistencia Técnica (respostes).xml')

for  in root.findall('incidencia'):
    nivelurgencia=incidencia.find('nivelurgencia').text


    print(Incidencia:{nivelurgencia},)