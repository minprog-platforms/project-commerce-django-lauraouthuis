Procesboek programmeerproject Django  
Laura Outhuis (s14687887)  

Maandag 28 november  
Omdat ik vorige week weinig tijd had besteed aan het projectvak en meer aan programmeren 2, heb ik besloten om deze week te beginnen aan commerce door alles op een rijtje krijgen. Ik ben door de verschillende bestanden gegaan en heb bij een aantal bestanden opgeschreven waar ze voor dienen:  
auctions/urls.py → this is where the URL configuration for this app is defined  
auctions/views.py → here you can see that the views are associated with each of the routes  
the login_view renders a login form when a user tries to GET the page  
the logout_view view logs the user out and redirects them to the index page  
the register route displays a registration form to the user and creates a new user when the form is submitted  
auctions/templates/auctions/layout.html → several parts of the template are wrapped in a check for if user.is_authenticated, so that different content can be rendered depending on whether the user is signed in or not  
auctions/models.py → this is where you will define any models for your web application, where each model represents some type of data you want to store in your database   
there is already a User model that represents each user of the application   
because it inherits from AbstractUser, it already has fields for a username, email, passwords, etc. → you can add new fields to the User class if there is any additional information that you wish to represent  
you will also need to add additional models to this file to represent details about auction listings, bids, comments, and auction categories  

Omdat ik niet zo goed wist waar ik moest beginnen, ben ik gewoon de lijst in de hints afgegaan. Toen zag ik dat er stond ‘create a superuser account that can access Django’s admin interface’. Omdat ik dit nog niet eerder had gedaan, heb ik gegoogled hoe dit moet.2 Ik wist verder nog niet zo goed wat ik hiermee moest doen, dus ik heb alleen even via de url/admin getest of het inloggen werkte, maar daarna heb ik even gelaten voor wat het is.  

on_delete = models.CASCADE → “When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well).”1  

