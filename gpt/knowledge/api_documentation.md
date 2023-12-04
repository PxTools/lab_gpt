# API dokumentasjon 

- Ved å bytte ut "no" med "en" i adressen, får du engelsk versjon av datasettene. 

- Enkelte dager vil det være høy belastning de første minuttene etter at nye tall publiseres kl. 8.00. Med
mindre du har behov for det, unngå tidsrommet 07.55 – 08.15. 

## Søk etter data: ( "operationId": "GetTableDataByPost", )
Alle spørringer består av objektet: {"query" :[ { … } ] }

Filtre gjør at du kun får det du ønsker fra statistikkbanktabellen. 

## item 
- gir enkeltverdier i en liste 
- f.eks. ["2013", "2014"] 
- - Dette eksempelet filtrerer på alle måneder i årene 2013 og 2014. 
 > "code": "Tid",
> "selection":{
> "filter:"item",
> "values": ["2013", "2017M02", "2014]

## all
- valg med jokertegn
- f.eks.: Bare "*" gir alle verdier. "2019*" gir alle verdier som begynner på 2019. "*M12" i en månedstabell gir alle desember for hvert år.
- Dette eksempelet filtrerer på alle måneder i årene 2017, 2018 og 2019. 
 > "code": "Tid",
> "selection":{
> "filter:"all",
> "values": ["2017M*", "2018M*", "2019M*"]


## top
- velger et antall av de nyeste eller første verdiene.
 - Dette eksempelet henter de siste / nyeste 13 verdiene. 
 > "code": "Tid",
> "selection":{
> "filter:"top",
> "values": ["13"]

### Spørre etter oppdaterte tall
Med filtrene all og top kan en få til rullerende spørring på tid. Da kan du i framtiden kan bruke samme spørring til å hente oppdaterte tall. Legger du til et tidspunkt i framtiden med "filter": "item" vil du få feilmelding.

## Naviger med URL
- Alle tabeller i Statistikkbanken kjennetegnes ved et 5-sifret tabellnummer.

- Har du nummeret for den aktuelle tabellen, anbefaler vi å benytte URL på formen: https://data.ssb.no/api/v0/no/table/(5-sifret tabellnummer) http GET viser tabellens metadata som JSON. Dette er den samme URL-en som en POST-er spørringen mot, f.eks. med programmet cURL.
>  Eksempel: https://data.ssb.no/api/v0/no/table/11000

###  Hierarki

- https://data.ssb.no/api/v0/no/table/ henter hovedemner i JSON-format fra emnehierarkiet. Her er alle emnene i SSB sitt api: 
> [{"id" : "al" : "type" : "l" : "text" : "Arbeid og lønn"}, {"id" : "bf" : "type" : "l" : "text" : "Bank og finansmarked"}, {"id" : "be" : "type" : "l" : "text" : "Befolkning"}, {"id" : "bb" : "type" : "l" : "text" : "Bygg, bolig og eiendom"}, {"id" : "ei" : "type" : "l" : "text" : "Energi og industri"}, {"id" : "he" : "type" : "l" : "text" : "Helse"}, {"id" : "if" : "type" : "l" : "text" : "Inntekt og forbruk"}, {"id" : "in" : "type" : "l" : "text" : "Innvandring og innvandrere"}, {"id" : "js" : "type" : "l" : "text" : "Jord, skog, jakt og fiskeri"}, {"id" : "kf" : "type" : "l" : "text" : "Kultur og fritid"}, {"id" : "nk" : "type" : "l" : "text" : "Nasjonalregnskap og konjunkturer"}, {"id" : "nm" : "type" : "l" : "text" : "Natur og miljø"}, {"id" : "os" : "type" : "l" : "text" : "Offentlig sektor"}, 7 {"id" : "pp" : "type" : "l" : "text" : "Priser og prisindekser"}, {"id" : "sk" : "type" : "l" : "text" : "Sosiale forhold og kriminalitet"}, {"id" : "sv" : "type" : "l" : "text" : "Svalbard"}, {"id" : "ti" : "type" : "l" : "text" : "Teknologi og innovasjon"}, {"id" : "tr" : "type" : "l" : "text" : "Transport og reiseliv"}, {"id" : "ud" : "type" : "l" : "text" : "Utdanning"}, {"id" : "ut" : "type" : "l" : "text" : "Utenriksøkonomi"}, {"id" : "va" : "type" : "l" : "text" : "Valg"}, {"id" : "vt" : "type" : "l" : "text" : "Varehandel og tjenesteyting"}, {"id" : "vf" : "type" : "l" : "text" : "Virksomheter, foretak og regnskap"}]

- Generelt er strukturen: emne – underemne – statistikk – tabell. Statistikker med mange tabeller kan i tillegg ha ett eller to nivåer mellom statistikk og tabell. https://data.ssb.no/api/v0/no/table/be lister alle underemner til Befolkning. Vær oppmerksom på at statistikker kan plasseres under flere emner og underemner. Dessverre skiller ikke API-et mellom statistikkers primær- og sekundærplassering. En og samme tabell kan altså finnes under flere adresser. Blant annet er alle tabeller under emne-Idene "in" (innvandring) og "sv" (Svalbard) også plassert under andre emner. POST mot alle slike adresser vil fungere. En full utlisting av statistikkenes emneplassering og kortnavn som XML finner du på https://www.ssb.no/xp/_/service/mimir/subjectStructurStatistics.

- URL på kortformen med tabellnummer: https://data.ssb.no/api/v0/no/table/(5-sifret tabellnummer) er over tid mer stabil, enn URL på formen: https://data.ssb.no/api/v0/no/table/(emne)/(underemner)/(statistikk) eller (undernivå) /(tabellnavn). 
- Dette er fordi statistikker kan bli flyttet eller slått sammen i emnestrukturen på ssb.no, eller selve emnestrukturen kan bli endret. På samme måte som for tabellnummer er det også mulig bruke tabellnavn direkte etter table/, uten sti. 
- PxWeb benyttes av flere land. Dette er årsaken til den litt forvirrende blandingen av Tableid/tabellnavn og tabellnummer.
- 
### "type" i navigasjonen er enten:
- "l" - undernivå
- "t" - tabell

Eksempel fra https://data.ssb.no/api/v0/no/table/be/be02/folkfram :
> { id: "Framskr2018T2", type: "t", text: "11668: Framskrevet folkemengde 1. januar, etter kjønn og alder, i 9 alternativer (K) (B) 2018 - 2040", updated: "2018-06-26T08:00:00" },

 For type "t" betyr de ulike taggene: 
 - "id" : tabellnavn (det interne navnet på tabellen i vår database)
 - "type" : t = tabell
 - "text" : tabelltittel (5-sifret tabellnummer + beskrivelse av innholdet)
 - Vær oppmerksom på at det kan være undernivåer som Avslutta tidsserier på samme nivå som du finner tabeller. Av Statistikkbankens nær 7000 tabeller er rundt 2600 avslutta.




 


## Utformater – "response": {…}
API-et kan gi resultatet i 6 formater: 
- json-stat2 versjon 2 . Mer brukervennlig enn v.1. 
- json-stat versjon 1.2. 
- csv2 (pivotvennlig kommaseparert) 
- csv3 (likt CSV2, men med koder i stedet. Det er dermed uten øæå, spesialtegn etc.) 
-  xlsx (Excel)
- csv (utdatert)

JSON-stat2, csv2 og csv3 er nye formater fra 2019. Vi anbefaler disse framfor de tidligere csv og JSONstat. Det gamle ‘csv’ har klare svakheter. Ved uttrekk opp mot 800.000 celler har versjon 1 av JSONstat og csv2 problemer. For prodssuksjonsløsninger anbefales JSON-stat v2 og CSV2 vil være mindre robust enn CSV3. Desimaltegn er . (punktum) for alle språk og alle formater. Unntaket er Excel på norsk der desimaltegnet er , komma.


## Søk tabeller med parameter ?query

Parameteren ?query i URL – søker i utgangspunktet variabler og titler. Søket er case-insensitivt. Mellomrom gir logisk AND. Filteret "title" begrenser søket til tittelfeltet. Det er også mulig å søke i andre felt ved å angi det direkte med kolon, f.eks. published:

Eksempler: 
-  Søk etter verdi-teksten "kakemiks" i alle tabeller https://data.ssb.no/api/v0/no/table/?query=kakemiks 
- Søk med Tabellid for å finne tabellnummer: https://data.ssb.no/api/v0/no/table/?query=FolkFramT8 
- Søk tabeller publisert på en spesiell dato eller intervall (dato kan være fram i tid) https://data.ssb.no/api/v0/no/table/?query=published:20180504* 
-  data.ssb.no/api/v0/no/table/?query=published:[20190301 TO 20190604*] 
- Søk med tabellnummer i tittel for å finne oppdateringsdato: https://data.ssb.no/api/v0/no/table/?query=title:03013 Søk alle tabeller innen emne be (befolkning) som har verdien "Hattfjelldal" https://data.ssb.no/api/v0/no/table/be/?query=hattfjelldal 
- Alle titler med ordene "trend" og/AND som begynner på "anlegg", (trunkeringstegn *) https://data.ssb.no/api/v0/no/table/?query=title:trend anlegg* 
- Søk etter "varenummer" og "HS" mindre enn 5 ord fra hverandre, (nærhetsoperator ~) https://data.ssb.no/api/v0/no/table/?query="varenummer hs" ~5 
- Søk etter ikke avslutta bydelstabeller (B) under området Befolkning. Merk \ foran ( og ) https://data.ssb.no/api/v0/no/table/be/?query=\(B\) NOT avslutta&filter=title 
- List alle tabeller under alle emner https://data.ssb.no/api/v0/no/table/?query=*&filter=*


Samme tabell kan som nevnt være plassert på flere emner. Søket vil da returnere den samme tabellen flere ganger, men med ulik url. Merk at mellomrom kodes i url som %20. Tegnene: " ( ) [ og ] vil bli kodet (escape) i url som hhv. %22, %28, %29, %5B, og %5D.


## Metadata for tabellen
Metadataene består av en tittel "title" samt en liste over variabler for tabellen. Variabelobjektene, har fire egenskaper:
- Kode (code)
- Navn (text) 
- Eliminering (elimination) 
- Tid (time)


Et variabelobjekt inneholder to lister, en med koder (‘values’) og en med presentasjonstekster (‘valueTexts’)

 **Eksempel fra tabell https://data.ssb.no/api/v0/no/table/11172:**
> {"title":"11172: Framskrevet forventet levealder, etter kjønn, alder, alternativ, statistikkvariabel og år","variables":[{"code":"Kjonn","text":"kjønn","values":["0","1","2"],"valueTexts":["Begge kjønn","Menn","Kvinner"],"elimination":true},{"code":"Alder","text":"alder","values":["000","001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025","026","027","028","029","030","031","032","033","034","035","036","037","038","039","040","041","042","043","044","045","046","047","048","049","050","051","052","053","054","055","056","057","058","059","060","061","062","063","064","065","066","067","068","069","070","071","072","073","074","075","076","077","078","079","080","081","082","083","084","085","086","087","088","089","090","091","092","093","094","095","096","097","098","099","100","101","102","103","104","105+"],"valueTexts":["0 år","1 år","2 år","3 år","4 år","5 år","6 år","7 år","8 år","9 år","10 år","11 år","12 år","13 år","14 år","15 år","16 år","17 år","18 år","19 år","20 år","21 år","22 år","23 år","24 år","25 år","26 år","27 år","28 år","29 år","30 år","31 år","32 år","33 år","34 år","35 år","36 år","37 år","38 år","39 år","40 år","41 år","42 år","43 år","44 år","45 år","46 år","47 år","48 år","49 år","50 år","51 år","52 år","53 år","54 år","55 år","56 år","57 år","58 år","59 år","60 år","61 år","62 år","63 år","64 år","65 år","66 år","67 år","68 år","69 år","70 år","71 år","72 år","73 år","74 år","75 år","76 år","77 år","78 år","79 år","80 år","81 år","82 år","83 år","84 år","85 år","86 år","87 år","88 år","89 år","90 år","91 år","92 år","93 år","94 år","95 år","96 år","97 år","98 år","99 år","100 år","101 år","102 år","103 år","104 år","105 år eller eldre"]},{"code":"Framskriv","text":"alternativ","values":["M","L","H"],"valueTexts":["Middels levealder","Lav levealder","Høy levealder"]},{"code":"ContentsCode","text":"statistikkvariabel","values":["ForventetLevealder"],"valueTexts":["Forventet levealder"]},{"code":"Tid","text":"år","values":["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2036","2037","2038","2039","2040","2041","2042","2043","2044","2045","2046","2047","2048","2049","2050","2051","2052","2053","2054","2055","2056","2057","2058","2059","2060","2061","2062","2063","2064","2065","2066","2067","2068","2069","2070","2071","2072","2073","2074","2075","2076","2077","2078","2079","2080","2081","2082","2083","2084","2085","2086","2087","2088","2089","2090","2091","2092","2093","2094","2095","2096","2097","2098","2099","2100"],"valueTexts":["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2036","2037","2038","2039","2040","2041","2042","2043","2044","2045","2046","2047","2048","2049","2050","2051","2052","2053","2054","2055","2056","2057","2058","2059","2060","2061","2062","2063","2064","2065","2066","2067","2068","2069","2070","2071","2072","2073","2074","2075","2076","2077","2078","2079","2080","2081","2082","2083","2084","2085","2086","2087","2088","2089","2090","2091","2092","2093","2094","2095","2096","2097","2098","2099","2100"],"time":true}]}



### Eliminasjon
En variabel kan tas helt vekk fra spørringen. Da vil resultatet variere ettersom variabelen er eliminerbar eller ikke.
1.  Er variabelen eliminerbar (true) vises: 
	-  enten en elimineringsverdi, vanligvis summen («Begge kjønn» i eksempelet over) 
	- eller så aggregeres samtlige verdier til en.
2. Er variabelen ikke eliminerbar (false), returneres alle enkeltverdiene for variabelen. Tid er ikke eliminerbar. Tas Tid vekk fra spørringen, får du hele tidsserien inkl. nye tidsperioder. Dette er en teknikk som blir brukt i koden til «API-spørring for denne tabellen» når du velger hele tidsserien. En tom spørring med bare [ ] vil altså fungere, men API-et forsøker å eliminere de variablene, som det ikke er valgt verdier for. En tom spørring mot tabell på kommunenivå vil typisk bare gi tall for «Hele landet» (summen av alle kommunene), med alle tidsperioder.


### Aggregeringer, grupperinger, kommunereformen
Grupperinger og aggregeringer, som aldersgrupper, vises (dessverre) ikke i API-ets metadata. Men disse er synlige du har laget en tabell i Statistikkbanken og velger:
**agg:**
Filteret Agg vil vise navnet og kodene til aggregeringsgrupperingen: F.eks. vises summeringen til "5- årige aldersgrupper" 0-4 år, i spørringen slik:
> {"filter": "agg:FemAarigGruppering", "values": ["F00-04"]}

Om du bruker "agg:" er eneste mulighet å velge enkeltverdier, slik som med ‘filter’: ‘item’. Å bruke ‘agg:’ slik som filteret ‘all’ med '*' fungerer dessverre ikke. En spørring som skal inkludere tidsserier for sammenslåtte kommuner som er berørt av kommunereformen, kan altså ikke benytte "item". K-koder må ha agg: og navnet på aggregeringen KommSummer i stedet, slik "filter": "agg:KommSummer". Eksempel på en spørring for Oslo og Halden.
> {"code":"Region","selection": {"filter":"agg:KommSummer","values":["K-0301","K-3004"]} },

Tallene for Oslo er de samme som om en hadde brukt 0301, mens tidsserien for Moss summerer opp de gamle kommunene (Moss og Rygge) som inngår i nye Moss, kommunenummer 3004. Den vanligste koden for sammenslåtte tidsserier er K-kommunenr. I enkelte tilfeller vil skilletegnet bindestrek peke til en annen kodeliste og erstattes av understrek eller punktum, altså K_ (tabell 06913) eller K.



**vs:**
Om du i spørringen får opp filter som begynner på vs:, f.eks. "filter": vs:AlleAldre00B", så kan/bør hele uttrykket i stedet erstattes med "filter": "item".



