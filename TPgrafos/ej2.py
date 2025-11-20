from graph import Graph

ambientes = Graph()
ambientes.insert_vertex("cocina")
ambientes.insert_vertex("comedor")
ambientes.insert_vertex("cochera")
ambientes.insert_vertex("quincho")
ambientes.insert_vertex("baño1")
ambientes.insert_vertex("baño2")
ambientes.insert_vertex("habitacion1")
ambientes.insert_vertex("habitacion2")
ambientes.insert_vertex("sala")
ambientes.insert_vertex("terraza")
ambientes.insert_vertex("patio")

ambientes.insert_edge("patio", "comedor", 2)

# cocina
ambientes.insert_edge("cocina", "comedor", 3)
ambientes.insert_edge("cocina", "cochera", 4)
ambientes.insert_edge("cocina", "baño1", 2)

# cochera
ambientes.insert_edge("cochera", "patio", 3)
ambientes.insert_edge("cochera", "quincho", 5)
ambientes.insert_edge("cochera", "habitacion2", 4)

# quincho
ambientes.insert_edge("quincho", "comedor", 4)
ambientes.insert_edge("quincho", "terraza", 6)

# terraza
ambientes.insert_edge("terraza", "patio", 3)
ambientes.insert_edge("terraza", "habitacion1", 4)

# sala
ambientes.insert_edge("comedor", "sala", 2)
ambientes.insert_edge("sala", "patio", 2)
ambientes.insert_edge("sala", "habitacion1", 3)
ambientes.insert_edge("sala", "habitacion2", 3)
ambientes.insert_edge("sala", "terraza", 3)

# baños y habitaciones
ambientes.insert_edge("baño1", "patio", 1)
ambientes.insert_edge("baño1", "baño2", 1)
ambientes.insert_edge("baño2", "habitacion1", 2)
ambientes.insert_edge("baño2", "habitacion2", 2)

exp_min,cable=ambientes.kruskal("baño1",True)
print(f"arbol de expansion minima: {exp_min}")
print()
print(f"metros de cable: {cable}")
print()
print(ambientes.dijkstra("habitacion1","sala"))