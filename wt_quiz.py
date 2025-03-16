


import random

class HTML:
    questions = [
        ("Was ist das Standard-Dokumentelement in HTML?", "<html>", "<div>", "<body>", "<head>"),
        ("Welches HTML-Tag wird verwendet, um eine Überschrift der ersten Ebene zu definieren?", "<h1>", "<h2>", "<h3>", "<h4>"),
        ("Welches Attribut wird verwendet, um den Titel einer Webseite zu definieren?", "title", "name", "header", "alt"),
        ("Wie fügt man ein Bild in HTML ein?", "<img src='bild.jpg'>", "<image src='bild.jpg'>", "<pic src='bild.jpg'>", "<img href='bild.jpg'>"),
        ("Welches HTML-Tag wird verwendet, um einen Hyperlink zu erstellen?", "<a>", "<link>", "<href>", "<url>"),
        ("Welches HTML-Tag wird verwendet, um eine ungeordnete Liste zu erstellen?", "<ul>", "<ol>", "<li>", "<dl>"),
        ("Wie kann man Text fett darstellen?", "<strong>", "<b>", "<f>", "<em>"),
        ("Welches HTML-Tag wird verwendet, um eine Tabelle zu definieren?", "<table>", "<tr>", "<td>", "<th>"),
        ("Wie fügt man einen Kommentar in HTML ein?", "<!-- Kommentar -->", "// Kommentar", "/* Kommentar */", "<# Kommentar #>"),
        ("Wie kann man in HTML eine Dropdown-Liste erstellen?", "<select>", "<dropdown>", "<list>", "<option>"),
        ("Welches Attribut wird verwendet, um ein Eingabefeld für ein Passwort zu erstellen?", "type='password'", "type='text'", "type='hidden'", "type='input'"),
        ("Welches HTML-Tag wird verwendet, um einen Abschnitt (Absatz) zu definieren?", "<p>", "<section>", "<div>", "<article>"),
        ("Wie fügt man eine externe JavaScript-Datei in HTML ein?", "<script src='script.js'>", "<js src='script.js'>", "<javascript src='script.js'>", "<external src='script.js'>"),
        ("Welches HTML-Tag wird verwendet, um eine Überschrift der dritten Ebene zu definieren?", "<h3>", "<h1>", "<h2>", "<h4>"),
        ("Welches Attribut wird verwendet, um einen Link in einem neuen Fenster zu öffnen?", "target='_blank'", "window='new'", "open='true'", "new='window'"),
        ("Wie kann man ein Video in HTML einfügen?", "<video src='video.mp4'>", "<movie src='video.mp4'>", "<video href='video.mp4'>", "<media src='video.mp4'>"),
        ("Was ist das Attribut für die Angabe der Quelle einer eingebetteten Audio-Datei?", "src", "source", "file", "audio-src"),
        ("Wie kann man in HTML eine Tabelle mit einer Kopfzeile definieren?", "<table><thead>...</thead></table>", "<table><head>...</head></table>", "<table><header>...</header></table>", "<table><th>...</th></table>"),
        ("Welches HTML-Tag wird verwendet, um eine horizontale Linie zu erstellen?", "<hr>", "<line>", "<br>", "<hline>"),
        ("Welches HTML-Tag wird verwendet, um einen Link zu einer anderen Webseite hinzuzufügen?", "<a>", "<url>", "<link>", "<navigate>"),
        ("Welches Attribut wird verwendet, um den Stil einer HTML-Seite mit CSS zu verknüpfen?", "style", "href", "css", "link"),
        ("Was ist der Zweck des `alt`-Attributs in einem `<img>`-Tag?", "Es gibt eine Textbeschreibung des Bildes", "Es gibt die Größe des Bildes an", "Es bestimmt den Pfad des Bildes", "Es gibt den Titel des Bildes an"),
        ("Welches HTML-Tag wird verwendet, um eine geordnete Liste zu erstellen?", "<ol>", "<ul>", "<dl>", "<list>"),
        ("Wie fügt man einen internen CSS-Stil in eine HTML-Seite ein?", "<style>...</style>", "<css>...</css>", "<link>...</link>", "<script>...</script>"),
        ("Was ist das Standardwert für das Attribut `type` eines `<input>`-Tags?", "text", "password", "checkbox", "radio"),
        ("Wie kann man ein neues Zeilenumbruch in HTML einfügen?", "<br>", "<hr>", "<p>", "<newline>"),
        ("Was ist das richtige HTML-Tag, um ein Formularfeld für die Eingabe einer E-Mail-Adresse zu erstellen?", "<input type='email'>", "<input type='text'>", "<input type='url'>", "<input type='password'>"),
        ("Wie kann man einen CSS-Stil direkt in einem HTML-Tag anwenden?", "style='...'", "class='...'", "id='...'", "src='...'"),
        ("Welches HTML-Tag wird verwendet, um ein Video einzubetten?", "<video>", "<embed>", "<source>", "<movie>"),
        ("Welches HTML-Tag wird verwendet, um den Kopfbereich einer Webseite zu definieren?", "<head>", "<header>", "<meta>", "<title>"),
        ("Wie wird das Attribut `href` in einem `<a>`-Tag verwendet?", "Um die Ziel-URL des Links zu definieren", "Um den Text des Links festzulegen", "Um den Stil des Links festzulegen", "Um das Ziel des Links festzulegen"),
        ("Welches HTML-Tag wird verwendet, um eine Liste von Definitionen zu erstellen?", "<dl>", "<ul>", "<ol>", "<list>"),
        ("Wie fügt man in HTML ein Formular mit mehreren Eingabefeldern hinzu?", "<form>...</form>", "<input>...</input>", "<field>...</field>", "<submit>...</submit>"),
        ("Welches HTML-Tag wird verwendet, um einen Abschnitt von Inhalten zu definieren?", "<section>", "<article>", "<div>", "<span>"),
        ("Welches HTML-Tag wird verwendet, um den Titel einer Webseite zu definieren?", "<title>", "<head>", "<meta>", "<h1>"),
        ("Wie wird das Attribut `disabled` in HTML verwendet?", "Um ein Formularfeld zu deaktivieren", "Um ein Bild zu verbergen", "Um einen Link zu deaktivieren", "Um Text zu deaktivieren"),
        ("Was ist der Unterschied zwischen `<div>` und `<span>` in HTML?", "`<div>` ist block-level, `<span>` ist inline", "`<div>` wird nur für Text verwendet, `<span>` für Block-Elemente", "`<div>` hat keine Bedeutung, `<span>` ist ein Container", "`<div>` wird verwendet, um Links zu erstellen, `<span>` nicht"),
        ("Wie definiert man eine Metadatenangabe für eine HTML-Seite?", "<meta>", "<head>", "<title>", "<link>"),
        ("Welches HTML-Tag wird verwendet, um eine Checkbox zu erstellen?", "<input type='checkbox'>", "<checkbox>", "<input type='radio'>", "<button>"),
        ("Welches HTML-Tag wird verwendet, um Text in einer Tabelle auszurichten?", "<td align='...'>", "<th>", "<tr>", "<table>"),
        ("Was bedeutet das Attribut `action` in einem `<form>`-Tag?", "Es gibt die URL an, an die das Formular gesendet wird", "Es gibt den Stil des Formulars an", "Es gibt den Text des Submit-Buttons an", "Es definiert die Methode der Formulareingabe"),
        ("Welches HTML-Tag wird verwendet, um den Text einer Webseite in einem Absatz darzustellen?", "<p>", "<div>", "<span>", "<text>"),
        ("Wie kann man ein eingebettetes Formular in einer Webseite erstellen?", "<form>", "<input>", "<button>", "<embed>"),
        ("Welches HTML-Tag wird verwendet, um eine Tabelle zu definieren?", "<table>", "<tr>", "<td>", "<th>"),
        ("Wie fügt man einen Hyperlink zu einer externen Webseite hinzu?", "<a href='url'>Linktext</a>", "<link href='url'>Linktext</link>", "<url href='url'>Linktext</url>", "<navigate href='url'>Linktext</navigate>"),
        ("Was ist der Unterschied zwischen `<section>` und `<article>` in HTML?", "<section> definiert einen thematischen Abschnitt, <article> einen unabhängigen Inhalt", "<article> ist für Metadaten, <section> für Textinhalte", "<section> enthält nur Listen, <article> nur Absätze", "<article> hat immer ein Bild, <section> nicht"),
        ("Welches HTML-Tag wird verwendet, um eine Zeile in einer Tabelle zu definieren?", "<tr>", "<td>", "<th>", "<table>"),
        ("Welches HTML-Tag wird verwendet, um eine Kopfzeile in einer Tabelle zu definieren?", "<th>", "<thead>", "<header>", "<tr>"),
        ("Welches HTML-Tag wird verwendet, um eine Fußzeile in einer Tabelle zu definieren?", "<tfoot>", "<tr>", "<footer>", "<td>"),
        ("Wie kann man den Stil einer Webseite mit einem externen Stylesheet verbinden?", "<link rel='stylesheet' href='style.css'>", "<style src='style.css'>", "<css href='style.css'>", "<stylesheet link='style.css'>"),
        ("Welches HTML-Tag wird verwendet, um eine geordnete Liste zu definieren?", "<ol>", "<ul>", "<li>", "<list>"),
        ("Wie kann man eine Hintergrundfarbe für eine Webseite festlegen?", "<body style='background-color: #fff'>", "<background color='#fff'>", "<body background='#fff'>", "<div style='background-color: #fff'>"),
        ("Wie erstellt man ein Eingabefeld für eine Telefonnummer in HTML?", "<input type='tel'>", "<input type='phone'>", "<input type='number'>", "<input type='text'>"),
        ("Wie fügt man ein eingebettetes YouTube-Video in HTML ein?", "<iframe src='https://www.youtube.com/embed/...'>", "<video src='https://www.youtube.com/...'>", "<embed src='https://www.youtube.com/...'>", "<youtube src='https://www.youtube.com/...'>"),
        ("Welches HTML-Tag wird verwendet, um eine Dropdown-Liste von Optionen anzuzeigen?", "<select>", "<option>", "<list>", "<dropdown>"),
        ("Was bedeutet das Attribut `value` in einem `<input>`-Tag?", "Es gibt den Standardwert für das Eingabefeld an", "Es gibt den Typ des Eingabefeldes an", "Es gibt die ID des Eingabefeldes an", "Es gibt den Text an, der im Eingabefeld angezeigt wird"),
        ("Welches HTML-Tag wird verwendet, um eine Bildunterschrift zu einer Tabelle hinzuzufügen?", "<caption>", "<image>", "<figcaption>", "<alt>"),
        ("Wie erstellt man in HTML ein eingebettetes Formular zur Dateiauswahl?", "<input type='file'>", "<input type='select'>", "<input type='browse'>", "<input type='upload'>"),
        ("Welches HTML-Tag wird verwendet, um den Text in einer Tabelle fett darzustellen?", "<strong>", "<b>", "<td><b>Text</b></td>", "<table><b>Text</b></table>"),
        ("Welches HTML-Tag wird verwendet, um eine horizontale Linie zu erstellen?", "<hr>", "<line>", "<br>", "<hline>"),
        ("Welches HTML-Tag wird verwendet, um Text in einer Webseite zu markieren?", "<mark>", "<highlight>", "<b>", "<strong>"),
        ("Wie kann man eine Liste von Definitionen in HTML erstellen?", "<dl><dt>...</dt><dd>...</dd></dl>", "<ul><li>...</li></ul>", "<ol><li>...</li></ol>", "<list><item>...</item></list>"),
        ("Welches Attribut eines `<a>`-Tags wird verwendet, um festzulegen, ob der Link in einem neuen Fenster geöffnet wird?", "target='_blank'", "new='window'", "open='true'", "target='new'"),
        ("Welches HTML-Tag wird verwendet, um einen Textabschnitt zu definieren?", "<div>", "<p>", "<section>", "<article>"),
        ("Wie kann man das Standardverhalten eines Formulars verhindern?", "event.preventDefault()", "form.preventSubmit()", "submit.prevent()", "form.stop()"),
        ("Welches HTML-Tag wird verwendet, um ein eingebettetes Dokument anzuzeigen?", "<iframe>", "<object>", "<embed>", "<frame>"),
        ("Welches Attribut wird verwendet, um den Hintergrund eines Dokuments festzulegen?", "background", "bgcolor", "style", "color"),
        ("Wie kann man eine Webseite responsiv gestalten?", "Durch Verwendung von Media Queries", "Durch Verwendung von `<meta>`-Tags", "Durch Verwendung von `position: absolute`", "Durch Verwendung von `flexbox`-Layouts"),
        ("Welches HTML-Tag wird verwendet, um eine Grafik einzubetten?", "<img>", "<picture>", "<svg>", "<graphic>"),
        ("Wie kann man einen Button in HTML erstellen?", "<button>Button</button>", "<input type='button'>", "<input value='Button'>", "<link type='button'>"),
        ("Welches HTML-Tag wird verwendet, um Text fett darzustellen?", "<strong>", "<bold>", "<b>", "<em>"),
        ("Wie kann man eine HTML-Seite an eine andere weiterleiten?", "<meta http-equiv='refresh' content='5; url=http://example.com'>", "<link rel='redirect' href='http://example.com'>", "<a href='http://example.com'>Redirect</a>", "<redirect url='http://example.com'>"),
        ("Wie kann man ein Formular in HTML verschicken?", "<form action='url' method='post'>", "<form method='post' url='url'>", "<form action='url' submit='true'>", "<form submit='url'>"),
        ("Welches HTML-Tag wird verwendet, um eine Audiodatei in einer Webseite einzubetten?", "<audio>", "<sound>", "<music>", "<audiofile>"),
        ("Wie kann man eine Eingabeaufforderung mit einem `<select>`-Tag erstellen?", "<select><option>...</option></select>", "<dropdown><option>...</option></dropdown>", "<list><item>...</item></list>", "<choose><option>...</option></choose>"),
        ("Was ist das Standardverhalten des Attributs `type` für ein `<button>`-Tag?", "submit", "reset", "button", "action"),
        ("Welches HTML-Tag wird verwendet, um den Inhalt einer Webseite im Hintergrund zu laden?", "<body>", "<iframe>", "<embed>", "<object>"),
        ("Wie kann man einen HTML-Link zu einer bestimmten Stelle innerhalb der gleichen Seite erstellen?", "<a href='#ziel'>Link</a>", "<link href='#ziel'>Link</link>", "<a href='ziel'>Link</a>", "<target href='#ziel'>Link</target>"),
        ("Wie kann man den Wert eines Formularfeldes nach dem Absenden anzeigen?", "Indem man `value` im Formularfeld ausgibt", "Indem man `value` an die URL anhängt", "Indem man `value` anzeigt", "Indem man `alert()` verwendet"),
        ("Welches HTML-Tag wird verwendet, um ein eingebettetes YouTube-Video hinzuzufügen?", "<iframe src='https://www.youtube.com/embed/...'>", "<video src='https://www.youtube.com/...'>", "<embed src='https://www.youtube.com/...'>", "<youtube src='https://www.youtube.com/...'>"),
        ("Welches HTML-Tag wird verwendet, um die Größe eines Bildes festzulegen?", "<img width='...' height='...'>", "<image size='...'/>", "<img src='...' size='...'>", "<image src='...' width='...' height='...'>"),
        ("Wie kann man das Zeichen `<` in HTML anzeigen, ohne dass es als Tag interpretiert wird?", "&lt;", "&gt;", "&amp;", "&copy;"),
        ("Welches HTML-Tag wird verwendet, um den Text als Fußnote darzustellen?", "<footer>", "<fn>", "<footnote>", "<note>"),
        ("Wie kann man das Verhalten eines Links in HTML ändern, sodass es nicht den aktuellen Tab verlässt?", "Durch Hinzufügen von `target='_self'`", "Durch Hinzufügen von `target='_blank'`", "Durch Entfernen des `href`-Attributs", "Durch Hinzufügen von `target='_new'`"),
    ]

