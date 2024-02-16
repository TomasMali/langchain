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


record_c = Tool(
    name='record_c',
    func= endpoints.record_c,
    description="Usa questo tool quando vuoi ottenere informazioni sugli record_c. Ci sono queste colonne: Data ultimo aggiornamento stato WF (DTUWML),1° Limite Valore Accettaz. (LAV1ML),Tipo Record (TIREML),Descrizione articolo (DESCML),Codice Documento Allegato (CDDAML),Fornitore (CDCFML),Lotto Minimo (LOMIML),Profilo Ultima Manutenzione (PROFML),Codice Listino (CLISML),Articolo esterno (CDAEML),Perc. di Assorbimento (PCASML),Classe (CLASML),Quantità in Ordine (QTORML),2° Limite Valore Acc. Val.Sec. (LAV2ML2),Codice AIC articolo (CAICML),Stato processo WF (STPWML),Codice Marca (CDMAML),Codice Unità di Misura (CDUMML),Coefficiente (COEFML),Codice Ditta (CDDTML),Codice ATC articolo (CATCML),Descrizione Articolo (DSARML),1° Limite Valore Acc. Val.Sec. (LAV1ML2),Tempo Approvvigionamento (TMAPML),Flag Per Personalizzazioni      1 (FLA1ML),Lotto Riordino (LORIML),Flag Per Personalizzazioni      3 (FLA3ML),Codice Class. Gerarc. 2 (CDG2ML),Flag Per Personalizzazioni      5 (FLA5ML),1° Limite Giorni Accettaz. (LAG1ML),Imp.Min. Acquisto Val.Sec. (IMINML2),Codice Articolo (CDARML),Data Ult. Valutaz. Qualità (DTUVML),Codice Fase di Lavorazione (CDFAML),Data Immissione Rec. (DT01ML),Codice Valuta (CDVAML),Stato Assegnazione 1/2/3/4/ (STASML),Quantità Produzione Giornaliera (QPOGML),Codice Ciclo (CDCIML),Punteggio Valutaz. Qualità (PUVAML),Importo Minimo Acquisto (IMINML),2° Limite Valore Accettaz. (LAV2ML),Data Ultima Manutenzione (DTMNML),Flag eclusione processo WF (ESPWML),Codice Estensione (CTGMML),Lotto Multiplo S/N (LOMUML),Raggruppam. Listino (RGLIML),Data Ultimo Aggiornam. Rec. (DTUAML),Descrizione articolo esterno (DSAEML),Flag Per Personalizzazioni      2 (FLA2ML),Flag Per Personalizzazioni      4 (FLA4ML),Fornitore Produttore (CDFPML),Codice Class. Gerarc. 1 (CDG1ML),2° Limite Giorni Accettaz. (LAG2ML),Barcode (CBARML),Codice Distributore (CDDSML),Codice Class. Gerarc. 3 (CDG3ML)"
)



