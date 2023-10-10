class ObraArteDTO:
    def __init__(self, fecha, codigo, ubicacion_obra, distrito, departamento, autor, titulo_obra, medio,
                 edicion, firma, nacionalidad, ano_creacion, tecnica, observaciones_obra, medidas, estado,
                 registro_fotografico_a, registro_fotografico_b, artista, valor_comercial):
        self.fecha = fecha
        self.codigo = f"{codigo:08}"
        self.ubicacion_obra = ubicacion_obra
        self.distrito = distrito
        self.departamento = departamento
        self.autor = autor
        self.titulo_obra = titulo_obra
        self.medio = medio
        self.edicion = edicion
        self.firma = firma
        self.nacionalidad = nacionalidad
        self.ano_creacion = ano_creacion
        self.tecnica = tecnica
        self.observaciones_obra = observaciones_obra
        self.medidas = f"{medidas} cm"
        self.estado = estado
        self.registro_fotografico_a = registro_fotografico_a
        self.registro_fotografico_b = registro_fotografico_b
        self.artista = artista
        self.valor_comercial = format(valor_comercial, '.2f') 