class CSS:
    questions = [
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen den Inhalten eines Elements und seinem Rand festzulegen?", "padding", "margin", "border", "spacing"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen Elementen auf der Seite zu definieren?", "margin", "padding", "width", "height"),
        ("Mit welchem CSS-Selektor wählt man alle Elemente mit der Klasse 'example' aus?", ".example", "#example", "example", "<example>"),
        ("Wie setzt man die Hintergrundfarbe eines Elements in CSS?", "background-color: #fff;", "color: #fff;", "bg-color: #fff;", "background: #fff;"),
        ("Welches CSS-Attribut wird verwendet, um den Text in einer Schriftart darzustellen?", "font-family", "text-style", "font-size", "font-weight"),
        ("Wie kann man die Breite eines Elements in CSS auf 100% des Elternelements setzen?", "width: 100%;", "width: auto;", "width: inherit;", "width: 100px;"),
        ("Welches CSS-Attribut steuert die Transparenz eines Elements?", "opacity", "visibility", "transparent", "background-opacity"),
        ("Mit welchem CSS-Attribut setzt man den Abstand zwischen den Zeilen in einem Text?", "line-height", "text-indent", "letter-spacing", "word-spacing"),
        ("Wie setzt man einen runden Rahmen um ein Element in CSS?", "border-radius: 50%;", "border: round;", "border-style: rounded;", "border-radius: 10px;"),
        ("Welches CSS-Attribut wird verwendet, um Text fett darzustellen?", "font-weight: bold;", "font-style: bold;", "text-weight: bold;", "text-decoration: bold;"),
        ("Wie kann man ein Element in CSS verstecken?", "display: none;", "visibility: hidden;", "opacity: 0;", "all of the above"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen den Buchstaben eines Textes zu definieren?", "letter-spacing", "line-height", "word-spacing", "text-align"),
        ("Wie ändert man die Schriftgröße in CSS?", "font-size: 16px;", "text-size: 16px;", "font-style: 16px;", "text-font: 16px;"),
        ("Mit welchem CSS-Attribut wird der Text in einer bestimmten Farbe angezeigt?", "color", "background-color", "text-color", "font-color"),
        ("Welches CSS-Attribut wird verwendet, um die Position eines Elements relativ zum nächsten positionierten Vorfahren zu steuern?", "position", "z-index", "float", "top"),
        ("Wie macht man in CSS ein Element absolut positioniert?", "position: absolute;", "position: fixed;", "position: relative;", "position: static;"),
        ("Mit welchem CSS-Attribut kann man ein Element nach rechts verschieben?", "margin-left", "margin-right", "right", "left"),
        ("Wie setzt man eine Umrandung (Border) für ein Element in CSS?", "border: 1px solid #000;", "border-width: 1px;", "border-style: solid;", "border-color: #000;"),
        ("Mit welchem CSS-Attribut kann man den Text in einer Zeile zentrieren?", "text-align: center;", "align: center;", "text-position: center;", "line-align: center;"),
        ("Wie setzt man eine feste Höhe für ein Element in CSS?", "height: 100px;", "width: 100px;", "size: 100px;", "height: auto;"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen den Elementen eines flex containers zu definieren?", "justify-content", "align-items", "align-self", "flex-direction"),
        ("Wie kann man in CSS eine Dropdown-Liste erstellen?", "select { ... }", "dropdown { ... }", "input[type='dropdown'] { ... }", "menu { ... }"),
        ("Welches CSS-Attribut wird verwendet, um den Inhalt eines Elements horizontal zu zentrieren?", "margin: 0 auto;", "text-align: center;", "display: flex;", "align-items: center;"),
        ("Mit welchem CSS-Attribut wird die Position eines Elements relativ zum gesamten Dokument festgelegt?", "position: fixed;", "position: absolute;", "position: relative;", "position: static;"),
        ("Wie kann man den Text in einem Element so umbrechen, dass er innerhalb des Elements bleibt?", "word-wrap: break-word;", "word-break: break-all;", "white-space: normal;", "text-wrap: break-word;"),
        ("Mit welchem CSS-Attribut ändert man die Transparenz des Hintergrunds?", "background-color: rgba(255, 255, 255, 0.5);", "background-opacity: 0.5;", "background: transparent;", "opacity: 0.5;"),
        ("Welches CSS-Attribut wird verwendet, um die Höhe eines Elements automatisch anzupassen?", "height: auto;", "height: inherit;", "height: fit-content;", "height: initial;"),
        ("Mit welchem CSS-Attribut wird das Verhalten von Text bei Zeilenumbrüchen definiert?", "white-space", "line-height", "text-align", "word-spacing"),
        ("Wie kann man in CSS die Reihenfolge von Flex-Elementen ändern?", "order", "flex-order", "z-index", "position-order"),
        ("Welches CSS-Attribut wird verwendet, um die Schriftart eines Elements zu definieren?", "font-family", "font-style", "font-size", "font-weight"),
        ("Mit welchem CSS-Attribut kann man Text hervorheben, ohne die Farbe zu ändern?", "text-decoration: underline;", "text-transform: capitalize;", "font-weight: bold;", "letter-spacing: 2px;"),
        ("Wie lässt sich in CSS eine Box-Schatten-Effekte hinzufügen?", "box-shadow: 10px 10px 5px rgba(0,0,0,0.3);", "shadow-box: 10px 10px;", "text-shadow: 10px 10px 5px rgba(0,0,0,0.3);", "box-effect: shadow;"),
        ("Wie setzt man in CSS ein Layout, das sich automatisch an die Bildschirmgröße anpasst?", "media queries", "flexbox", "grid", "viewport"),
        ("Mit welchem CSS-Attribut kann man den Text in Kleinbuchstaben umwandeln?", "text-transform: lowercase;", "font-case: lowercase;", "text-case: lowercase;", "text-style: small;"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen den Zeilen eines Textes zu definieren?", "line-height", "letter-spacing", "word-spacing", "text-spacing"),
        ("Wie kann man ein Element mit CSS horizontal und vertikal im Viewport zentrieren?", "position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);", "display: flex; align-items: center; justify-content: center;", "position: relative; top: 50%; left: 50%;", "margin: 0 auto;"),
        ("Wie ändert man die Schriftart in CSS?", "font-family: 'Arial', sans-serif;", "text-font: 'Arial', sans-serif;", "font-type: 'Arial', sans-serif;", "font-style: 'Arial', sans-serif;"),
        ("Wie lässt sich der Abstand zwischen zwei Flexbox-Elementen steuern?", "justify-content", "align-items", "flex-direction", "gap"),
        ("Mit welchem CSS-Attribut kann man ein Element fixieren, sodass es immer an der gleichen Stelle bleibt, auch beim Scrollen?", "position: fixed;", "position: absolute;", "position: relative;", "position: sticky;"),
        ("Wie setzt man in CSS eine Dropdown-Liste so, dass sie beim Hover angezeigt wird?", "display: block;", "visibility: visible;", "position: absolute;", "display: inline-block;"),
        ("Mit welchem CSS-Attribut kann man verhindern, dass Text über das Ende eines Elements hinausgeht?", "overflow: hidden;", "text-overflow: ellipsis;", "white-space: nowrap;", "text-wrap: normal;"),
        ("Wie kann man das Flexbox-Layout so einstellen, dass sich die Elemente automatisch anordnen?", "flex-wrap: wrap;", "flex-direction: column;", "align-items: center;", "justify-content: space-between;"),
        ("Welches CSS-Attribut wird verwendet, um die Breite eines Elements relativ zur Breite seines Elternelements zu definieren?", "width: %;", "width: auto;", "width: fit-content;", "width: inherit;"),
        ("Wie kann man die Sichtbarkeit eines Elements beibehalten, aber es unsichtbar machen?", "visibility: hidden;", "opacity: 0;", "display: none;", "color: transparent;"),
        ("Welches CSS-Attribut wird verwendet, um die Höhe eines Elements auf 100% der Bildschirmhöhe zu setzen?", "height: 100vh;", "height: 100%;", "height: full;", "height: auto;"),
        ("Wie setzt man einen Text in CSS kursiv?", "font-style: italic;", "font-weight: italic;", "text-decoration: italic;", "font-transform: italic;"),
        ("Mit welchem CSS-Attribut kann man die Breite eines Elements auf die Breite seines Inhalts anpassen?", "width: auto;", "width: fit-content;", "width: inherit;", "width: stretch;"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen den Buchstaben eines Textes zu verändern?", "letter-spacing", "word-spacing", "line-height", "text-indent"),
        ("Wie macht man in CSS eine Box mit abgerundeten Ecken?", "border-radius", "border: rounded;", "corner-radius", "round-border"),
        ("Mit welchem CSS-Attribut kann man ein Element relativ zu seinem Elternelement positionieren?", "position: relative;", "position: fixed;", "position: absolute;", "position: sticky;"),
        ("Wie sorgt man dafür, dass ein Element in CSS immer auf der Seite sichtbar bleibt, wenn der Benutzer scrollt?", "position: fixed;", "position: sticky;", "position: absolute;", "position: relative;"),
        ("Mit welchem CSS-Attribut ändert man die Schriftgröße?", "font-size", "text-size", "font-weight", "text-style"),
        ("Welches CSS-Attribut wird verwendet, um Text in einem Element zentriert anzuzeigen?", "text-align: center;", "text-align: middle;", "align-text: center;", "center-text: true;"),
        ("Wie entfernt man die Standard-Listenkugeln einer ungeordneten Liste in CSS?", "list-style-type: none;", "list-type: none;", "list-decoration: none;", "list-style: none;"),
        ("Mit welchem CSS-Attribut kann man die Transparenz eines Hintergrunds einstellen?", "background-color: rgba(255, 255, 255, 0.5);", "background-color: transparent;", "background-opacity: 0.5;", "opacity: 0.5;"),
        ("Wie kann man verhindern, dass Text in einem Element überläuft?", "overflow: hidden;", "overflow: scroll;", "overflow: auto;", "word-wrap: break-word;"),
        ("Mit welchem CSS-Attribut wird der Abstand zwischen den Zellen in einer Tabelle festgelegt?", "border-spacing", "cell-spacing", "padding", "table-spacing"),
        ("Wie kann man die Reihenfolge von Elementen in einem Flexbox-Layout ändern?", "order", "flex-order", "z-index", "flex-reverse"),
        ("Welches CSS-Attribut wird verwendet, um das Verhalten von Elementen innerhalb eines flex containers entlang der Achse zu steuern?", "justify-content", "align-items", "flex-direction", "align-self"),
        ("Mit welchem CSS-Attribut wird der Abstand zwischen den Flex-Elementen in einem Flex-Container festgelegt?", "gap", "space-between", "align-items", "justify-items"),
        ("Wie ändert man die Schriftart für ein Element in CSS?", "font-family: 'Arial', sans-serif;", "font-style: 'Arial', sans-serif;", "font-type: 'Arial', sans-serif;", "font-text: 'Arial', sans-serif;"),
        ("Wie sorgt man dafür, dass sich die Höhe eines flex Containers an die darin enthaltenen Elemente anpasst?", "align-items: stretch;", "height: auto;", "align-items: flex-start;", "align-items: center;"),
        ("Wie fügt man ein Bild als Hintergrund in CSS ein?", "background-image: url('bild.jpg');", "image-background: url('bild.jpg');", "background: image('bild.jpg');", "background: url('bild.jpg');"),
        ("Mit welchem CSS-Attribut ändert man die Breite eines Bildes?", "width", "img-width", "image-size", "img-width: auto;"),
        ("Wie kann man verhindern, dass ein Element den gesamten Raum innerhalb eines Containers einnimmt, wenn es eine Flexbox ist?", "flex-shrink: 1;", "flex-grow: 0;", "flex: none;", "flex-basis: auto;"),
        ("Mit welchem CSS-Attribut sorgt man dafür, dass der Text in einem Element in Großbuchstaben angezeigt wird?", "text-transform: uppercase;", "font-transform: uppercase;", "text-style: uppercase;", "font-style: uppercase;"),
        ("Welches CSS-Attribut wird verwendet, um den Abstand zwischen dem Inhalt und dem Rand eines Elements zu steuern?", "padding", "margin", "border", "spacing"),
        ("Wie setzt man in CSS den Abstand zwischen einem Element und dem Rand seines Elternelements?", "margin", "padding", "border", "distance"),
        ("Mit welchem CSS-Attribut kann man ein Element so positionieren, dass es innerhalb eines flex Containers sowohl horizontal als auch vertikal zentriert wird?", "align-items: center; justify-content: center;", "justify-content: center;", "align-self: center;", "align-items: flex-start;"),
        ("Welches CSS-Attribut wird verwendet, um eine Box um ein Element zu zeichnen?", "border", "outline", "margin", "padding"),
        ("Wie setzt man eine animierte Bewegung für ein Element in CSS?", "animation", "transition", "keyframes", "motion"),
        ("Mit welchem CSS-Attribut kann man ein Element transparent machen?", "opacity", "visibility", "transparent", "hidden"),
        ("Wie lässt sich in CSS eine Textfarbe setzen?", "color", "font-color", "text-color", "background-color"),
        ("Mit welchem CSS-Attribut kann man die Textausrichtung innerhalb eines Containers steuern?", "text-align", "vertical-align", "text-position", "align-text"),
        ("Wie sorgt man dafür, dass ein Flex-Container seine Elemente gleichmäßig verteilt?", "justify-content: space-between;", "justify-content: flex-start;", "align-items: center;", "align-self: center;"),
        ("Welches CSS-Attribut wird verwendet, um den Hintergrund eines Elements mit einem Farbverlauf zu füllen?", "background: linear-gradient();", "background-color: gradient();", "background: gradient-color;", "gradient-background: true;"),
        ("Wie kann man in CSS verhindern, dass der Text von einem Element seine maximale Breite überschreitet?", "text-overflow: ellipsis;", "overflow: hidden;", "word-wrap: break-word;", "max-width: 100%;"),
        ("Mit welchem CSS-Attribut kann man ein Element als Flex-Container definieren?", "display: flex;", "display: grid;", "display: block;", "display: inline;"),
        ("Wie lässt sich in CSS eine Box-Schatten für ein Element hinzufügen?", "box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.3);", "shadow: 10px 10px 5px rgba(0, 0, 0, 0.3);", "background-shadow: rgba(0, 0, 0, 0.3);", "text-shadow: 10px 10px 5px rgba(0, 0, 0, 0.3);"),
        ("Wie kann man in CSS ein Element bei Hover-Ereignissen ändern?", "pseudo-classes: hover;", "style-on-hover;", "change-on-hover;", "onhover: style;"),
        ("Mit welchem CSS-Attribut können Links in einem Text deaktiviert werden?", "pointer-events: none;", "visibility: hidden;", "display: none;", "opacity: 0;"),
        ("Wie setzt man den Abstand zwischen den Spalten in einem CSS-Grid?", "grid-column-gap", "column-gap", "gap", "grid-gap"),
        ("Wie macht man in CSS ein Element vollständig transparent?", "opacity: 0;", "visibility: hidden;", "background-color: transparent;", "display: none;"),
        ("Mit welchem CSS-Attribut kann man in einem Flexbox-Layout die Position eines Elements horizontal und vertikal ausrichten?", "align-items: center; justify-content: center;", "align-self: center;", "flex-align: center;", "flex-position: center;"),
        ("Wie kann man den Abstand zwischen den Flex-Elementen innerhalb eines Flex-Containers erhöhen?", "gap: 20px;", "space-between: 20px;", "margin: 20px;", "padding: 20px;"),
        ("Wie ändert man die Schriftgröße eines Textes in CSS?", "font-size", "font-weight", "text-size", "font-style"),
        ("Mit welchem CSS-Attribut kann man die maximale Breite eines Elements festlegen?", "max-width", "min-width", "width", "fit-content"),
        ("Wie kann man in CSS ein Bild als Hintergrundbild für ein Element festlegen?", "background-image: url('bild.jpg');", "background: url('bild.jpg');", "image-background: url('bild.jpg');", "background: image('bild.jpg');"),
    ]

class PHP:
    questions = [
        ("Was ist der Zweck der Funktion `echo` in PHP?", "Um Text oder HTML auszugeben", "Um eine Datei zu öffnen", "Um eine Variable zu deklarieren", "Um eine Verbindung zur Datenbank herzustellen"),
        ("Welche Funktion wird verwendet, um eine Datei in PHP zu öffnen?", "fopen", "file_open", "open_file", "read_file"),
        ("Was ist der Unterschied zwischen `==` und `===` in PHP?", "`==` vergleicht nur den Wert, `===` vergleicht sowohl Wert als auch Typ", "`==` vergleicht Werte und Typen, `===` vergleicht nur Werte", "`==` ist ein logischer Operator, `===` ein Vergleichsoperator", "Kein Unterschied"),
        ("Wie kann man in PHP eine Variable definieren?", "$variable = Wert;", "variable $variable = Wert;", "var $variable = Wert;", "$variable := Wert;"),
        ("Welche Funktion wird verwendet, um den Wert einer Session-Variable zu setzen?", "$_SESSION['key'] = value;", "$SESSION['key'] = value;", "session_set('key', value);", "session('key', value);"),
        ("Wie fügt man in PHP eine neue Zeile zu einer Textdatei hinzu?", "file_put_contents('datei.txt', 'neuer Inhalt', FILE_APPEND);", "fwrite('datei.txt', 'neuer Inhalt');", "fopen('datei.txt', 'a');", "append('datei.txt', 'neuer Inhalt');"),
        ("Welche Funktion wird verwendet, um eine Verbindung zu einer MySQL-Datenbank in PHP herzustellen?", "mysqli_connect", "mysql_connect", "db_connect", "pdo_connect"),
        ("Was bedeutet `$_GET` in PHP?", "Es ist ein Array, das die Werte von URL-Parametern enthält", "Es ist ein Array, das Benutzereingaben enthält", "Es ist eine Funktion zur Datenbankabfrage", "Es ist ein globales Array für Sessions"),
        ("Wie erstellt man eine Schleife in PHP, die von 1 bis 10 zählt?", "for ($i = 1; $i <= 10; $i++)", "for ($i = 1; $i < 10; i++)", "for ($i = 1; $i != 10; $i++)", "foreach ($i = 1; $i <= 10; $i++)"),
        ("Wie kann man in PHP die Länge eines Strings herausfinden?", "strlen()", "str_length()", "count()", "length()"),
        ("Wie kann man einen Kommentar in PHP einfügen?", "// Kommentar", "/* Kommentar */", "# Kommentar", "Alle oben genannten"),
        ("Welche Funktion wird verwendet, um eine PHP-Variable in einen String umzuwandeln?", "strval()", "to_string()", "stringify()", "convert_to_string()"),
        ("Was passiert, wenn man auf eine nicht definierte PHP-Variable zugreift?", "Es gibt eine Warnung aus", "Es wird ein Fehler ausgelöst", "Es wird automatisch ein Wert zugewiesen", "Es passiert nichts"),
        ("Welche Funktion wird verwendet, um eine Datei in PHP zu schließen?", "fclose", "file_close", "close_file", "close()"),
        ("Was ist ein `foreach`-Loop in PHP?", "Ein Loop, der jedes Element in einem Array oder einer Liste durchläuft", "Ein Loop, der durch Zahlen von 1 bis N zählt", "Ein Loop, der eine Bedingung prüft", "Ein Loop, der auf den Wert einer Variablen prüft"),
        ("Wie kann man in PHP ein Formular-Input-Feld mit einem Standardwert füllen?", "value='Standardwert'", "default='Standardwert'", "input='Standardwert'", "value: 'Standardwert'"),
        ("Wie kann man in PHP den aktuellen Zeitpunkt in einem bestimmten Format ausgeben?", "date('Y-m-d H:i:s')", "time('Y-m-d H:i:s')", "get_date('Y-m-d H:i:s')", "current_time('Y-m-d H:i:s')"),
        ("Wie wird eine PHP-Datei auf dem Server ausgeführt?", "Durch Aufrufen der Datei über den Webserver", "Durch Ausführen des Befehls `php file.php`", "Durch Kompilieren der Datei", "Durch Einfügen in ein HTML-Dokument"),
        ("Was bedeutet `$_POST` in PHP?", "Es ist ein Array, das die Daten eines Formulars enthält, das mit der POST-Methode gesendet wurde", "Es ist ein Array, das die Session-Daten enthält", "Es ist eine Funktion zur Datenbankabfrage", "Es ist ein globales Array für URL-Parameter"),
        ("Wie kann man eine PHP-Funktion definieren?", "function funktionsname() { ... }", "def funktionsname() { ... }", "funct funktionsname() { ... }", "define funktionsname() { ... }"),
        ("Was ist eine `cookie` in PHP?", "Ein kleines Stück Daten, das im Browser des Benutzers gespeichert wird", "Ein Server, der Daten speichert", "Ein PHP-Array", "Ein globaler Speicher für Daten"),
        ("Wie macht man in PHP ein Array assoziativ?", "$array = ['key' => 'value'];", "$array = array('key' => 'value');", "array('key', 'value');", "$array = ['value' => 'key'];"),
        ("Welche Funktion in PHP wird verwendet, um Daten aus einer MySQL-Datenbank abzurufen?", "mysqli_query", "mysql_fetch", "mysql_select", "mysqli_fetch"),
        ("Wie kann man in PHP eine neue Datei erstellen?", "fopen('dateiname', 'w')", "file_create('dateiname')", "new_file('dateiname')", "file_open('dateiname')"),
        ("Welche PHP-Funktion wird verwendet, um den Inhalt einer Datei zu lesen?", "file_get_contents", "read_file", "file_read", "fget()"),
        ("Wie kann man in PHP eine Funktion mit einer variablen Anzahl von Argumenten erstellen?", "function myFunction(...$args)", "function myFunction($args*)", "function myFunction($args...)", "function myFunction($args, $more_args)"),
        ("Wie kann man den PHP-Fehlermodus auf 'Alle Fehler anzeigen' setzen?", "error_reporting(E_ALL);", "display_errors(true);", "show_errors(true);", "report_errors('ALL');"),
        ("Welche PHP-Funktion wird verwendet, um eine Weiterleitung auf eine andere Seite vorzunehmen?", "header('Location: seite.php');", "redirect('seite.php');", "go_to('seite.php');", "location('seite.php');"),
        ("Was ist der Unterschied zwischen `include` und `require` in PHP?", "`include` gibt eine Warnung aus, wenn die Datei nicht gefunden wird, `require` gibt einen Fehler aus", "`require` gibt eine Warnung aus, wenn die Datei nicht gefunden wird, `include` gibt einen Fehler aus", "`include` ist schneller als `require`", "Kein Unterschied"),
        ("Wie kann man eine PHP-Variable global verfügbar machen?", "global $variable;", "globalize($variable);", "export $variable;", "declare global $variable;"),
        ("Was ist der Standardwert von `$_SESSION` in PHP?", "Es ist ein assoziatives Array", "Es ist ein globales Objekt", "Es ist ein numerisches Array", "Es ist ein leeres String-Array"),
        ("Wie startet man in PHP eine Session?", "session_start();", "start_session();", "initialize_session();", "session_begin();"),
        ("Wie kann man in PHP die aktuelle Zeit im UNIX-Timestamp-Format erhalten?", "time();", "current_time();", "get_timestamp();", "unix_time();"),
        ("Wie ruft man in PHP die Datei-Informationen wie Größe und Änderungsdatum ab?", "stat('datei');", "file_info('datei');", "file_details('datei');", "get_file_info('datei');"),
        ("Wie gibt man in PHP die Werte eines Arrays aus?", "print_r($array);", "echo($array);", "print($array);", "array_print($array);"),
        ("Wie kann man in PHP ein Array sortieren?", "sort($array);", "array_sort($array);", "order_array($array);", "arrange($array);"),
        ("Was passiert, wenn `isset()` in PHP auf eine nicht definierte Variable angewendet wird?", "Es gibt `false` zurück", "Es gibt einen Fehler zurück", "Es gibt `null` zurück", "Es gibt `true` zurück"),
        ("Wie kann man in PHP den Wert einer Umgebungsvariable erhalten?", "getenv('VAR_NAME');", "env('VAR_NAME');", "get_variable('VAR_NAME');", "fetchenv('VAR_NAME');"),
        ("Wie kann man in PHP den Dateinamen einer Datei ohne Erweiterung erhalten?", "pathinfo($datei, PATHINFO_FILENAME);", "get_filename($datei);", "basename($datei, '.ext');", "strip_extension($datei);"),
        ("Was ist der Zweck der Funktion `exit()` in PHP?", "Beendet das Skript sofort", "Gibt eine Fehlermeldung aus", "Lädt eine neue Seite", "Stoppt die Schleife"),
        ("Welche PHP-Funktion wird verwendet, um ein Element aus einem Array zu entfernen?", "unset($array['key']);", "remove($array['key']);", "delete($array['key']);", "pop($array['key']);"),
        ("Wie kann man in PHP die Eingabe von Benutzern sicherstellen, um SQL-Injection zu verhindern?", "Mit `mysqli_real_escape_string()`", "Mit `htmlspecialchars()`", "Mit `addslashes()`", "Mit `filter_var()`"),
        ("Was ist der Zweck von `$_SERVER` in PHP?", "Es ist ein globales Array, das Server- und Umgebungsinformationen enthält", "Es ist ein globales Array für Session-Daten", "Es ist eine PHP-Funktion für Serverkommunikation", "Es speichert Benutzereingaben"),
        ("Wie löscht man in PHP eine Session-Variable?", "unset($_SESSION['variable']);", "delete($_SESSION['variable']);", "remove($_SESSION['variable']);", "destroy($_SESSION['variable']);"),
        ("Welche Funktion wird in PHP verwendet, um eine Datenbankverbindung zu schließen?", "mysqli_close", "db_close", "close_connection", "close_db"),
        ("Wie kann man in PHP den Wert einer Umgebungsvariable setzen?", "putenv('VAR_NAME=value');", "setenv('VAR_NAME', 'value');", "env_set('VAR_NAME', 'value');", "set_variable('VAR_NAME', 'value');"),
        ("Was bedeutet die Funktion `preg_match()` in PHP?", "Sie führt eine reguläre Ausdrucksprüfung durch", "Sie vergleicht zwei Strings", "Sie überprüft, ob eine Zahl größer als ein Wert ist", "Sie gibt den Index eines Elements zurück"),
        ("Wie kann man in PHP eine neue Zeile in einer Textdatei einfügen?", "fwrite($file, 'Text\n');", "file_put_contents($file, 'Text');", "append($file, 'Text');", "write_line($file, 'Text');"),
        ("Wie wird in PHP ein leeres Array erzeugt?", "$array = [];", "$array = array();", "$array = new array();", "$array = empty();"),
        ("Wie kann man eine HTTP-Anfrage in PHP senden?", "file_get_contents('url');", "http_request('url');", "fetch('url');", "curl('url');"),
        ("Welche Funktion wird verwendet, um den Wert einer POST-Variable in PHP zu erhalten?", "$_POST['key'];", "post('key');", "fetch_post('key');", "get_post('key');"),
        ("Was ist der Unterschied zwischen `$_SESSION` und `$_COOKIE` in PHP?", "`$_SESSION` speichert Daten serverseitig, während `$_COOKIE` clientseitig gespeichert wird", "`$_SESSION` speichert Daten clientseitig, während `$_COOKIE` serverseitig gespeichert wird", "`$_SESSION` speichert nur Login-Daten, `$_COOKIE` speichert alle Daten", "Es gibt keinen Unterschied"),
        ("Wie kann man in PHP eine Umleitung zu einer anderen Seite durchführen?", "header('Location: neuerPfad');", "redirect('neuerPfad');", "go_to('neuerPfad');", "location_change('neuerPfad');"),
        ("Was ist die Funktion `isset()` in PHP?", "Überprüft, ob eine Variable gesetzt und nicht null ist", "Erstellt eine neue Variable", "Löscht eine Variable", "Gibt den Wert einer Variablen zurück"),
        ("Wie kann man in PHP eine Schleife für jedes Element in einem Array ausführen?", "foreach ($array as $value) { ... }", "for ($i = 0; $i < count($array); $i++) { ... }", "while ($array) { ... }", "do { ... } while ($array);"),
        ("Welche Funktion gibt den aktuellen Unix-Timestamp in PHP zurück?", "time();", "timestamp();", "get_timestamp();", "current_time();"),
        ("Was bedeutet `$_SERVER['REQUEST_METHOD']` in PHP?", "Es gibt den HTTP-Methoden-Typ der Anfrage zurück (z. B. GET oder POST)", "Es gibt die URL der Anfrage zurück", "Es gibt den Hostnamen des Servers zurück", "Es gibt die HTTP-Header zurück"),
        ("Wie kann man in PHP eine Umgebungsvariable für das gesamte Skript setzen?", "putenv('VAR=value');", "setenv('VAR=value');", "env('VAR=value');", "set_variable('VAR=value');"),
        ("Was ist die Funktion `exit()` in PHP?", "Beendet das Skript und gibt optional einen Statuscode zurück", "Lädt eine neue Seite", "Beendet die Schleife", "Stoppt die Verbindung zur Datenbank"),
        ("Welche Funktion wird in PHP verwendet, um alle Elemente eines Arrays in eine Zeichenkette zu verbinden?", "implode()", "join()", "array_to_string()", "concat()"),
        ("Was bedeutet `$_FILES` in PHP?", "Es enthält die Daten von hochgeladenen Dateien", "Es enthält die Formulardaten", "Es enthält Benutzereingaben", "Es enthält Session-Daten"),
        ("Welche Funktion wird verwendet, um eine Variable in PHP zu speichern?", "serialize()", "store()", "save()", "persist()"),
        ("Was passiert, wenn `$_POST` für eine nicht gesetzte Variable in PHP verwendet wird?", "Es gibt `null` zurück", "Es gibt einen Fehler aus", "Es gibt `false` zurück", "Es gibt eine Warnung aus"),
        ("Wie kann man die Größe eines Arrays in PHP ermitteln?", "count($array);", "size($array);", "array_size($array);", "length($array);"),
        ("Welche PHP-Funktion wird verwendet, um die Dateityp-Erweiterung eines Dateinamens zu erhalten?", "pathinfo($filename, PATHINFO_EXTENSION);", "get_extension($filename);", "file_extension($filename);", "get_filetype($filename);"),
        ("Wie kann man in PHP einen Fehlerbericht unterdrücken?", "@fopen('datei.txt', 'r');", "@echo $variable;", "error_report('none');", "suppress_error('fopen');"),
        ("Welche PHP-Funktion wird verwendet, um einen neuen Datensatz in eine MySQL-Datenbank einzufügen?", "mysqli_insert", "mysqli_query", "mysqli_exec", "mysqli_insert_id"),
        ("Welche PHP-Funktion wird verwendet, um alle Einträge aus einer MySQL-Datenbanktabelle zu holen?", "mysqli_fetch_assoc", "mysqli_fetch_row", "mysqli_fetch_all", "mysqli_select"),
        ("Wie erhält man in PHP den aktuellen Server-IP-Adresse?", "$_SERVER['SERVER_ADDR'];", "$_SERVER['REMOTE_ADDR'];", "$_SERVER['HOST'];", "$_SERVER['SERVER_NAME'];"),
        ("Wie wird ein PHP-Skript in eine HTML-Datei eingebettet?", "<?php ... ?>", "<script php> ... </script>", "<php> ... </php>", "<code> ... </code>"),
        ("Wie kann man in PHP einen Wert in einer Datenbanktabelle aktualisieren?", "UPDATE table SET column='value' WHERE condition", "ALTER table UPDATE column SET value", "UPDATE table SET value WHERE column", "INSERT INTO table VALUES()"),
        ("Was passiert, wenn man `$_GET` auf eine nicht definierte Variable in PHP verwendet?", "Es gibt `null` zurück", "Es gibt `false` zurück", "Es gibt `undefined` zurück", "Es gibt einen Fehler aus"),
        ("Wie kann man in PHP ein Array in einen JSON-String umwandeln?", "json_encode($array);", "json_decode($array);", "array_to_json($array);", "json_stringify($array);"),
        ("Wie kann man in PHP eine URL weiterleiten?", "header('Location: url');", "redirect('url');", "url_redirect('url');", "go_to('url');"),
        ("Wie wird in PHP eine Datei hochgeladen?", "$_FILES", "$_UPLOAD", "$_POST", "$_FILE"),
        ("Welche Funktion wird verwendet, um eine Zeitverzögerung in PHP zu verursachen?", "sleep();", "wait();", "pause();", "delay();"),
        ("Welche Funktion wird in PHP verwendet, um den aktuellen Monat zu erhalten?", "date('m');", "get_month();", "current_month();", "month_now();"),
        ("Was gibt `count()` in PHP zurück?", "Die Anzahl der Elemente in einem Array", "Die Länge eines Strings", "Die Anzahl der Zeichen in einem Array", "Die Anzahl der Variablen in einem Array"),
        ("Was ist die Aufgabe der Funktion `session_destroy()` in PHP?", "Löscht die Session-Daten und schließt die Sitzung", "Zerstört alle Variablen", "Löscht alle Cookies", "Löscht die Datenbankverbindung"),
        ("Wie kann man eine MySQL-Datenbankverbindung in PHP herstellen?", "$conn = mysqli_connect('host', 'user', 'password', 'dbname');", "$conn = new mysqli('host', 'user', 'password', 'dbname');", "$conn = db_connect('host', 'user', 'password', 'dbname');", "$conn = open_mysql('host', 'user', 'password', 'dbname');"),
        ("Wie kann man in PHP eine neue Klasse erstellen?", "class MyClass { ... }", "new class MyClass { ... }", "create class MyClass { ... }", "define class MyClass { ... }"),
        ("Was macht die Funktion `uniqid()` in PHP?", "Generiert eine einzigartige ID basierend auf der aktuellen Zeit", "Gibt eine zufällige ID zurück", "Generiert eine ID aus einem String", "Erzeugt eine zufällige Zahl"),
        ("Welche Funktion wird verwendet, um ein Formular in PHP zu verarbeiten?", "$_POST", "$_GET", "submit()", "handle_form()"),
        ("Wie lässt sich in PHP eine Variable an eine Funktion übergeben?", "Durch Wertübergabe", "Durch Referenzübergabe", "Beide Methoden", "Mit einer Rückgabewerte"),
        ("Wie kann man einen Wert in PHP in eine CSV-Datei speichern?", "fputcsv($file, $array);", "csv_write($file, $array);", "write_csv($file, $array);", "array_to_csv($file, $array);"),
        ("Wie wird in PHP eine Datei geöffnet?", "fopen('dateiname', 'modus');", "open_file('dateiname', 'modus');", "file_open('dateiname', 'modus');", "open('dateiname');"),
        ("Was bedeutet die PHP-Variable `$_SERVER['PHP_SELF']`?", "Der Pfad zur aktuellen Datei", "Der Name der aktuellen Datei", "Die IP-Adresse des Servers", "Die URL der aktuellen Seite"),
        ("Welche Funktion gibt den Inhalt einer Datei in PHP zurück?", "file_get_contents('dateiname');", "read_file('dateiname');", "get_file_contents('dateiname');", "file_read('dateiname');"),
        ("Welche Funktion wird in PHP verwendet, um ein Array in einen String zu konvertieren?", "implode()", "merge()", "concat()", "join()"),
        ("Wie kann man den aktuellen Benutzernamen in PHP abrufen?", "get_current_user();", "user();", "current_user();", "whoami();"),
        ("Welche Funktion wird verwendet, um in PHP eine Datei zu löschen?", "unlink()", "delete()", "remove()", "destroy()"),
        ("Wie kann man in PHP eine Session starten?", "session_start();", "start_session();", "init_session();", "begin_session();"),
        ("Welche Funktion gibt die aktuelle Uhrzeit in PHP zurück?", "date('H:i:s');", "current_time();", "get_time();", "now();"),
        ("Wie kann man in PHP einen HTTP-Header senden?", "header('HTTP/1.1 200 OK');", "send_header('HTTP/1.1 200 OK');", "send_http('200 OK');", "header_send('200 OK');"),
        ("Wie wird ein Wert in einer PHP-Session gespeichert?", "$_SESSION['key'] = value;", "$_SESSION(key) = value;", "session_set('key', value);", "set_session('key', value);"),
        ("Wie kann man in PHP den Dateityp einer Datei überprüfen?", "mime_content_type();", "file_type();", "fileinfo();", "get_file_type();"),
        ("Was ist der Zweck von `require_once()` in PHP?", "Stellt sicher, dass eine Datei nur einmal eingebunden wird", "Lädt eine Datei in einem bestimmten Modus", "Inkludiert eine Datei nur, wenn sie existiert", "Erstellt eine neue Datei"),
        ("Wie kann man in PHP alle Elemente eines Arrays löschen?", "unset($array);", "delete($array);", "clear($array);", "remove($array);"),
        ("Welche Funktion wird verwendet, um alle Zeichen aus einem String zu entfernen?", "trim();", "strip_tags();", "clean();", "sanitize();"),
        ("Wie können in PHP Cookies gesetzt werden?", "setcookie('name', 'value');", "cookie('name', 'value');", "set_cookie('name', 'value');", "cookie_set('name', 'value');"),
        ("Welche Funktion überprüft, ob eine Variable in PHP gesetzt ist?", "isset();", "exists();", "defined();", "variable_exists();"),
        ("Was bedeutet `$_POST` in PHP?", "Es enthält Daten aus einem HTML-Formular, das mit der POST-Methode gesendet wurde", "Es enthält die URL-Parameter", "Es speichert Sitzungsvariablen", "Es speichert Cookies"),
        ("Wie kann man in PHP die maximale Größe einer Datei für den Upload begrenzen?", "max_file_size = ini_set('upload_max_filesize', '10M');", "file_upload_size = 10M;", "set_upload_size(10);", "file_limit(10M);"),
        ("Welche Funktion wird verwendet, um in PHP eine Datei zu öffnen?", "fopen();", "file_open();", "open_file();", "file_read();"),
        ("Welche PHP-Funktion wird verwendet, um eine Zeichenkette zu entschlüsseln?", "openssl_decrypt();", "decrypt_string();", "string_decrypt();", "decode_string();"),
        ("Wie kann man den Inhalt eines Textfeldes in einem Formular in PHP lesen?", "$_POST['fieldname'];", "$_GET['fieldname'];", "$_FORM['fieldname'];", "$_REQUEST['fieldname'];"),
        ("Welche Funktion gibt die Länge eines Strings in PHP zurück?", "strlen();", "string_length();", "length();", "char_count();"),
        ("Wie kann man in PHP eine Datei schreiben?", "fwrite($file, 'Text');", "file_put_contents('dateiname', 'Text');", "write_file('dateiname', 'Text');", "file_write('dateiname', 'Text');"),
        ("Welche Funktion prüft, ob eine Datei in PHP existiert?", "file_exists();", "is_file();", "file_check();", "check_file();"),
        ("Was passiert, wenn man `$_FILES` auf eine nicht existierende Datei verwendet?", "Es gibt `null` zurück", "Es gibt eine Fehlermeldung", "Es gibt eine leere Antwort", "Es gibt den Dateinamen zurück"),
    ]

class XML_JSON_AJAX_DOM:
    questions = [
        # XML Fragen
        ("Was ist XML?", "Eine Markup-Sprache für die Strukturierung von Daten", "Ein Datenbank", "Eine Programmiersprache", "Ein Textformat für HTML"),
        ("Welches Zeichen wird in XML verwendet, um ein Element zu schließen?", "</>", "</element>", "</>", "<element/>"),
        ("Was ist das grundlegende Strukturmerkmal einer XML-Datei?", "Tags und Attribute", "JSON-Objekte", "HTML-Tags", "SQL-Abfragen"),
        ("Welches Attribut wird verwendet, um eine XML-Deklaration hinzuzufügen?", "<?xml version='1.0' encoding='UTF-8'?>", "<!DOCTYPE xml>", "<xml version='1.0'>", "<xml declaration='1.0'>"),
        ("Welches XML-Element enthält Informationen über die Version der XML-Daten?", "<?xml>", "<xml>", "<version>", "<data>"),
        ("Was beschreibt die DTD (Document Type Definition) in einer XML-Datei?", "Die Syntaxregeln und die Struktur der XML-Daten", "Das Styling der XML-Daten", "Die URL der XML-Datenquelle", "Den Namen des XML-Dokuments"),
        ("Welches Element in einer XML-Datei dient dazu, benutzerdefinierte Daten hinzuzufügen?", "<data>", "<user>", "<element>", "<attribute>"),
        ("Welches Tool wird verwendet, um XML-Daten zu validieren?", "XSD (XML Schema Definition)", "CSS", "HTML5", "SQL"),
        ("Was passiert, wenn ein XML-Dokument nicht gut geformt ist?", "Es gibt einen Fehler und kann nicht geladen werden", "Es wird von Webbrowsern ignoriert", "Es wird automatisch korrigiert", "Es wird als HTML interpretiert"),
        ("Welches ist das grundlegende Attribut einer XML-Datei, um die Struktur zu definieren?", "xmlns", "schema", "encoding", "DOCTYPE"),
                ("Welches Tag wird verwendet, um Kommentare in einer XML-Datei zu schreiben?", 
         "<!-- Kommentar -->", 
         "/* Kommentar */", 
         "// Kommentar", 
         "# Kommentar"),
        
        ("Was ist der Zweck einer DTD in XML?", 
         "Es definiert die Struktur und Regeln des XML-Dokuments", 
         "Es stellt sicher, dass XML korrekt formatiert ist", 
         "Es speichert alle XML-Daten", 
         "Es speichert die XML-Datei auf dem Server"),

        ("Wie erstellt man in XML ein Attribut?", 
         "Tagname='Wert'", 
         "<attribute='Wert'>", 
         "<tag value='Wert'>", 
         "Tagname['Wert']"),

        ("Was bedeutet der Fehler 'unterbrochene Entität' in XML?", 
         "Ein Tag oder eine Entität wurde nicht korrekt geschlossen", 
         "Die DTD ist nicht vorhanden", 
         "Es gibt ein ungültiges Attribut", 
         "Es fehlt ein schließendes Zeichen für ein Tag"),

        ("Welche der folgenden ist kein gültiger XML-Datentyp?", 
         "Boolean", 
         "Integer", 
         "DateTime", 
         "Double"),

        ("Welches Tag wird verwendet, um einen Namespace in XML zu deklarieren?", 
         "xmlns", 
         "namespace", 
         "xmlns:prefix", 
         "namespace:uri"),

        ("Welcher XML-Parser unterstützt die DTD-Validierung?", 
         "SAX", 
         "DOM", 
         "Expat", 
         "Minidom"),

        ("Was ist die Funktion von `CDATA` in XML?", 
         "Es schützt den Inhalt vor der Interpretion als XML-Tag", 
         "Es speichert Daten als binäre Informationen", 
         "Es sorgt dafür, dass Daten verschlüsselt werden", 
         "Es speichert Kommentare"),

        ("Was ist der Hauptunterschied zwischen XML und JSON?", 
         "XML verwendet Tags, JSON verwendet Schlüssel-Wert-Paare", 
         "XML verwendet nur Text, JSON unterstützt auch Arrays", 
         "XML ist ein binäres Format, JSON ist ein Textformat", 
         "XML ist schneller zu verarbeiten als JSON"),

        ("Was passiert, wenn ein XML-Dokument keine gültige DTD hat?", 
         "Es kann nicht validiert werden", 
         "Es wird ignoriert", 
         "Es wird von HTML verarbeitet", 
         "Es wird automatisch korrigiert"),

                 ("Welche der folgenden Aussagen beschreibt die XML-Syntax?", 
         "XML ist case-sensitiv und muss korrekt geschlossene Tags haben", 
         "XML ist nicht case-sensitiv", 
         "XML benötigt keine Tags", 
         "XML kann doppelte Tags enthalten"),

        ("Welches Tag ist in einer XML-Datei immer erforderlich?", 
         "Ein Root-Element", 
         "Ein Kommentar-Tag", 
         "Ein schließendes Tag", 
         "Ein DTD-Tag"),

        ("Welches Attribut wird verwendet, um die Version von XML zu deklarieren?", 
         "version", 
         "type", 
         "encoding", 
         "namespace"),

        ("Welche der folgenden Optionen ist ein gültiges XML-Element?", 
         "<name>Wert</name>", 
         "<name Wert>", 
         "<name WERT>", 
         "<name>Wert"),

        ("Was ist die Bedeutung des `<?xml ... ?>`-Tags in XML?", 
         "Es kennzeichnet die XML-Deklaration", 
         "Es dient als Kommentar", 
         "Es beschreibt die DTD", 
         "Es stellt einen Namespace dar"),
        
        # JSON Fragen
        ("Was ist JSON?", "Ein Textformat für Datenübertragung", "Ein HTML-Element", "Ein Datenbankmanagement-System", "Ein Programmiersprachen-Parser"),
        ("Wie sieht die Grundstruktur eines JSON-Objekts aus?", "Schlüssel-Wert-Paare innerhalb von geschweiften Klammern {}", "Listen innerhalb von runden Klammern ()", "Werte in einer durch Kommas getrennten Zeile", "Attribute innerhalb von eckigen Klammern []"),
        ("Welches der folgenden ist eine gültige JSON-Datenstruktur?", '{"name": "John", "age": 30}', '{name: "John", age: 30}', '"name": "John", "age": 30', '("name": "John", "age": 30)'),
        ("Welche der folgenden Datentypen können in JSON verwendet werden?", "Strings, Arrays, Objekte", "Nur Strings", "Nur Zahlen", "Nur Objekte"),
        ("Was ist der Unterschied zwischen JSON und XML?", "JSON ist einfacher und leichter zu lesen", "XML kann nur Text speichern, JSON kann auch Bilder speichern", "XML ist effizienter bei der Datenübertragung", "JSON unterstützt keine Arrays"),
        ("Wie repräsentiert JSON ein Array?", "Mit eckigen Klammern []", "Mit geschweiften Klammern {}", "Mit runden Klammern ()", "Mit Anführungszeichen ''"),
        ("Wie schließt man ein JSON-Objekt ab?", "Mit einer schließenden geschweiften Klammer }", "Mit einer schließenden runden Klammer )", "Mit einer schließenden eckigen Klammer ]", "Mit einem Semikolon ;"),
        ("Wie fügt man in JSON einen neuen Wert zu einem bestehenden Objekt hinzu?", "Indem man das Schlüssel-Wert-Paar hinzufügt", "Indem man das Array erweitert", "Indem man das Objekt neu definiert", "Indem man das Attribut überschreibt"),
        ("Was passiert, wenn ein ungültiges JSON-Format übermittelt wird?", "Es führt zu einem Fehler", "Es wird automatisch repariert", "Es wird ignoriert", "Es wird als String behandelt"),
        ("Was ist die maximale Anzahl der verschachtelten JSON-Objekte?", "Es gibt keine feste Grenze", "10", "100", "1000"),
                ("Wie wird in JSON ein Array dargestellt?", 
         "Mit eckigen Klammern []", 
         "Mit geschweiften Klammern {}", 
         "Mit runden Klammern ()", 
         "Mit Anführungszeichen ' '"),

        ("Welche der folgenden Werte sind in JSON nicht gültig?", 
         "Function", 
         "Boolean", 
         "Number", 
         "String"),

        ("Welcher Datentyp wird in JSON nicht unterstützt?", 
         "Funktionen", 
         "Strings", 
         "Objekte", 
         "Arrays"),

        ("Wie wird ein Objekt in JSON definiert?", 
         "Schlüssel-Wert-Paare in geschweiften Klammern", 
         "Mit einer Liste von Werten", 
         "Mit Anführungszeichen", 
         "Mit eckigen Klammern"),

        ("Was ist der Unterschied zwischen JSON und JavaScript-Objekten?", 
         "JSON ist ein Datenaustauschformat, JavaScript-Objekte sind Programmiersprachenobjekte", 
         "JSON ist langsamer als JavaScript", 
         "JavaScript-Objekte sind stringbasiert, JSON ist binär", 
         "JSON kann keine Arrays enthalten"),

        ("Was passiert, wenn JSON ungültige Syntax hat?", 
         "Es führt zu einem Fehler", 
         "Es wird automatisch repariert", 
         "Es wird als String behandelt", 
         "Es wird ignoriert"),

        ("Was ist die Bedeutung des `parse()`-Methodenaufrufs in JSON?", 
         "Es analysiert JSON-Daten in JavaScript-Objekte", 
         "Es konvertiert JavaScript-Objekte in JSON", 
         "Es prüft die Struktur von JSON-Daten", 
         "Es speichert JSON-Daten in einer Datei"),

        ("Welche der folgenden Zeichen sind nicht in einem JSON-Schlüssel zulässig?", 
         "Komma", 
         "Doppelpunkt", 
         "Anführungszeichen", 
         "Semikolon"),

        ("Welches der folgenden Formate ist kein JSON-kompatibles Datentyp?", 
         "Funktionen", 
         "Array", 
         "String", 
         "Zahl"),

                 ("Welches Format wird in JSON verwendet, um Schlüssel-Wert-Paare darzustellen?", 
         "Doppelpunkt (:) zwischen Schlüssel und Wert", 
         "Komma zwischen Schlüssel und Wert", 
         "Semikolon zwischen Schlüssel und Wert", 
         "Klammern zwischen Schlüssel und Wert"),

        ("Welcher der folgenden Datentypen wird in JSON nicht unterstützt?", 
         "Function", 
         "Array", 
         "String", 
         "Number"),

        ("Wie wird in JSON eine Zahl dargestellt?", 
         "Als Ganzzahl oder Dezimalzahl", 
         "Als String", 
         "Als Array", 
         "Als Boolean"),

        ("Was muss bei der Verwendung von JSON-Objekten beachtet werden?", 
         "Schlüssel müssen als Strings angegeben werden", 
         "Werte dürfen keine Arrays enthalten", 
         "Die Schlüssel dürfen keine Leerzeichen enthalten", 
         "Objekte müssen mit Semikolons getrennt sein"),

        ("Wie wird ein JSON-Dokument gültig formatiert?", 
         "Schlüssel und Werte müssen in Anführungszeichen gesetzt werden", 
         "Der JSON-Inhalt muss in geschweifte Klammern eingeschlossen werden", 
         "Es müssen mindestens drei Schlüssel-Wert-Paare vorhanden sein", 
         "JSON benötigt keine Klammern"),
        
        # AJAX Fragen
        ("Was bedeutet AJAX?", "Asynchronous JavaScript and XML", "Active JavaScript and XHTML", "Asynchronous JSON and XML", "All JavaScript and XML"),
        ("Welche Methode wird in AJAX verwendet, um Daten asynchron zu laden?", "XMLHttpRequest", "fetch()", "getElementById()", "load()"),
        ("Was ist der Hauptvorteil von AJAX?", "Ermöglicht das Laden von Daten ohne die Seite neu zu laden", "Erhöht die Ladegeschwindigkeit der Seite", "Verringert die Serverlast", "Ermöglicht die Synchronisation von Daten in Echtzeit"),
        ("Welche HTTP-Methoden können in AJAX verwendet werden?", "GET, POST, PUT, DELETE", "GET, POST", "POST, PATCH", "GET"),
        ("Wie ruft man in AJAX eine Funktion nach dem erfolgreichen Laden der Daten auf?", "Indem man die `onload`-Eigenschaft verwendet", "Indem man die `onreadystatechange`-Eigenschaft verwendet", "Indem man die `complete`-Eigenschaft verwendet", "Indem man `then()` verwendet"),
                ("Welches der folgenden Attribute ist erforderlich, um eine AJAX-Anfrage mit `XMLHttpRequest` zu initiieren?", 
         "open()", 
         "send()", 
         "getElementById()", 
         "request()"),

        ("Welche HTTP-Methode wird typischerweise verwendet, um Daten in einer AJAX-Anfrage zu senden?", 
         "POST", 
         "GET", 
         "PUT", 
         "DELETE"),

        ("Wie kann man in JavaScript auf den Erfolg einer AJAX-Anfrage reagieren?", 
         "Mit der `onload`-Eigenschaft", 
         "Mit der `onSuccess`-Eigenschaft", 
         "Mit der `then()`-Methode", 
         "Mit der `callback`-Funktion"),

        ("Was bedeutet 'Asynchronous' in AJAX?", 
         "Daten werden ohne Neuladen der Seite im Hintergrund geladen", 
         "Daten werden sofort auf der Seite angezeigt", 
         "Daten werden synchron geladen und blockieren die Benutzeroberfläche", 
         "Daten werden in einer Schleife geladen"),

        ("Welche der folgenden Funktionen gehört zur AJAX-Syntax in JavaScript?", 
         "XMLHttpRequest.send()", 
         "fetch.send()", 
         "ajax.sendRequest()", 
         "request.send()"),

                 ("Was ist der Zweck von AJAX?", 
         "Ermöglicht asynchrone Kommunikation zwischen dem Client und dem Server", 
         "Ermöglicht die Synchronisierung von Daten zwischen Client und Server", 
         "Verhindert das Neuladen der Seite", 
         "Speichert Daten lokal im Browser"),

        ("Welche der folgenden HTTP-Methoden wird häufig in einer AJAX-Anfrage verwendet?", 
         "GET", 
         "POST", 
         "PUT", 
         "DELETE"),

        ("Was passiert bei einem erfolgreichen AJAX-Request?", 
         "Die `onload`-Funktion wird aufgerufen", 
         "Die Seite wird neu geladen", 
         "Es wird ein Fehler angezeigt", 
         "Die Anfrage wird automatisch abgebrochen"),

        ("Wie kann man mit AJAX Daten an den Server senden?", 
         "Mit der `send()`-Methode", 
         "Mit der `get()`-Methode", 
         "Mit der `submit()`-Methode", 
         "Mit der `load()`-Methode"),

        ("Welcher Typ von HTTP-Anfragen wird typischerweise in einer AJAX-Anwendung verwendet?", 
         "Asynchrone Anfragen", 
         "Senkrechte Anfragen", 
         "Synchrone Anfragen", 
         "Abgebrochene Anfragen"),
        
        # DOM Fragen
        ("Was bedeutet DOM?", "Document Object Model", "Data Object Model", "Direct Object Model", "Document Online Model"),
        ("Welches JavaScript-Objekt ermöglicht den Zugriff auf HTML-Dokumente?", "document", "html", "window", "body"),
        ("Wie kann man ein neues HTML-Element mit JavaScript im DOM hinzufügen?", "document.createElement('element');", "document.addElement('element');", "document.insert('element');", "document.append('element');"),
        ("Wie kann man in JavaScript auf den Inhalt eines Elements im DOM zugreifen?", "element.innerHTML", "element.content", "element.value", "element.textContent"),
        ("Wie entfernt man ein Element aus dem DOM?", "element.remove();", "document.removeElement();", "document.deleteChild();", "element.delete();"),
                ("Wie kann man in JavaScript auf ein DOM-Element zugreifen?", 
         "Mit document.getElementById()", 
         "Mit document.createElement()", 
         "Mit document.querySelector()", 
         "Mit document.getElementsByTagName()"),

        ("Wie erstellt man ein neues DOM-Element in JavaScript?", 
         "Mit document.createElement()", 
         "Mit document.createTextNode()", 
         "Mit document.createTag()", 
         "Mit document.insertElement()"),

        ("Was ist der Zweck der `innerHTML`-Eigenschaft?", 
         "Sie gibt den HTML-Inhalt eines Elements zurück oder setzt ihn", 
         "Sie gibt den Textinhalt eines Elements zurück", 
         "Sie erstellt neue HTML-Tags", 
         "Sie gibt die Attribute eines Elements zurück"),

        ("Welche Methode entfernt ein DOM-Element?", 
         "remove()", 
         "delete()", 
         "destroy()", 
         "discard()"),

        ("Wie kann man den Textinhalt eines DOM-Elements ändern?", 
         "element.textContent = 'Neuer Text'", 
         "element.innerHTML = 'Neuer Text'", 
         "element.value = 'Neuer Text'", 
         "element.setAttribute('text', 'Neuer Text')"),

                 ("Welches der folgenden DOM-Methoden gibt den Textinhalt eines Elements zurück?", 
         "textContent", 
         "getElementById", 
         "innerHTML", 
         "setAttribute"),

        ("Wie kann man ein DOM-Element erstellen?", 
         "Mit `document.createElement()`", 
         "Mit `document.createTextNode()`", 
         "Mit `document.getElementById()`", 
         "Mit `document.createNode()`"),

        ("Wie wird der Wert eines `input`-Feldes im DOM ausgelesen?", 
         "Mit `element.value`", 
         "Mit `element.textContent`", 
         "Mit `element.innerHTML`", 
         "Mit `element.setAttribute()`"),

        ("Wie kann man ein DOM-Element aus dem Dokument entfernen?", 
         "Mit `removeChild()`", 
         "Mit `deleteChild()`", 
         "Mit `destroyChild()`", 
         "Mit `removeElement()`"),

        ("Welches DOM-Objekt repräsentiert das HTML-Dokument?", 
         "document", 
         "window", 
         "body", 
         "html"),

        ("Welche Methode wird verwendet, um auf das erste Element eines Dokuments zuzugreifen?", 
         "getElementsByTagName()", 
         "querySelectorAll()", 
         "getElementById()", 
         "createElement()"),

        ("Welche DOM-Methode wird verwendet, um einen neuen Knoten an das Ende eines anderen Elements anzufügen?", 
         "appendChild()", 
         "insertBefore()", 
         "removeChild()", 
         "setAttribute()"),

        ("Wie kann man alle Elemente eines bestimmten Typs im DOM finden?", 
         "Mit `document.getElementsByTagName()`", 
         "Mit `document.querySelectorAll()`", 
         "Mit `document.getElementById()`", 
         "Mit `document.createElement()`"),

        ("Was ist der Unterschied zwischen `innerHTML` und `textContent`?", 
         "`innerHTML` gibt HTML-Inhalte zurück, `textContent` gibt nur Text zurück", 
         "`textContent` gibt HTML-Inhalte zurück, `innerHTML` gibt nur Text zurück", 
         "`innerHTML` entfernt die HTML-Tags, `textContent` fügt sie hinzu", 
         "`textContent` ist schneller als `innerHTML`"),

        ("Wie kann man in JavaScript die Attribute eines DOM-Elements ändern?", 
         "Mit `setAttribute()`", 
         "Mit `getAttribute()`", 
         "Mit `changeAttribute()`", 
         "Mit `alterAttribute()`"),
    ]

class Javascript:
    questions = [
        ("Welche der folgenden Methoden wird verwendet, um eine Variable in JavaScript zu deklarieren?", 
         "var", 
         "let", 
         "const", 
         "define"),

        ("Wie wird eine Funktion in JavaScript definiert?", 
         "function name() {}", 
         "def name() {}", 
         "func name() {}", 
         "create name() {}"),

        ("Was wird durch den `typeof`-Operator in JavaScript zurückgegeben?", 
         "Den Datentyp eines Werts", 
         "Den Wert eines Objekts", 
         "Den Namen einer Variablen", 
         "Den Wert eines Funktionsaufrufs"),

        ("Welche der folgenden Schleifen gibt es in JavaScript?", 
         "for", 
         "foreach", 
         "do-while", 
         "repeat-until"),

        ("Wie können Sie ein Element aus einem Array in JavaScript entfernen?", 
         "array.pop()", 
         "array.remove()", 
         "array.delete()", 
         "array.shift()"),

        ("Was gibt die `NaN`-Eigenschaft in JavaScript an?", 
         "Not-a-Number", 
         "Not-a-Null", 
         "Negative-Number", 
         "Negative-Null"),

        ("Welche Methode kann verwendet werden, um das Hinzufügen von Ereignissen in JavaScript zu ermöglichen?", 
         "addEventListener()", 
         "attachEvent()", 
         "onEvent()", 
         "eventListener()"),

        ("Welche der folgenden Optionen ist die richtige Methode, um einen Wert in einer Konsole auszugeben?", 
         "console.log()", 
         "print()", 
         "alert()", 
         "echo()"),

        ("Was macht der `push()`-Befehl in JavaScript?", 
         "Fügt ein Element an das Ende eines Arrays an", 
         "Fügt ein Element an den Anfang eines Arrays an", 
         "Entfernt das letzte Element eines Arrays", 
         "Entfernt das erste Element eines Arrays"),

        ("Wie erstellt man ein leeres Objekt in JavaScript?", 
         "var obj = {}", 
         "var obj = []", 
         "var obj = null", 
         "var obj = ''"),

        ("Was passiert, wenn man den Operator `==` in JavaScript verwendet?", 
         "Vergleicht die Werte, ohne den Typ zu berücksichtigen", 
         "Vergleicht den Typ und den Wert", 
         "Vergleicht nur den Wert", 
         "Vergleicht die Referenz von Objekten"),

        ("Wie wird ein String in JavaScript in Kleinbuchstaben umgewandelt?", 
         "string.toLowerCase()", 
         "string.toLower()", 
         "string.toLowercase()", 
         "string.toSmall()"),

        ("Welche der folgenden Anweisungen ist korrekt, um eine Klasse in JavaScript zu definieren?", 
         "class MyClass {}", 
         "function MyClass {}", 
         "define MyClass {}", 
         "class: MyClass {}"),

        ("Welche Methode wird verwendet, um den Index eines Elements in einem Array zu finden?", 
         "indexOf()", 
         "find()", 
         "search()", 
         "positionOf()"),

        ("Was wird durch die Methode `Array.isArray()` in JavaScript zurückgegeben?", 
         "Wahr, wenn es sich um ein Array handelt", 
         "Falsch, wenn es sich um ein Array handelt", 
         "Den Index des Arrays", 
         "Den Typ des Arrays"),

        ("Was ist `this` in JavaScript?", 
         "Ein Verweis auf das aktuelle Objekt", 
         "Ein Schlüsselwort, um die aktuelle Funktion zu benennen", 
         "Der globale Kontext", 
         "Der Funktionsname"),

        ("Wie erstellt man eine anonyme Funktion in JavaScript?", 
         "function() {}", 
         "anonymous()", 
         "fn() {}", 
         "function anonymous() {}"),

        ("Welche der folgenden Aussagen beschreibt den Unterschied zwischen `let` und `var`?", 
         "`let` hat Blockscope, `var` hat Funktionsscope", 
         "`var` hat Blockscope, `let` hat Funktionsscope", 
         "`var` ist immer global", 
         "`let` ist immer global"),

        ("Wie wird die Länge eines Arrays in JavaScript ermittelt?", 
         "array.length", 
         "array.size", 
         "array.count", 
         "array.length()"),

        ("Welche der folgenden Funktionen kann verwendet werden, um einen Wert von einer Webseite in JavaScript zu erhalten?", 
         "document.getElementById()", 
         "document.querySelector()", 
         "document.getElementByName()", 
         "document.select()"),

        ("Wie gibt man die erste Zahl in einem Array von Zahlen in JavaScript aus?", 
         "console.log(array[0])", 
         "console.log(array[1])", 
         "console.log(array.first())", 
         "console.log(array.firstNumber())"),

        ("Wie entfernt man Leerzeichen am Anfang und Ende eines Strings in JavaScript?", 
         "string.trim()", 
         "string.strip()", 
         "string.cut()", 
         "string.remove()"),

                 ("Was bedeutet der Operator `===` in JavaScript?", 
         "Vergleicht sowohl den Wert als auch den Typ", 
         "Vergleicht nur den Wert", 
         "Vergleicht nur den Typ", 
         "Überprüft, ob zwei Objekte gleich sind"),

        ("Welche Methode wird verwendet, um den aktuellen Wert einer Eingabebox zu erhalten?", 
         "input.value", 
         "input.text", 
         "input.get()", 
         "input()"),

        ("Was wird durch den `break`-Befehl in einer Schleife bewirkt?", 
         "Beendet die Schleife", 
         "Setzt die Schleife fort", 
         "Springt zum nächsten Durchlauf", 
         "Bricht den gesamten Code ab"),

        ("Welche der folgenden Methoden fügt ein Element an das Ende eines Arrays in JavaScript an?", 
         "push()", 
         "add()", 
         "append()", 
         "insert()"),

        ("Wie kann eine Funktion in JavaScript an eine Variable zugewiesen werden?", 
         "var func = function() {}", 
         "function func = {}", 
         "func() = function {}", 
         "let func() = {}"),

        ("Welche der folgenden Methoden gibt den letzten Index eines bestimmten Werts in einem Array zurück?", 
         "lastIndexOf()", 
         "indexOf()", 
         "findLast()", 
         "findIndex()"),

        ("Was ist die Rückgabe von `typeof null` in JavaScript?", 
         "object", 
         "null", 
         "undefined", 
         "NaN"),

        ("Welche Methode wird verwendet, um ein Element aus einer Liste von DOM-Elementen zu entfernen?", 
         "removeChild()", 
         "deleteChild()", 
         "removeElement()", 
         "remove()"),

        ("Was bedeutet `NaN` in JavaScript?", 
         "Not-a-Number", 
         "Null-and-Nothing", 
         "Not-a-Negative", 
         "Not-a-Name"),

        ("Wie erstellt man ein Set in JavaScript?", 
         "let set = new Set()", 
         "let set = []", 
         "let set = {} ", 
         "let set = Set()"),

        ("Welche der folgenden Anweisungen wird verwendet, um eine Fehlerbehandlung durchzuführen?", 
         "try-catch", 
         "throw-catch", 
         "catch-throw", 
         "catch-try"),

        ("Wie wird der Wert eines Attributs in JavaScript geändert?", 
         "element.setAttribute()", 
         "element.changeAttribute()", 
         "element.updateAttribute()", 
         "element.setAttributeValue()"),

        ("Welche Methode wird verwendet, um das erste Element eines Arrays zu entfernen?", 
         "shift()", 
         "pop()", 
         "removeFirst()", 
         "delete()"),

        ("Was ist die Funktion von `JSON.parse()` in JavaScript?", 
         "Parst einen JSON-String in ein JavaScript-Objekt", 
         "Gibt einen JSON-String zurück", 
         "Überprüft, ob ein String gültiges JSON ist", 
         "Konnvertiert ein JavaScript-Objekt in JSON"),

        ("Wie kann man ein Objekt in JavaScript in einen String umwandeln?", 
         "JSON.stringify()", 
         "JSON.parse()", 
         "object.toString()", 
         "object.stringify()"),

        ("Was gibt die Methode `Array.concat()` in JavaScript zurück?", 
         "Ein neues Array, das die Elemente beider Arrays enthält", 
         "Den Index des ersten Arrays", 
         "Die Länge des Arrays", 
         "Eine Kopie des ersten Arrays"),

        ("Wie kann man in JavaScript ein Ereignis auf ein Element binden?", 
         "element.addEventListener()", 
         "element.bind()", 
         "element.on()", 
         "element.listen()"),

        ("Was ist der Unterschied zwischen `let` und `const` in JavaScript?", 
         "`let` kann neu zugewiesen werden, `const` nicht", 
         "`const` ist immer lokal, `let` ist global", 
         "`const` ist nur für Arrays, `let` für alle Datentypen", 
         "`let` ist für Funktionen, `const` für Objekte"),

        ("Wie ruft man eine Eigenschaft eines Objekts in JavaScript auf?", 
         "obj.property", 
         "obj.getProperty()", 
         "obj['property']", 
         "obj->property"),

        ("Welche Methode wird verwendet, um die Elemente eines Arrays in JavaScript zu sortieren?", 
         "sort()", 
         "order()", 
         "arrange()", 
         "setOrder()"),

        ("Was ist `localStorage` in JavaScript?", 
         "Speichert Daten lokal im Browser", 
         "Speichert Daten auf dem Server", 
         "Speichert Daten global", 
         "Speichert Daten temporär während einer Sitzung"),

                 ("Welche Methode wird verwendet, um alle Elemente aus einem Array zu entfernen?", 
         "array.length = 0", 
         "array.clear()", 
         "array.pop()", 
         "array.shift()"),

        ("Wie können Sie auf ein DOM-Element mit der `id` 'myElement' zugreifen?", 
         "document.getElementById('myElement')", 
         "document.getElementByClassName('myElement')", 
         "document.querySelector('#myElement')", 
         "document.getElementByName('myElement')"),

        ("Welche Methode wird verwendet, um ein Array in JavaScript in umgekehrter Reihenfolge zu sortieren?", 
         "reverse()", 
         "sort()", 
         "invert()", 
         "arrange()"),

        ("Welche Methode gibt `true` zurück, wenn eine Variable `null` ist?", 
         "variable === null", 
         "variable == null", 
         "isNull(variable)", 
         "nullCheck(variable)"),

        ("Wie gibt man den `JSON`-Inhalt eines Objekts in einen String um?", 
         "JSON.stringify(object)", 
         "JSON.parse(object)", 
         "object.toJSON()", 
         "object.JSON()"),

        ("Welche Methode gibt das erste Vorkommen eines Werts in einem Array zurück?", 
         "indexOf()", 
         "findIndex()", 
         "search()", 
         "locate()"),

        ("Was macht der `setTimeout()`-Befehl in JavaScript?", 
         "Verzögert die Ausführung eines Codes für eine bestimmte Zeit", 
         "Führt den Code sofort aus", 
         "Stoppt die Ausführung des Codes", 
         "Setzt eine Schleife mit einer Verzögerung fort"),

        ("Welche Methode wird verwendet, um einen Wert von einer Webseite in JavaScript zu setzen?", 
         "element.value = 'newValue'", 
         "element.setValue('newValue')", 
         "element.setText('newValue')", 
         "element.text = 'newValue'"),

        ("Wie kann man in JavaScript die Schleifensteuerung abbrechen?", 
         "break", 
         "continue", 
         "exit", 
         "stop"),

        ("Welche Methode verwendet man, um die Anzahl der Elemente in einem Array zu ermitteln?", 
         "array.length", 
         "array.count()", 
         "array.size()", 
         "array.items()"),

        ("Wie kann man den Fehler in einem JavaScript-Programm auffangen?", 
         "try-catch", 
         "if-else", 
         "throw-catch", 
         "error-handle"),

        ("Wie kann man einen neuen leeren Array in JavaScript erstellen?", 
         "let arr = []", 
         "let arr = {}", 
         "let arr = Array()", 
         "let arr = new Array()"),

        ("Was gibt die Methode `toFixed()` in JavaScript zurück?", 
         "Einen String mit einer bestimmten Anzahl Dezimalstellen", 
         "Eine Zahl ohne Dezimalstellen", 
         "Einen Integer-Wert", 
         "Die gerundete Zahl"),

        ("Wie ruft man das erste Element in einem Array von Objekten auf?", 
         "array[0]", 
         "array[1]", 
         "array.first()", 
         "array.at(0)"),

        ("Was gibt der Befehl `NaN == NaN` in JavaScript zurück?", 
         "false", 
         "true", 
         "undefined", 
         "NaN"),

        ("Was ist der Unterschied zwischen `==` und `===` in JavaScript?", 
         "`==` vergleicht nur den Wert, `===` vergleicht auch den Typ", 
         "`===` vergleicht nur den Wert, `==` vergleicht auch den Typ", 
         "`===` vergleicht auch den Wert, `==` nicht", 
         "`==` und `===` haben keine Unterschiede"),

        ("Welche der folgenden Methoden wird verwendet, um ein Array in JavaScript zu verbinden?", 
         "concat()", 
         "combine()", 
         "join()", 
         "merge()"),

        ("Welche der folgenden Aussagen beschreibt korrekt, was `window.localStorage` ist?", 
         "Es speichert Daten lokal im Browser, auch nach einem Seitenreload", 
         "Es speichert Daten temporär während einer Sitzung", 
         "Es speichert Daten nur für eine bestimmte Zeit", 
         "Es speichert Daten nur auf der Serverseite"),

        ("Was passiert, wenn man `parseInt('10.5')` in JavaScript ausführt?", 
         "Es gibt 10 zurück", 
         "Es gibt 10.5 zurück", 
         "Es gibt '10.5' zurück", 
         "Es gibt null zurück"),

        ("Wie erstellt man ein neues leeres Set in JavaScript?", 
         "let mySet = new Set()", 
         "let mySet = []", 
         "let mySet = {}", 
         "let mySet = Set()"),

                 ("Was bedeutet der Befehl `const` in JavaScript?", 
         "Deklariert eine Konstante, deren Wert nicht geändert werden kann", 
         "Deklariert eine Variable, deren Wert später geändert werden kann", 
         "Erstellt eine neue Funktion", 
         "Deklariert eine Klasse"),

        ("Welche Methode wird verwendet, um eine neue Eigenschaft zu einem Objekt hinzuzufügen?", 
         "obj.property = value", 
         "obj.addProperty(value)", 
         "obj.setProperty(value)", 
         "obj.appendProperty(value)"),

        ("Wie können Sie in JavaScript eine Funktion mit einem Rückgabewert deklarieren?", 
         "function myFunc() { return value; }", 
         "function myFunc { value; }", 
         "myFunc() => { value; }", 
         "function myFunc() => value;"),

        ("Welche Methode wird verwendet, um alle Elemente eines Arrays zu löschen?", 
         "array.splice(0, array.length)", 
         "array.removeAll()", 
         "array.clear()", 
         "array.delete()"),

        ("Was passiert, wenn man `null == undefined` in JavaScript vergleicht?", 
         "Es ergibt `true`", 
         "Es ergibt `false`", 
         "Es wirft einen Fehler", 
         "Es ergibt `undefined`"),

        ("Was ist der Unterschied zwischen `let` und `var`?", 
         "`let` hat blockscope, während `var` function scope hat", 
         "`var` hat blockscope, während `let` function scope hat", 
         "`let` ist nur für Arrays, `var` für Objekte", 
         "`let` ist schneller als `var`"),

        ("Wie kann man ein Event-Listener für ein Element hinzufügen?", 
         "element.addEventListener('event', callback)", 
         "element.on('event', callback)", 
         "element.addEvent('event', callback)", 
         "element.attachEvent('event', callback)"),

        ("Welche Methode gibt `true` zurück, wenn das Objekt einen bestimmten Schlüssel hat?", 
         "obj.hasOwnProperty('key')", 
         "obj.contains('key')", 
         "obj.checkKey('key')", 
         "obj.isKeyPresent('key')"),

        ("Was gibt die Methode `Array.isArray()` zurück?", 
         "True, wenn es sich um ein Array handelt", 
         "False, wenn es kein Array ist", 
         "True, wenn es ein Objekt ist", 
         "False, wenn es eine Zahl ist"),

        ("Wie kann man eine zufällige Zahl zwischen 1 und 100 erzeugen?", 
         "Math.floor(Math.random() * 100) + 1", 
         "Math.random() * 100", 
         "Math.random(1, 100)", 
         "Math.random(1) * 100"),

        ("Wie kann man einen JSON-String in ein JavaScript-Objekt umwandeln?", 
         "JSON.parse(jsonString)", 
         "JSON.convert(jsonString)", 
         "JSON.toObject(jsonString)", 
         "JSON.stringify(jsonString)"),

        ("Welche Methode gibt die Anzahl der Elemente in einem Set zurück?", 
         "set.size", 
         "set.length", 
         "set.count()", 
         "set.getCount()"),

        ("Wie ruft man den ersten Wert eines Arrays in JavaScript auf?", 
         "array[0]", 
         "array.first()", 
         "array.get(0)", 
         "array.at(0)"),

        ("Wie kann man den Wert einer Eigenschaft eines Objekts ändern?", 
         "obj.property = newValue", 
         "obj.changeProperty(newValue)", 
         "obj.setProperty(newValue)", 
         "obj.updateProperty(newValue)"),

        ("Wie können Sie die maximale Zahl in einem Array finden?", 
         "Math.max(...array)", 
         "array.max()", 
         "array.getMax()", 
         "Math.max(array)"),

        ("Welche Methode wird verwendet, um den Wert eines Parameters aus der URL zu extrahieren?", 
         "new URLSearchParams(window.location.search).get('param')", 
         "window.location.getParameter('param')", 
         "window.location.searchParam('param')", 
         "window.getQuery('param')"),

        ("Was gibt `undefined` in JavaScript zurück?", 
         "Es ist der Wert einer nicht zugewiesenen Variable", 
         "Es ist der Wert einer nicht existierenden Funktion", 
         "Es ist der Wert einer nicht gefundenen Eigenschaft", 
         "Es ist eine spezielle Datenstruktur"),

        ("Wie kann man den aktuellen Datumswert in JavaScript anzeigen?", 
         "new Date()", 
         "Date.now()", 
         "currentDate()", 
         "getCurrentDate()"),

        ("Welche Methode wird verwendet, um ein Array zu sortieren?", 
         "array.sort()", 
         "array.order()", 
         "array.arrange()", 
         "array.sortValues()"),

        ("Wie kann man in JavaScript eine unendliche Schleife erzeugen?", 
         "while(true) {}", 
         "for(;;) {}", 
         "loop { ... }", 
         "repeat { ... }")
    ]



import random

class Quiz:
    # Die verfügbaren Kategorien
    categories = [
        ("JavaScript", Javascript),
        ("XML_JSON_AJAX_DOM", XML_JSON_AJAX_DOM),
        ("PHP", PHP),
        ("CSS", CSS),
        ("HTML", HTML)
    ]


    def __init__(self):
        self.score = 0
        self.total_questions = 50  # Hier auf 50 stellen
        self.selected_categories = []  # Liste der vom Benutzer ausgewählten Kategorien

    def show_categories(self):
        print("Verfügbare Kategorien:")
        for idx, (name, _) in enumerate(self.categories, 1):
            print(f"{idx}. {name}")

    def select_categories(self):
        self.show_categories()

        # Benutzereingabe für Kategorien
        selected = input(
            "Wählen Sie die Kategorien, aus denen Fragen kommen sollen (z.B. 1, 3, 5 für mehrere Kategorien): ")
        selected_indexes = [int(x.strip()) - 1 for x in selected.split(",") if x.strip().isdigit()]


        # Die ausgewählten Kategorien hinzufügen
        self.selected_categories = [self.categories[i][1] for i in selected_indexes]

        if not self.selected_categories:
            print("Keine gültigen Kategorien ausgewählt. Standardkategorien werden verwendet.")
            self.selected_categories = [category[1] for category in self.categories]  # Alle Kategorien verwenden

    def start(self):
        print("Willkommen zum IT-Quiz!")

        # Den Benutzer nach den Kategorien fragen
        self.select_categories()

        # Pool aller Fragen aus den ausgewählten Kategorien zusammenstellen
        questions_pool = []
        for category in self.selected_categories:
            questions_pool.extend(category.questions)

        # Wenn weniger als 50 Fragen im Pool sind, wird der Pool auf die vorhandene Anzahl begrenzt
        num_questions = min(self.total_questions, len(questions_pool))

        # 50 zufällige Fragen aus dem Pool auswählen
        selected_questions = random.sample(questions_pool, num_questions)

        # Die ausgewählten Fragen durchgehen
        for i in range(num_questions):
            q, correct, *wrong = selected_questions[i]
            answers = [correct] + wrong
            random.shuffle(answers)

            print(f"\nFrage {i + 1}: {q}")
            for j, answer in enumerate(answers, 1):
                print(f"{j}. {answer}")

            # Schleife bis eine gültige Eingabe erfolgt
            while True:
                try:
                    choice = int(input("Ihre Wahl (1-4): "))

                    # Sicherstellen, dass die Eingabe zwischen 1 und 4 liegt
                    if 1 <= choice <= 4:
                        if answers[choice - 1] == correct:
                            print("Richtig!")
                            self.score += 1
                        else:
                            print(f"Falsch! Die richtige Antwort war: {correct}")
                        break  # Bei einer gültigen Antwort aus der Schleife heraus
                    else:
                        print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")
                except (ValueError, IndexError):
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")

        self.calculate_grade()

    def calculate_grade(self):
        percentage = (self.score / self.total_questions) * 100
        if percentage >= 90:
            grade = "1.0"
        elif percentage >= 80:
            grade = "2.0"
        elif percentage >= 70:
            grade = "3.0"
        elif percentage >= 60:
            grade = "4.0"
        else:
            grade = "5.0"

        print(f"\nQuiz beendet! Sie haben {self.score}/{self.total_questions} Fragen richtig beantwortet.")
        print(f"Ihre Note: {grade}")


# Quiz starten
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()