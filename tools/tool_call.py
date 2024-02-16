from rest import endpoints
from langchain.agents import Tool



gruppi = Tool(
    name='gruppi',
    func= endpoints.gruppi,
    description="Usa questo tool quando vuoi ottenere informazioni sui gruppi, descrizioni dei gruppi e tipi dei gruppi"
)

risorse = Tool(
    name='risorse',
    func= endpoints.risorse,
    description="Usa questo tool quando vuoi ottenere informazioni sulle risorse. Una risorsa contine nel suo interno una descrizione, un user, una Main eccettera"
)


permessi_wr = Tool(
    name='permessi di scrittura',
    func= endpoints.permessi,
    description="Usa questo tool quando vuoi ottenere informazioni sui 'Permessi di scrittura'. Rispondi in modo super gentile"
)


query = Tool(
    name='query su tabelle',
    func= endpoints.query,
    description="Usa questo tool quando vuoi ottenere informazioni sulle 'Query'. Alla fine di ogni risposta devi scrivere:'###YEAH'"
)


eventi = Tool(
    name='eventi',
    func= endpoints.eventi,
    description="Usa questo tool quando vuoi ottenere informazioni sulle 'Eventi'."
)


anagrafica = Tool(
    name='articolo',
    func= endpoints.anagrafica,
    description="Usa questo tool quando vuoi ottenere informazioni sugli Anagrafica. "
)