In models.py wilde ik de models registreren. Ik wist eerst niet goed wat hiermee bedoeld werd, en ik dacht dat ik dit via de interface moest doen, tot iemand aan mijn tafel suggesteerde om ‘register models in admin django’ te Googlen. Via de documentatie website van Django3 vond ik daardoor hoe ik deze code kon schrijven (“admin.site.register(Author, AuthorAdmin”).   

Ik liep er vervolgens wel tegenaan dat in de admin interface, bij elk field een extra ‘s’ werd geplakt (Auction listingss, Bidss, etc.). Ik dacht dat ik hier een fout had gemaakt, maar na wat zoeken vond ik via Stackoverflow4 dat dat hoort bij de Django admin panel. Omdat er geen last van heb, heb ik besloten om er niks aan te doen (in de comments stond dat je met behulp van een class Meta dit kan oplossen, maar misschien dat ik dit in een later stadium nog probeer).  

Het was mij niet helemaal duidelijk waarom je (volgens de specificaties in de opdracht) een aparte file moet hebben voor het aanmaken van nieuwe listings (“Create Listing: Users should be able to visit a page to create a new listing.(...).”), als je ook alles kan aanmaken via de interface. Ik vroeg het aan de assistent en die zei dat het op deze manier een stuk gebruiksvriendelijker is en dat was op zich wel logisch.  

Ik liep een tijdje vast na het aanmaken van de ‘create_listing.html’, omdat ik de pagina niet terug kon vinden op de website. Na een tijdje alles nalezen kwam ik erachter dat ik was vergeten om de path toe te voegen via urls.py en niet had toegevoegd in de navigatiebalk bovenin de pagina, dus het was wel logisch dat hij het dan niet zou doen.  

Op gegeven moment kwam ik er ook achter dat de create listing pagina niet naar de juiste file verwees. Hij liet namelijk steeds de inhoud van index.html zien, en niet van create_listing.html. Ook moest ik elke keer als ik op ‘Create a new listing’ klikte opnieuw inloggen, zelfs als ik al ingelogd was.  

Woensdag 30 november  
Ik wilde testen of het aanmaken van een nieuw listing item nu helemaal werkte, maar ik kreeg deze error:  
MultiValueDictKeyError at /create_listing  
Exception Location: /home/lauraouthuis/.local/lib/python3.8/ site-packages/django/utils/datastructures.py, line 86, in _getitem__
  
Omdat hij een error gaf bij create_listing, ben ik in de create_listing.html gaan zoeken, maar daar komt de _getitem__ niet in voor en is ook geen line 86. Uiteindelijk ben ik met een tafelgenoot alle code gaan langslopen en hebben we meerdere dingen aangepast, waardoor het het uiteindelijk wel deed, maar ik weet niet zo goed wat het hem nou gedaan heeft.  
  
Maandag 5 december  
Over wat bijv. widht: 18rem betekent5  

Bij het aanmaken van de watchlist had ik de volgende code geschreven:  




Alleen werkte dit niet en gaf het een Syntax error. Ik heb daarom de losse if statements vervangen voor if else.  

5 - 9 december 2022  
Ik heb deze week verschillende dingen aangepast in het project, maar ben vergeten de te committen en pushen. Ik heb vooral veel dingen over de structuur opgezocht en heb bij verschillende forms en for loops beschrijvingen toegevoegd, omdat ik een beetje het overzicht begon te verliezen. Dit hielp heel erg. Ook heb ik geprobeerd de code wat overzichtelijker te maken door meer witregels ertussen te laten.  

Het duurde heel erg lang voordat alles met de categories goed werkte. Ik haalde vaak de namen van een path en de namen van de functies of bestanden door elkaar (die allemaal net iets verschilden van elkaar, bijvoorbeeld get_category, category, categories). Uiteindelijk ben ik met de zoekfunctie samen met iemand alles langsgegaan en heb ik op meerdere plekken de namen aangepast, waardoor het het eindelijk weer deed. Ik heb hier heel veel tijd op verloren, omdat ik de website hierdoor niet kon zien en daardoor ook lastig verder kon werken aan andere onderdelen, dus heb toen wat meer tijd besteed aan programmeren 2.  

Donderdag 8 december  
Ik zag vandaag dat er een fout zat in het models.py bestand op regel 40, hier stond naar als related_name bij category “owner”, maar dit moest category zijn.  
  
13 december 2022  
Ik heb vandaag geprobeerd om de layout wat op te schonen, bijvoorbeeld door ruimte tussen de afbeeldingen in de cards toe te voegen. Het duurde heel erg lang voordat dit goed werkte. Vaak werkte het niet om in de stylesheet opmaak toe te voegen, dus het ik style attributen in de div van de class gezet. Ook gaf iemand de tip om soms de pagina hard the refreshen (ctrl F5) omdat de veranderingen dan opeens wel zichtbaar waren. Ook heb ik andere Bootstrap layouts uitgeprobeerd (bijv. btn-btn-outline-primary waardoor je alleen de outline ziet).  
  
14 december 2022  
Vandaag heb ik de laatste aanpassingen gedaan aan de Markdown bestanden. De syntax voor het invoegen van afbeeldingen in een markdown bestand kon ik vrij gemakkelijk Googlen, maar op een of andere manier liet hij bij 1 afbeelding alleen de alt tekst zien. Ik heb meerdere keren geprobeerd dingen aan te passen (volgorde, afbeelding opnieuw downloaden, maar hij bleef het niet doen). Aan het einde van de dag nadat ik een paar keer opnieuw gepusht had deed hij het opeens weer wel, maar ik weet niet zo goed waar dat door is gekomen.  
  
Als laatste kwam ik vandaag pas achter dat je ook een Class diagram moest maken, wat ik nog niet zo goed begreep. Ik zag doordat ik naar de verschillende classes ging kijken ook dat de User class eigenlijk niks deed (hier staat alleen ‘pass’) maar nadat ik hem had verwijderd deed het inlogsysteem het niet meer, dus toen heb ik hem weer terug gezet. Ik zag toen dat in de register functie de User class wel wordt gebruikt, namelijk om nieuwe gebruikers in op te slaan, deze is dus wel nodig.  
  
Ook heb ik nog wat extra comments over de specificaties van de opdracht weggehaald en doc strings toegevoegd bij classes en methods met uitleg over wat deze doen.  
  
Eind evaluatie  
Ik merkte tijdens dit project vooral dat ik snel het overzicht verloor, waardoor ik dingen door elkaar ging halen (en andersom). Ik heb geprobeerd om dit tijdens het project te verbeteren door veel comments toe te voegen. Ook vergat ik aan het begin vaak om te committen en pushen, ik denk dat dit een kwestie van gewenning was, want aan het einde deed ik dit veel frequenter. Ook was ik aan het begin bang om dingen op te zoeken van pagina’s zoals StackOverflow, omdat ik bang was om dingen per ongeluk over te nemen en nam ik ook geen eigen oude code over, bijvoorbeeld uit de Wiki opdracht. Nadat ik met een paar assistenten het hierover heb gehad zeiden zij dat je soms dingen nou eenmaal niet op 100 verschillende manieren kan doen en je daardoor sowieso snel repetitieve stukken code krijgt, en dat het niet altijd erg is om aan de hand van andermans voorbeelden te werken, zolang je het maar zelf implementeert en begrijpt hoe het werkt. Het heeft toen ook geholpen om meer vragen te stellen aan medestudenten over hun aanpak.  
  
Referenties  
1 What does on_delete do on Django models? (2016, 15 juli). Stack Overflow. https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models  
2 How to create a superuser in Django. (z.d.). Educative: Interactive Courses for Software Developers. https://www.educative.io/answers/how-to-create-a-superuser-in-django  
3 Django. (z.d.). Django Project. https://docs.djangoproject.com/en/4.1/ref/contrib/admin/  
4 How can i remove extra “s” from django admin panel? (2015c, augustus 17). Stack Overflow. https://stackoverflow.com/questions/32047686/how-can-i-remove-extra-s-from-django-admin-panel  
5 Winter, R. (2022, 23 augustus). What Are Rem Units? (& How to Use Them in CSS). https://blog.hubspot.com/website/css-rem  