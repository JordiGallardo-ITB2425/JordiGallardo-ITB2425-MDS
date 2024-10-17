import xml.etree.ElementTree as ET

# Cargar el archivo XML
tree = ET.parse('SolicitudAsistenciaTécnica(respostes).xml')
root = tree.getroot()

# Iterar sobre cada incidencia
for incidencia in root.findall('incidencia'):
    # Obtener información de la incidencia
    nivelurgencia = infoincidencia.find('nivelurgencia').text.strip()
    infoincidencia = incidencia.find('infoincidencia')
    tipoincidencia = infoincidencia.find('tipoincidencia').text.strip()
    departamento = infoincidencia.find('departamento').text.strip()
    equipoafectado = infoincidencia.find('equipoafectado').text.strip()
    descripcionproblema = infoincidencia.find('descripcionproblema').text.strip()
    accionesprevias = infoincidencia.find('accionesprevias').text.strip()

    # Imprimir la información de la incidencia
    print(f'Nivel de urgencia: {nivelurgencia}')
    print(f'Tipo de incidencia: {tipoincidencia}')
    print(f'Departamento: {departamento}')
    print(f'Equipo afectado: {equipoafectado}')
    print(f'Descripción del problema: {descripcionproblema}')
    print(f'Acciones previas: {accionesprevias}')

