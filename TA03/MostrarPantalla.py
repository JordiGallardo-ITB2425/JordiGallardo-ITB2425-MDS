import xml.etree.ElementTree as ET

# Cargar el archivo XML
tree = ET.parse('SolicitudAsistenciaTécnica(respostes).xml')
root = tree.getroot()

# Iterar sobre las SolicitudAsistenciaTécnica(respostes) y extraer la información
for incidencia in root.findall('incidencia'):
    # Extraer información de la persona
    persona = incidencia.find('persona')
    nombre = persona.find('nombreapellidos').text.strip()
    email = persona.find('email').text.strip()
    
    # Extraer información de la fecha
    marcatiempo = incidencia.find('fecha/marcatiempo').text.strip()
    fecha_incidencia = incidencia.find('fecha/fechaincidencia').text.strip()
    
    # Extraer información de la incidencia
    info = incidencia.find('infoincidencia')
    tipo_incidencia = info.find('tipoincidencia').text.strip()
    departamento = info.find('departamento').text.strip()
    equipo_afectado = info.find('equipoafectado').text.strip()
    descripcion = info.find('descripcionproblema').text.strip()
    urgencia = info.find('nivelurgencia').text.strip()
    acciones_previas = info.find('accionesprevias').text.strip()

    # Imprimir la información de la incidencia
    print('--- Incidencia ---')
    print(f'Nombre: {nombre}')
    print(f'Email: {email}')
    print(f'Marca de tiempo: {marcatiempo}')
    print(f'Fecha de incidencia: {fecha_incidencia}')
    print(f'Tipo de incidencia: {tipo_incidencia}')
    print(f'Departamento: {departamento}')
    print(f'Equipo afectado: {equipo_afectado}')
    print(f'Descripción del problema: {descripcion}')
    print(f'Nivel de urgencia: {urgencia}')
    print(f'Acciones previas: {acciones_previas}')
