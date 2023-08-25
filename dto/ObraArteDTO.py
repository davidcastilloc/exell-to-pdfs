class ObraArteDTO:
    def __init__(self, fecha, codigo, ubicacion_obra, distrito, departamento, autor, titulo_obra, medio,
                 tiraje, nacionalidad, ano_creacion, tecnica, observaciones_obra, medidas, estado,
                 registro_fotografico, artista, valor_comercial):
        self.fecha = fecha
        self.codigo = codigo
        self.ubicacion_obra = ubicacion_obra
        self.distrito = distrito
        self.departamento = departamento
        self.autor = autor
        self.titulo_obra = titulo_obra
        self.medio = medio
        self.tiraje = tiraje
        self.nacionalidad = nacionalidad
        self.ano_creacion = ano_creacion
        self.tecnica = tecnica
        self.observaciones_obra = observaciones_obra
        self.medidas = medidas
        self.estado = estado
        self.registro_fotografico = registro_fotografico
        self.artista = artista
        self.valor_comercial = valor_comercial

# Ejemplo de uso:
obra_dto = ObraArteDTO(
    fecha="Fecha de la obra",
    codigo="Código de la obra",
    ubicacion_obra="Ubicación de la obra",
    distrito="Distrito",
    departamento="Departamento",
    autor="Autor de la obra",
    titulo_obra="Título de la obra",
    medio="Medio",
    tiraje="Tiraje",
    nacionalidad="Nacionalidad",
    ano_creacion="Año de creación",
    tecnica="Técnica",
    observaciones_obra="Observaciones de la obra",
    medidas="Medidas",
    estado="Estado",
    registro_fotografico="Registro fotográfico",
    artista="Artista",
    valor_comercial="Valor comercial"
)