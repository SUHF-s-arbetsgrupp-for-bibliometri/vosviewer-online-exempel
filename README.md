# vosviewer-online-exempel
Kodfragment till "Nätverksvisualisering med VOSviewer" 2023-12-15. Se först VOSviewer online - exempel.pptx.
<p>
<b>AddToVOSViewerNetwork.py</b> används för att läsa in ett nätverk i <a href="https://app.vosviewer.com/docs/file-types/json-file-type">JSON-format</a> (exporterat från VOSViewer) med syfte att exemplifiera hur information kan adderas till såväl klusternivå som till enskilda noder.
</p>

<p>Övriga filer:</p>
<ul>
  <li><b>ExampleNetwork.json</b> - 978 publikationer från Institutionen för datavetenskap vid UmU. Kluster skapade på basis av gemensamma referenser och termer från titel och abstract. Här en partitionering bestående av 16 kluster.</li>
  <li><b>clusterInfo.txt</b> - En beskrivning av varje kluster.</li>
  <li><b>itemInfo.txt</b> - Information rörande varje enskild nod, här ScopusID och titel. ID används för att generera länkar in till Scopus.</li>
  <li><b><a href="https://rawcdn.githack.com/SUHF-s-arbetsgrupp-for-bibliometri/vosviewer-online-exempel/fb48deca601414399780833d39fda731d1886a1b/index.html">index.html</a></b> - HTML-fil där vi använder VOSViewer online för att rendera ExampleNetwork.json och EampleNetworkAugmented.json</li>		
</ul>


<pre><code>usage: AddToVOSViewerNetwork.py [-h] -i INPUTNETWORK -o OUTPUTNETWORK -ci CLUSTERINFO -ii ITEMINFO

Add information to a VOSViewer file.
options:
  -h, --help            show this help message and exit
  -i INPUTNETWORK, --inputNetwork INPUTNETWORK
                        Input VOSViewer JSON network file
  -o OUTPUTNETWORK, --outputNetwork OUTPUTNETWORK
                        Output augmented VOSViewer JSON network file
  -ci CLUSTERINFO, --clusterInfo CLUSTERINFO
                        tab-separated txt-file, cluster level information
  -ii ITEMINFO, --itemInfo ITEMINFO
                        tab-separated txt-file. item level information</code></pre>
	
	
<pre><code>python AddToVOSViewerNetwork.py -i ExampleNetwork.json -o ExampleNetworkAugmented.json -ii itemInfo.txt -ci clusterInfo.txt	</code></pre>

<p>Övrigt:</p>

<ol type="a">
  <li>Som framgår av index.html så är det inte nödvändigt att ha en egen instans av VOSViewer online om man så inte önskar ("installerad på egen server"). Det går vidare bra att lagra JSON-filerna på vanliga molntjänster som t.ex. OneDrive. Detta kombinerat med att vi bäddar in renderingarna med s.k. Iframes gör att de flesta borde kunna använda sig av ett dylikt upplägg då det inte krävs någon speciell åtkomst till IT-infrastruktur (utöver möjligheten att redigera HTML-sidor)</li>
  <li>VOSviewer online är ofta ett utmärkt verktyg för att visualisera olika nätverk oavsett hur dessa skapats. Säg att nätverket konstruerats i en pipeline, partitioneringen (klustren) i en annan och koordinaterna i 2D-rymden i en tredje. Så länge denna information representeras enligt det aktuella JSON-formatet så kan VOSviewer online användas för att tillgängliggöra det hela för tredje part.</li>
  <li>Dokumentation och beskrivning av JSON-formatet finns <a href="https://app.vosviewer.com/docs/file-types/json-file-type">här</a>.</li>
</ol>  
