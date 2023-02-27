
from pdf import *





class manager():   

    data_one = ""
    data_two = ""
    data_three = ""
    data_four = ""
    name_pdf = ""



    def __init__(self, data_one, data_two, data_three, data_four, name_pdf ):

        self.data_one = data_one
        self.data_two = data_two
        self.data_three = data_three
        self.data_four = data_four
        self.name_pdf = name_pdf
        self.printPdf()

   

    def printPdf(self):      

        pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 

        pdf.alias_nb_pages()
        pdf.add_page()

        pdf.set_left_margin(20)
        pdf.set_right_margin(20)

        # TEXTO DEL RECUADRO
        
        pdf.set_font('Arial', '', 15) 
        pdf.multi_cell(w = 0, h = 8, txt = 'BIJZONDERE VOORWAARDEN: \n ARBEIDSRECHT  SOCIALE ZEKERHEID', border = 1,
                 align = 'C', fill = 0)
        pdf.ln(3)
        tfont_size(pdf, 11)
        pdf.cell(w = 0, h = 8, txt = 'Tussen:', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.ln(2)
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV\nWestlaan 120\n8800 Roeselare\nBTW BE 0883.206.675 ', border = 0,
                 align = 'L', fill = 0)
        pdf.ln(2)

      
        pdf.cell(w = 0, h = 8, txt = 'BV MODDER gedelegeerd bestuurder met als vast vertegenwoordiger Dhr. Mathias Vandaele', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.ln(2)
        pdf.cell(w = 0, h = 8, txt = 'En', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.ln(2)
        pdf.multi_cell(w = 0, h = 5, txt = self.data_one + '\n' + self.data_two + '\n' + self.data_three + '\n' + self.data_four, border = 0,
                 align = 'L', fill = 0)  
        pdf.ln(2)
        pdf.multi_cell(w = 0, h = 5, txt = 'Hierbij vertegenwoordigd door Dhr. 	, hierna tevens genoemd de Aannemer ', border = 0,
                 align = 'L', fill = 0)
        pdf.ln(2)
        
        ################################################################################################
        ######################## ITEM UNO
        ################################################################################################


        pdf.cell(w = 0, h = 5, txt = '1.    Zelfstandigheid in de uitvoering van de opdracht', border = 0, ln = 4, 
                 align = 'L', fill = 0)

        pdf.set_left_margin(27.5)
        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer die de bestelbon van Hectaar NV met verwijzing naar onderhavige bijzondere voorwaarden inzake de naleving van het arbeidsrecht en het sociale zekerheidsrecht schriftelijk heeft aanvaard, verbindt er zich toe om alle hierna vermelde wettelijke, reglementaire en conventionele verplichtingen te zullen naleven en te doen naleven door zijn Onderaannemer(s), en elke persoon waarop hij beroep doet.', border = 0,
                 align = 'J', fill = 0)



        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.1  Onafhankelijkheid', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal de opdracht volledig zelfstandig en autonoom uitvoeren.', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.2  Eigen personeel, eigen aangestelden', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal voor de uitvoering van de werken zoals voorzien in deze overeenkomst uitsluitend eigen personeel of eigen aangestelden inzetten, voor wie hij de volledige verantwoordelijkheid als werkgever en/of als aansteller draagt.', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.3  Inzet personeel / aangestelden', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer beslist zelf over het aantal werknemers en/of aangestelden die hij inzet voor de uitvoering van het werk (rekening houdend met de aard en de omvang van het werk, en de planning en doelstellingen die overeengekomen werden of die door partijen worden vastgelegd of aangepast lopende de uitvoering van de werken).', border = 0,
                 align = 'J', fill = 0)


        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.4  Vakbekwaam personeel / aangestelden', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer verbindt er zich toe om voor de uitvoering van de overeengekomen opdrachten uitsluitend en voldoende vakbekwame / gediplomeerde personen in te zetten.', border = 0,
                 align = 'J', fill = 0)


        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.5  Aanstelling van een communicatiepersoon en een ploegverantwoordelijke', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer stelt een communicatiepersoon aan. Deze communicatiepersoon zal instaan voor de communicatie tussen de Aannemer en Hectaar NV.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal er voor zorgen dat er steeds minstens één leidinggevende werknemer of aangestelde beschikbaar is die als ploegverantwoordelijke functioneert en die volgende Nederlands dan wel Frans of Engels kan lezen en spreken.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'Deze ploegverantwoordelijke zal minstens gekwalificeerd zijn als meestergast en is voldoende bekwaam om alle werkzaamheden en alle werknemers of aangestelden van de Aannemer te leiden. Hij zal instaan voor het geven van alle instructies die nodig zijn voor de goede uitvoering van de opdracht', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'M.o. de veiligheid en de goede communicatie op de plaats van het werk zal de Aannemer ervoor zorgen dat deze ploegverantwoordelijke voldoende kennis heeft van alle wettelijke en reglementaire preventieverplichtingen.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'Vóór de uitvoering van de overeenkomst zal de Aannemer Hectaar NV in kennis stellen van de volgende gegevens:', border = 0,
                 align = 'J', fill = 0)

        pdf.multi_cell(w = 0, h = 5, txt = '-	    Communicatiepersoon (communicatie met Hectaar NV):', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = ' 	    __________________________________________________', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Ploegverantwoordelijke (communicatie op de werf):', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = ' 	    __________________________________________________', border = 0,
                 align = 'J', fill = 0)




        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.6  Leiding van het eigen personeel / aangestelden', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De ploegverantwoordelijke van de Aannemer staat in voor het geven van alle instructies en het nemen van alle maatregelen die nodig zijn voor de goede uitvoering van de opdracht. Hectaar NV zal er zich absoluut van onthouden om rechtstreeks instructies te geven aan de werknemers en aangestelden van de Aannemer.', border = 0,
                 align = 'J', fill = 0)
        pdf.multi_cell(w = 0, h = 5, txt = 'De werknemers of aangestelden van de Aannemer zullen op geen enkel ogenblik als werknemer of aangestelde van Hectaar NV kunnen worden beschouwd.', border = 0,
                 align = 'J', fill = 0)


        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.7  Instructies in verband met de uitvoering van de opdracht', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV zal zich onthouden van elke controle op de wijze van uitvoering van de opdracht. Het is Hectaar NV enkel toegelaten om de werken te controleren en de gebreken en/of de aanpassingen van de opdracht mee te delen aan de Aannemer; Hectaar NV zal zich desgevallend richten tot de communicatiepersoon of tot de ploegverantwoordelijke van de Aannemer.', border = 0,
                 align = 'J', fill = 0)
        
        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'Voor een goede planning en uitvoering van de werken kunnen lopende de uitvoering van de opdracht bijkomende afspraken worden gemaakt; desgevallend zullen deze afspraken _ indien zij betrekking hebben op instructies inzake de uitvoering van de opdracht _ steeds schriftelijk worden vastgelegd en als aanvulling van de overeenkomst gelden.', border = 0,
                 align = 'J', fill = 0)


        pdf.set_left_margin(20)
        pdf.ln(2)
        pdf.cell(w = 0, h = 5, txt = '1.8  Instructies door Hectaar NV  uitzonderingen', border = 0, ln = 4, 
                 align = 'L', fill = 0)
        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV mag de personeelsleden en de aangestelden van de Aannemer aldus in ieder geval geen (rechtstreekse) bevelen, instructies en richtlijnen geven, met uitzondering van:', border = 0,
                 align = 'J', fill = 0)

        pdf.multi_cell(w = 0, h = 5, txt = '-	    Eventuele (aanvullende en/of corrigerende) instructies tot naleving van de dwingende ', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = ' 	    wettelijke voorschriften inzake veiligheid en welzijn op het werk; ', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Eventuele instructies m.b.t. de toegang tot de plaats van het werk en de controle terzake.', border = 0,
                 align = 'J', fill = 0) 

        ################################################################################################
        ######################## ITEM DOS
        ################################################################################################

        pdf.set_left_margin(20)

        pdf.ln(2)       
        pdf.cell(w = 0, h = 5, txt = '2.    Naleving van het arbeidsrecht en het sociale zekerheidsrecht', border = 0, ln = 4, 
                 align = 'L', fill = 0)

        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '2.1  De Aannemer verbindt er zich toe om alle arbeidsrechtelijke en sociaalzekerheidsrechtelijke', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'verplichting na te leven met betrekking tot hemzelf, zijn personeel en zijn aangestelden.', border = 0,
                 align = 'J', fill = 0)

             


        pdf.set_left_margin(20)
        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = '2.2  De Aannemer verbindt er zich toe om alle arbeidsrechtelijke en sociaalzekerheidsrechtelijke', border = 0,
                 align = 'J', fill = 0)
        pdf.ln(2)      
        pdf.set_left_margin(27.5)   

        pdf.multi_cell(w = 0, h = 5, txt = '(i)	   De Aannemer zal er voor zorgen dat hij voor de uitvoering van het werk enkel eigen', border = 0,
                 align = 'J', fill = 0)
        pdf.set_left_margin(35)   
        pdf.multi_cell(w = 0, h = 5, txt = 'werknemers inschakelt.', border = 0,
                 align = 'J', fill = 0)
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal voor alle werknemers die niet in België worden tewerkgesteld en dewelke door de Aannemer gedetacheerd worden naar de plaats van het werk alle nodige maatregelen nemen voor de voorafgaande Limosa-aanmelding van de tewerkstelling in het kader van de controle op het vrij verkeer van werknemers. De Aannemer zal Hectaar NV in ieder geval een kopie bezorgen van alle attesten waaruit de correcte aanmelding voor de volledige duur van de tewerkstelling blijkt.', border = 0,
                 align = 'J', fill = 0)


        pdf.set_left_margin(27.5)   
        pdf.ln(2)    
        
        pdf.multi_cell(w = 0, h = 5, txt = '(ii)   De Aannemer zal voor al deze werknemers een zgn. A1-formulier of', border = 0,
                 align = 'J', fill = 0)
        pdf.set_left_margin(35)  
        pdf.multi_cell(w = 0, h = 5, txt = 'detacheringsverklaring overmaken.', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = 'Om een controle op de nakoming van deze verplichting mogelijk te maken zal de Aannemer tevens zorgen voor de aangifte van een duidelijk kopie van alle identiteitskaarten.', border = 0,
                 align = 'J', fill = 0)


        
        pdf.set_left_margin(27.5)   
        pdf.ln(2)    
        
        pdf.multi_cell(w = 0, h = 5, txt = '(iii)  Indien wettelijke vereist zullen voor werknemers die niet afkomstig zijn uit de EU-landen', border = 0,
                 align = 'J', fill = 0)
        pdf.set_left_margin(35)  
        pdf.multi_cell(w = 0, h = 5, txt = 'alle formaliteiten inzake arbeidskaarten, -vergunningen en de toegang en het verblijf in het land van de plaats van de uitvoering van de odracht worden nageleefd. De Aannemer zal in geen geval werknemers tewerkstellen voor wie niet voldaan is aan alle voormelde verplichtingen (randnummer (i), (ii) en (iii)). De Aannemer bezorgt Hectaar NV voorafgaand aan de uitvoering van de opdracht kopie van:', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Alle Limosa-meldingen;', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Alle A1-formulieren zoals vermeld in (i) en (ii);', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Alle arbeidsvergunningen- en kaarten en verblijfsvergunning zoals vermeld in (iii).', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = 'De personeelsleden van de Aannemer en zijn ploegverantwoordelijke zullen steeds in het bezit zijn van een kopie van deze documenten.', border = 0,
                 align = 'J', fill = 0) 


        
        pdf.set_left_margin(20)
        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '2.3  Naleving van het arbeidsrecht', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer verbindt er zich toe om het toepasselijke arbeidsrecht en in ieder geval ook alle dwingende bepalingen van het arbeidsrecht (inzake arbeids- en loonvoorwaarden, arbeidstijden, enz.) van de plaats van het werk na te leven.', border = 0,
                 align = 'J', fill = 0)
        pdf.ln(2)       

        pdf.multi_cell(w = 0, h = 5, txt = 'Meer in het bijzonder verbindt de Onderaannemer zich ertoe om steeds de sectoraal vastgelegde minimumlonen te respecteren zoals die geraadpleegd kunnen worden op de website van de FOD WASO (www.minimumlonen.be). Door de ondertekening van deze bijzondere voorwaarden bevestigd de Onderaannemer dat de werknemers die hij inschakelt bij de uitvoering van de opdracht steeds correct verloond zullen worden conform deze sectoraal vastgelegde minimumlonen.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)       

        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal er voor zorgen dat zijn leidinggevende ploegverantwoordelijke en communicatiepersoon in het bezit zijn van alle sociale documenten die volgens het vereenvoudigd stelsel (richtlijn 91/71/EG) beschikbaar moeten zijn in het geval van een sociale controle.', border = 0,
                 align = 'J', fill = 0)


        ################################################################################################
        ######################## ITEM TRES
        ################################################################################################


        pdf.set_left_margin(20)
        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '3.    Unieke werfmelding', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer dient de verplichtingen inzake de "unieke werfmelding" na te komen.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)   
        pdf.multi_cell(w = 0, h = 5, txt = 'Aldus zal de Aannemer zorgen voor de elektronische werfmelding voor alle opdrachten voor werken waarvan het totaalbedrag hoger is dan 30.000,00 EUR (excl. BTW), alsook voor alle werken waarvan het totaalbedrag hoger is dan 5.000,00 EUR op werven waarop meerdere Aannemers actief zijn.', border = 0,
                 align = 'J', fill = 0)
        pdf.ln(2)   

        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer is verplicht om Hectaar NV voorafgaandelijk in kennis te stellen van de:', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Datum begin van de uitvoering op de werf;', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    Datum einde van de uitvoering op de werf.', border = 0,
                 align = 'J', fill = 0) 

        pdf.ln(2)   
        pdf.multi_cell(w = 0, h = 5, txt = 'In geval van een voorafgaandelijke schriftelijke toestemming van Hectaar NV aan de Aannemer om de uitvoering van de werking in onderaanneming te geven, zal de Aannemer in overleg met Hectaar NV al het nodige doen opdat de verplichtingen inzake de "unieke werfmelding" nageleefd kunnen worden; in geval van enig gebrek in de communicatie terzake zal de Aannemer volledig aansprakelijk zijn voor elke mogelijke sanctie.', border = 0,
                 align = 'J', fill = 0) 

        ################################################################################################
        ######################## ITEM CUATRO
        ################################################################################################


        pdf.set_left_margin(20)
        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '4.    Elektronische aanwezigheidsregistratie op grote bouwwerven', border = 0,
                 align = 'J', fill = 0)

        pdf.multi_cell(w = 0, h = 5, txt = '4.1  Hectaar NV en de Aannemer dienen de verplichting inzake de "elektronische', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'aanwezigheidsregistratie op grote bouwwerven" na te leven in geval de opdracht betrekking heeft op een werf van meer dan 500.000,00 EUR. De Aannemer dient zelf na te gaan of hij gehouden is tot de naleving van deze verplichting.', border = 0,
                 align = 'J', fill = 0)
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal in ieder geval ook door de RSZ in kennis gesteld worden van zijn registratieverplichting en de zgn. "QR-code".', border = 0,
                 align = 'J', fill = 0)
        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = 'Behoudens in geval partijen schriftelijke orders overeenkomen, zal de Aannemer zorgen voor de registratie van alle personeel en alle eventuele uitzendkrachten en alle aangestelden die hij inschakelt voor de uitvoering van de opdracht op de werf.', border = 0,
                 align = 'J', fill = 0) 


        pdf.set_left_margin(20)

        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = '4.2  De Aannemer zal zelf instaan voor deze registratie via de online diensten van de RSZ.', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'Ingeval de Aannemer een inbreuk pleegt op zijn verplichting inzake de elektronische aanwezigheidsregistratie, zal hij t.o.v. Hectaar NV aansprakelijk zijn voor alle mogelijke financiële sancties en schade in hoofde van Hectaar NV.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  
        
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV is ingeval van een vaststelling van een dergelijke inbreuk gerechtigd om de volledige schadevergoeding in te houden op elke betaling die hij aan de Aannemer verschuldigd is; deze schadevergoeding zal desgevallend provisioneel begroot worden op basis van de wettelijke reglementering.', border = 0,
                 align = 'J', fill = 0)
        pdf.ln(2)  
        
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV heeft krachtens de wettelijke regeling de mogelijkheid om de elektronische aanwezigheidsregistratie door zijn Aannemer te controleren; partijen erkennen en bevestigen voor zoveel als nodig dat deze regeling geen afbreuk doet aan voormelde afspraken inzake de aansprakelijkheid voor schade ingeval van inbreuk door de Aannemer.', border = 0,
                 align = 'J', fill = 0)




        pdf.set_left_margin(20)

        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = '4.3  In geval van een voorafgaandelijke schriftelijke toestemming van Hectaar NV aan de', border = 0,
                 align = 'J', fill = 0)

        pdf.set_left_margin(27.5)        
        pdf.multi_cell(w = 0, h = 5, txt = 'Aannemer om de uitvoering van de werken in onderaanneming te geven zal de Aannemer in overleg met Hectaar NV al het nodige doen opdat de verplichtingen inzake de elektronische aanwezigheidsregistratie nageleefd worden; in geval van enig gebrek in deze verplichting terzake zal de Aannemer volledig aansprakelijk zijn voor elke mogelijke sanctie.', border = 0,
                 align = 'J', fill = 0)
        
        ################################################################################################
        ######################## ITEM CINCO
        ################################################################################################
        
        pdf.set_left_margin(20)
        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '5.    Preventie- en welzijnsverplichtingen', border = 0,
                 align = 'J', fill = 0)
        pdf.set_left_margin(27.5)        

        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal zichzelf en zijn werknemers en aangestelden goed informeren over al zijn verplichtingen inzake het welzijn en de veiligheid die conform de toepasselijke wetgeving op de plaats van het werk moeten worden nageleefd.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal instaan voor het uitvoeren van alle nodige risicoanalyses en het nemen van alle nodige preventiemaatregelen; de Aannemer zal hierbij steeds toepassing maken van de preventiebeginselen zoals voorzien in de Welzijnswet. In geval van de uitvoering van werken op hoogte en/of het gebruik van mobiele arbeidsmiddelen zal de Aannemer in ieder geval een specifieke risicoanalyse uitvoeren en zal zijn preventieadviseur hierover verslag; in geval van specifieke risico s zal de Aannemer minstens een voorafgaandelijke toolboxmeeting organiseren.', border = 0,
                 align = 'J', fill = 0)     


        pdf.ln(2)  

        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer zal zijn werknemers en aangestelden in ieder geval informeren over:', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    De risico s voor het welzijn van de werknemers op de plaats van het werk;', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    De bescherming en preventiemaatregelen en activiteiten op de plaats van het werk;', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    De organisatie van de eerste hulp op de plaats van het werk;', border = 0,
                 align = 'J', fill = 0) 
        pdf.multi_cell(w = 0, h = 5, txt = '-	    De brandbestrijding en de evacuatie van personen op de plaats van het werk.', border = 0,
                 align = 'J', fill = 0) 

        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = 'De Aannemer verbindt er zich toe zijn verplichtingen inzake het welzijn van de werknemers bij de uitvoering van hun werk, te doen naleven.', border = 0,
                 align = 'J', fill = 0) 
        
        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = 'De aansprakelijkheid van Hectaar NV zal in geen geval kunnen worden ingeroepen voor de ongevallen van welke aard ook, met inbegrip van die waarvan de Aannemer, de personeelsleden, de aangestelden en/of de helpers van de Aannemer het slachtoffer zouden kunnen zijn en/of voor de schade die de Aannemer, de personeelsleden, de aangestelden en/of de helpers zouden kunnen veroorzaken aan derden en/of aan hun goederen. De Aannemer staat derhalve zelf in voor dergelijke ongevallen en/of schade.', border = 0,
                 align = 'J', fill = 0) 


        ################################################################################################
        ######################## ITEM SEIS
        ################################################################################################

        pdf.set_left_margin(20)
        pdf.ln(2)       
       
        pdf.multi_cell(w = 0, h = 5, txt = '6.    Beëindiging van de overeenkomst', border = 0,
                 align = 'J', fill = 0)
        pdf.set_left_margin(27.5)        

        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV heeft het recht om de overeenkomst met de Aannemer met onmiddellijke ingang en zonder enigwelke vergoeding te beëindigen ingeval wordt vastgesteld dat de Aannemer een inbreuk pleegt op zijn verplichtingen zoals vastgelegd in de artikelen 1, 2, 3 en 4.', border = 0,
                 align = 'J', fill = 0)

        pdf.ln(2)  
        pdf.multi_cell(w = 0, h = 5, txt = 'Ditzelfde recht heeft Hectaar NV ook ingeval laatstgenoemde door de diensten van de sociale inspectie, conform de bepalingen van de Loon beschermingswet, op de hoogte wordt gebracht van het feit dat de Aannemer zijn loonverbintenissen t.a.v. zijn werknemers niet correct naleeft.', border = 0,
                 align = 'J', fill = 0)


        pdf.ln(30)  
        pdf.multi_cell(w = 0, h = 5, txt = 'Voor akkoord,	                                                                   Voor akkoord,', border = 0,
                 align = 'J', fill = 0)
        pdf.multi_cell(w = 0, h = 5, txt = 'Hectaar NV,	                                                                      de Aannemer', border = 0,
                 align = 'J', fill = 0)
        





       
        
        








        pdf.output(self.name_pdf +'.pdf')




