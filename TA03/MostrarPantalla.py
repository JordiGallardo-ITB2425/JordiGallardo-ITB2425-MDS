import xml.etree.ElementTree as ET
from colorama import init, Fore, Style
init(autoreset=True)

# Cargar el archivo XML
tree = ET.parse('SolicitudAsistenciaTécnica(respostes).xml')
root = tree.getroot()

# Iterar sobre las SolicitudAsistenciaTécnica(respostes) y extraer la información
for incidencia in root.findall('incidencia'):
    
    # Extraer información de la incidencia
    info = incidencia.find('infoincidencia')
    tipo_incidencia = info.find('tipoincidencia').text.strip()
    departamento = info.find('departamento').text.strip()
    equipo_afectado = info.find('equipoafectado').text.strip()
    descripcion = info.find('descripcionproblema').text.strip()
    urgencia = info.find('nivelurgencia').text.strip()
    acciones_previas = info.find('accionesprevias').text.strip()

    # Imprimir la información de la incidencia
    print(f'{Fore.RED}--- Incidencia ---')
    print(f'Nivel de urgencia: {urgencia}')
    print(f'Departamento: {departamento}')
    print(f'Equipo afectado: {equipo_afectado}')
    print(f'Descripción del problema: {descripcion}')
    print(f'Acciones previas: {acciones_previas}')
    print()