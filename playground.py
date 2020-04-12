import requests
import pandas as pd
from bs4 import BeautifulSoup
import js2py

# url = 'https://www.metal-archives.com/lists'
# # Create a handle, page, to handle the contents of the website
# page = requests.get(url)
# # Store the contents of the website under doc
# doc = lh.fromstring(page.content)
# # Parse data that are stored between <tr>..</tr> of HTML
# tr_elements = doc.xpath('//tr')
html_doc = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>A - Browse bands by letter - Encyclopaedia Metallum: The Metal Archives</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" type="text/css" href="/min/index.php?g=css" />
<script type="26a2292990d794eecd39b95e-text/javascript" src="/min/index.php?g=js"></script>
<script type="26a2292990d794eecd39b95e-text/javascript">
			var URL_SITE	= 'https://www.metal-archives.com/';
			var URL_IMAGES	= 'https://www.metal-archives.com/images/';
			var URL_CSS		= 'https://www.metal-archives.com/css/';
			var csrfToken	= '';

			$(document).ready(function() {
				toggleFixedPositioning(1280, 600);
				executeOnAllPages();

											});


		</script>
<noscript>
			<style type="text/css">
				.no-js { display: block !important; }
			</style>
		</noscript>
<!--[if lt IE 8]>
			<script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script>
			 <link rel="stylesheet" type="text/css" href="https://www.metal-archives.com/css/default/oldie.css" />
		<![endif]-->
<script type="26a2292990d794eecd39b95e-text/javascript">
			  var _gaq = _gaq || [];
			  _gaq.push(['_setAccount', 'UA-4046749-4']);
			  _gaq.push(['_trackPageview']);

			  (function() {
			    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			  })();
		</script>
</head>
<body>
<div id="wrapper">
<div id="header">
<a href="https://www.metal-archives.com/" id="MA_logo">Metal Archives</a>
<div class="clear loading"><img src="https://www.metal-archives.com/images/loading.gif" alt="loading" width="12" height="12" /> loading...</div>
<div id="search_box">
<form id="search_form" action="https://www.metal-archives.com/search" method="get">
<div>
<label>Search:</label><br />
<input name="searchString" type="text" id="searchQueryBox" size="25" value="" tabindex="1" />
<select name="type" tabindex="2">
<option value="band_name">Band name</option>
<option value="band_genre">Music genre</option>
<option value="band_themes">Lyrical themes</option>
<option value="album_title">Album title</option>
<option value="song_title">Song title</option>
<option value="label_name">Label</option>
<option value="artist_alias">Artist</option>
<option value="user_name">User profile</option>
<option value="google">Google</option>
</select>
<br />
<a href="https://www.metal-archives.com/search/advanced/?searchString=&type=" class="float_left" tabindex="4">Advanced search</a>
<button type="submit" class="btn_submit float_right" tabindex="3">Submit</button>
</div>
</form>
</div>
<div id="top_menu_box">
<ul class="menu_style_1">
<li><a href="https://www.metal-archives.com/content/help">Help</a></li>
<li><a href="https://www.metal-archives.com/content/rules">Rules</a></li>
<li><a href="https://www.metal-archives.com/board/" target="_top">Forum</a></li>
</ul>
<ul class="menu_style_2">
<li><a href="https://www.metal-archives.com/content/faq">FAQ</a></li>
<li><a href="https://www.metal-archives.com/content/support">Support Us</a></li>
<li><a href="https://www.metal-archives.com/content/tools">Add-ons</a></li>
</ul>
</div>
</div>
<div id="left_col">
<div id="member_box">
<form name="login_form" id="login_form" action="https://www.metal-archives.com/authentication/login" method="post">
<div>
<label>Username</label><br />
<input type="text" name="loginUsername" />
<label>Password</label><br />
<input type="password" name="loginPassword" />
<input type="hidden" name="origin" value="" />
<button type="submit" class="btn_login float_right">Login</button>
</div>
</form>
<a href="https://www.metal-archives.com/user/signup" class="float-left writeAction">Register</a>
<span class="float_right"><a href="https://www.metal-archives.com/user/forgot-password" class="float-left writeAction">Forgot login?</a> </span>
<div class="clear"> </div>
</div>
<div id="left_menu_box">
<ul class="menu_style_3 block_spacer_20">
<li>
Bands
<ul>
<li><a href="https://www.metal-archives.com/browse/letter">alphabetical</a></li>
<li><a href="https://www.metal-archives.com/browse/country">country</a></li>
<li><a href="https://www.metal-archives.com/browse/genre">genre</a></li>
</ul>
</li>
<li>
Labels
<ul>
<li><a href="https://www.metal-archives.com/label">alphabetical</a></li>
<li><a href="https://www.metal-archives.com/label/country">country</a></li>
</ul>
</li>
<li><a href="https://www.metal-archives.com/review/browse">Reviews</a></li>
</ul>
<ul class="menu_style_3 block_spacer_20">
<li><a href="https://www.metal-archives.com/artist/rip">R.I.P.</a></li>
<li><a href="https://www.metal-archives.com/band/random">Random Band</a></li>
<li><a href="https://www.metal-archives.com/user/list">User rankings</a></li>
<li><a href="https://www.metal-archives.com/news">News archive</a></li>
</ul>
<ul class="menu_style_3 ornement_30">
<li><a href="https://www.metal-archives.com/report/list">Reports</a></li>
<li><a href="https://www.metal-archives.com/todo">Contribute / To do</a></li>
</ul>
</div>
<div id="left_text_box">
<p class="small_text center"> &copy; 2002-2020<br />Encyclopaedia Metallum </p>
<p class="small_text center">Best viewed<br /> <a href="http://www.getfirefox.com" target="_blank">without</a> Internet Explorer, <br />in 1280 x 960 resolution<br /> or higher.</p>
</div>
<div>
<p class="small_text center"><a href="https://www.metal-archives.com/content/pp">Privacy Policy</a></p>
</div>
</div>
<div id="content_wrapper">
<script type="26a2292990d794eecd39b95e-text/javascript" src="https://www.metal-archives.com/js/jquery/jquery.dataTables.min.js"></script>
<h1 class="page_title">Browse Bands - Alphabetically - A </h1>

<div id="letterMenu" class="list_menu">
<ul class="menu_style_6">
<li class="active">
A
</li>
<li>
<a href="https://www.metal-archives.com/lists/B">B</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/C">C</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/D">D</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/E">E</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/F">F</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/G">G</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/H">H</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/I">I</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/J">J</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/K">K</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/L">L</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/M">M</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/N">N</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/O">O</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/P">P</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/Q">Q</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/R">R</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/S">S</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/T">T</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/U">U</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/V">V</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/W">W</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/X">X</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/Y">Y</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/Z">Z</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/NBR">#</a>
</li>
<li>
<a href="https://www.metal-archives.com/lists/~">~</a>
</li>
</ul>
</div>
<div class="clear">
<div class="dataTables_wrapper">
<table id="bandListAlpha" class="display" cellspacing="0">
<thead>
<tr>
<th>Band</th>
<th>Country</th>
<th>Genre</th>
<th>Status</th>
</tr>
</thead>
<tbody>
</tbody>
<tfoot>
<tr>
<th>Band</th>
<th>Country</th>
<th>Genre</th>
<th>Status</th>
</tr>
</tfoot>
</table>
</div>
<script type="26a2292990d794eecd39b95e-text/javascript">
			var grid = createGrid("#bandListAlpha", 500, 'browse/ajax-letter/l/A/json/1', { aoColumns: [ null, null, null, { bSortable: false, sWidth: '80px' } ] });
					</script>
</div>
</div>
</div>
<script src="https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js" data-cf-settings="26a2292990d794eecd39b95e-|49" defer=""></script></body>
</html>"""

soup = BeautifulSoup(html_doc, 'html.parser')

allHrefs = soup.find_all('a')

# for link in allHrefs:
#     print(link.get('href'))

allHrefs = [link.get('href') for link in allHrefs]

allListHrefs = [a for a in allHrefs if '/lists/' in a]
allListHrefs.append('https://www.metal-archives.com/lists/A')  # TODO: Why isn't A in the list of hrefs?

# for link in allListHrefs:
#     print(link)


mpla = '!function(){"use strict";function t(){return"cf-marker-"+Math.random().toString().slice(2)}function e(){for(' \
       'var t=[],e=0;e<arguments.length;e++)t[e]=arguments[e];(n=console.warn||console.log).call.apply(n,[console,' \
       '"[ROCKET LOADER] "].concat(t));var n}function n(t,e){var n=e.parentNode;n&&h(t,n,e)}function r(t,e){h(t,e,' \
       'e.childNodes[0])}function o(t){var e=t.parentNode;e&&e.removeChild(t)}function i(t){var ' \
       'e=t.namespaceURI===E?"xlink:href":"src";return t.getAttribute(e)}function a(t,e){var n=t.type.substr(' \
       'e.length);return!(n&&!A[n.trim()])&&((!k||!t.hasAttribute("nomodule"))&&!(!k&&"module"===n))}function c(t){' \
       'return a(t,"")}function s(t,e){return function(n){if(e(),t)return t.call(this,n)}}function u(t,e){t.onload=s(' \
       't.onload,e),t.onerror=s(t.onerror,e)}function p(t){var e=document.createElementNS(t.namespaceURI,' \
       '"script");e.async=t.hasAttribute("async"),e.textContent=t.textContent;for(var n=0;n<t.attributes.length;n++){' \
       'var r=t.attributes[n];try{r.namespaceURI?e.setAttributeNS(r.namespaceURI,r.name,r.value):e.setAttribute(' \
       'r.name,r.value)}catch(o){}}return e}function l(t,e){var n=new I(e);t.dispatchEvent(n)}function d(e){var ' \
       'n=e.namespaceURI===E,r=t();e.setAttribute(r,"");var i=n?"<svg>"+e.outerHTML+"</svg>":e.outerHTML;L.call(' \
       'document,i);var a=document.querySelector("["+r+"]");if(a){a.removeAttribute(r);var c=n&&a.parentNode;c&&o(' \
       'c)}return a}function f(t){if(t&&"handleEvent"in t){var e=t.handleEvent;return"function"==typeof e?e.bind(' \
       't):e}return t}function h(t,e,n){var r=n?function(t){return e.insertBefore(t,n)}:function(t){return ' \
       'e.appendChild(t)};Array.prototype.slice.call(t).forEach(r)}function v(){return/chrome/i.test(' \
       'navigator.userAgent)&&/google/i.test(navigator.vendor)}function y(t,e){function n(){this.constructor=t}H(t,' \
       'e),t.prototype=null===e?Object.create(e):(n.prototype=e.prototype,new n)}function m(t){return t instanceof ' \
       'Window?["load"]:t instanceof Document?["DOMContentLoaded","readystatechange"]:[]}function b(t){var ' \
       'e=t.getAttribute(R);if(!e)return null;var n=e.split(T);return{nonce:n[0],handlerPrefixLength:+n[1],' \
       'bailout:!t.hasAttribute("defer")}}function g(t){var e=B+t.nonce;Array.prototype.forEach.call(' \
       'document.querySelectorAll("["+e+"]"),function(n){n.removeAttribute(e),Array.prototype.forEach.call(' \
       'n.attributes,function(e){/^on/.test(e.name)&&"function"!=typeof n[e.name]&&n.setAttribute(e.name,' \
       'e.value.substring(t.handlerPrefixLength))})})}function S(){var t=window;"undefined"!=typeof Promise&&(' \
       't.__cfQR={done:new Promise(function(t){return U=t})})}function w(t){var e=new N(t),' \
       'n=new C(e);e.harvestScriptsInDocument(),new W(e,{nonce:t,blocking:!0,docWriteSimulator:n,callback:function(){' \
       '}}).run()}function x(t){var e=new N(t),n=new C(e);e.harvestScriptsInDocument();var r=new W(e,{nonce:t,' \
       'blocking:!1,docWriteSimulator:n,callback:function(){window.__cfRLUnblockHandlers=!0,r.removePreloadHints(),' \
       'P(t)}});r.insertPreloadHints(),M.runOnLoad(function(){r.run()})}function P(t){var e=new O(' \
       't);M.simulateStateBeforeDeferScriptsActivation(),e.harvestDeferScriptsInDocument(),new W(e,{nonce:t,' \
       'blocking:!1,callback:function(){M.simulateStateAfterDeferScriptsActivation(),U&&U()}}).run()}var ' \
       'E="http://www.w3.org/2000/svg",A={"application/ecmascript":!0,"application/javascript":!0,' \
       '"application/x-ecmascript":!0,"application/x-javascript":!0,"text/ecmascript":!0,"text/javascript":!0,' \
       '"text/javascript1.0":!0,"text/javascript1.1":!0,"text/javascript1.2":!0,"text/javascript1.3":!0,' \
       '"text/javascript1.4":!0,"text/javascript1.5":!0,"text/jscript":!0,"text/livescript":!0,' \
       '"text/x-ecmascript":!0,"text/x-javascript":!0,module:!0},k=void 0!==document.createElement(' \
       '"script").noModule,I=function(){var t=window;return t.__rocketLoaderEventCtor||Object.defineProperty(t,' \
       '"__rocketLoaderEventCtor",{value:Event}),t.__rocketLoaderEventCtor}(),L=document.write,_=document.writeln,' \
       'H=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var ' \
       'n in e)e.hasOwnProperty(n)&&(t[n]=e[n])},D=function(){function t(t){this.nonce=t,this.items=[]}return ' \
       'Object.defineProperty(t.prototype,"hasItems",{get:function(){return this.items.length>0},enumerable:!0,' \
       'configurable:!0}),t.prototype.pop=function(){return this.items.pop()},t.prototype.forEach=function(t){' \
       'this.items.forEach(function(e){var n=e.script;return t(n)})},t.prototype.harvestScripts=function(t,' \
       'e){var n=this,r=e.filter,o=e.mutate;Array.prototype.slice.call(t.querySelectorAll("script")).filter(' \
       'r).reverse().forEach(function(t){o(t),n.pushScriptOnStack(t)})},t.prototype.pushScriptOnStack=function(t){var ' \
       'e=t.parentNode,n=this.createPlaceholder(t),r=!!i(t);e.replaceChild(n,t),this.items.push({script:t,' \
       'placeholder:n,external:r,async:r&&t.hasAttribute("async"),executable:c(t)})},t.prototype.hasNonce=function(' \
       't){return 0===t.type.indexOf(this.nonce)},t.prototype.removeNonce=function(t){t.type=t.type.substr(' \
       'this.nonce.length)},t.prototype.makeNonExecutable=function(t){t.type=this.nonce+t.type},' \
       't.prototype.isPendingDeferScript=function(t){return t.hasAttribute(' \
       '"defer")||t.type===this.nonce+"module"&&!t.hasAttribute("async")},t}(),N=function(t){function e(){return ' \
       'null!==t&&t.apply(this,arguments)||this}return y(e,t),e.prototype.harvestScriptsInDocument=function(){var ' \
       't=this;this.harvestScripts(document,{filter:function(e){return t.hasNonce(e)},mutate:function(e){' \
       't.isPendingDeferScript(e)||t.removeNonce(e)}})},e.prototype.harvestScriptsAfterDocWrite=function(t){var ' \
       'e=this;this.harvestScripts(t,{filter:c,mutate:function(t){e.isPendingDeferScript(t)&&e.makeNonExecutable(' \
       't)}})},e.prototype.createPlaceholder=function(t){return document.createComment(t.outerHTML)},e}(D),' \
       'O=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return y(e,t),' \
       'e.prototype.harvestDeferScriptsInDocument=function(){var t=this;this.harvestScripts(document,' \
       '{filter:function(e){return t.hasNonce(e)&&t.isPendingDeferScript(e)},mutate:function(e){return t.removeNonce(' \
       'e)}})},e.prototype.createPlaceholder=function(t){var e=p(t);return this.makeNonExecutable(e),e},e}(D),' \
       'C=function(){function t(t){this.scriptStack=t}return t.prototype.enable=function(t){var ' \
       'e=this;this.insertionPointMarker=t,this.buffer="",document.write=function(){for(var t=[],' \
       'n=0;n<arguments.length;n++)t[n]=arguments[n];return e.write(t,!1)},document.writeln=function(){for(var t=[],' \
       'n=0;n<arguments.length;n++)t[n]=arguments[n];return e.write(t,!0)}},' \
       't.prototype.flushWrittenContentAndDisable=function(){document.write=L,document.writeln=_,' \
       'this.buffer.length&&(document.contains(' \
       'this.insertionPointMarker)?this.insertionPointMarker.parentNode===document.head?this.insertContentInHead(' \
       '):this.insertContentInBody():e("Insertion point marker for document.write was detached from document:",' \
       '"Markup will not be inserted"))},t.prototype.insertContentInHead=function(){var t=new DOMParser,e="<!DOCTYPE ' \
       'html><head>"+this.buffer+"</head>",o=t.parseFromString(e,"text/html");if(' \
       'this.scriptStack.harvestScriptsAfterDocWrite(o),n(o.head.childNodes,this.insertionPointMarker),' \
       'o.body.childNodes.length){for(var i=Array.prototype.slice.call(o.body.childNodes),' \
       'a=this.insertionPointMarker.nextSibling;a;)i.push(a),a=a.nextSibling;document.body||L.call(document,' \
       '"<body>"),r(i,document.body)}},t.prototype.insertContentInBody=function(){var ' \
       't=this.insertionPointMarker.parentElement,e=document.createElement(t.tagName);e.innerHTML=this.buffer,' \
       'this.scriptStack.harvestScriptsAfterDocWrite(e),n(e.childNodes,this.insertionPointMarker)},' \
       't.prototype.write=function(t,e){var n=document.currentScript;n&&i(n)&&n.hasAttribute("async")?(' \
       'r=e?_:L).call.apply(r,[document].concat(t)):this.buffer+=t.map(String).join(e?"\n":"");var r},t}(),' \
       'j=function(){function t(){var t=this;this.simulatedReadyState="loading",this.bypassEventsInProxies=!1,' \
       'this.nativeWindowAddEventListener=window.addEventListener;try{Object.defineProperty(document,"readyState",' \
       '{get:function(){return t.simulatedReadyState}})}catch(e){}this.setupEventListenerProxy(),' \
       'this.updateInlineHandlers()}return t.prototype.runOnLoad=function(t){var ' \
       'e=this;this.nativeWindowAddEventListener.call(window,"load",function(n){if(!e.bypassEventsInProxies)return t(' \
       'n)})},t.prototype.updateInlineHandlers=function(){this.proxyInlineHandler(document,"onreadystatechange"),' \
       'this.proxyInlineHandler(window,"onload"),document.body&&this.proxyInlineHandler(document.body,"onload")},' \
       't.prototype.simulateStateBeforeDeferScriptsActivation=function(){this.bypassEventsInProxies=!0,' \
       'this.simulatedReadyState="interactive",l(document,"readystatechange"),this.bypassEventsInProxies=!1},' \
       't.prototype.simulateStateAfterDeferScriptsActivation=function(){var t=this;this.bypassEventsInProxies=!0,' \
       'l(document,"DOMContentLoaded"),this.simulatedReadyState="complete",l(document,"readystatechange"),l(window,' \
       '"load"),this.bypassEventsInProxies=!1,window.setTimeout(function(){return t.bypassEventsInProxies=!0},0)},' \
       't.prototype.setupEventListenerProxy=function(){var t=this;("undefined"!=typeof EventTarget?[' \
       'EventTarget.prototype]:[Node.prototype,Window.prototype]).forEach(function(e){return ' \
       't.patchEventTargetMethods(e)})},t.prototype.patchEventTargetMethods=function(t){var e=this,' \
       'n=t.addEventListener,r=t.removeEventListener;t.addEventListener=function(t,r){for(var o=[],' \
       'i=2;i<arguments.length;i++)o[i-2]=arguments[i];var a=m(this),c=r&&r.__rocketLoaderProxiedHandler;if(!c){var ' \
       's=f(r);"function"==typeof s?(c=function(n){if(e.bypassEventsInProxies||a.indexOf(t)<0)return s.call(this,n)},' \
       'Object.defineProperty(r,"__rocketLoaderProxiedHandler",{value:c})):c=r}n.call.apply(n,[this,t,c].concat(o))},' \
       't.removeEventListener=function(t,e){for(var n=[],o=2;o<arguments.length;o++)n[o-2]=arguments[o];var ' \
       'i=e&&e.__rocketLoaderProxiedHandler||e;r.call.apply(r,[this,t,i].concat(n))}},' \
       't.prototype.proxyInlineHandler=function(t,e){try{var n=t[e];if(n&&!n.__rocketLoaderInlineHandlerProxy){var ' \
       'r=this;t[e]=function(t){if(r.bypassEventsInProxies)return n.call(this,t)},Object.defineProperty(t[e],' \
       '"__rocketLoaderInlineHandlerProxy",{value:!0})}}catch(o){return void console.warn("encountered an error when ' \
       'accessing "+e+" handler:",o.message)}},t}(),M=function(){var t=window;return ' \
       't.__rocketLoaderLoadProgressSimulator||Object.defineProperty(t,"__rocketLoaderLoadProgressSimulator",' \
       '{value:new j}),t.__rocketLoaderLoadProgressSimulator}(),W=function(){function t(t,e){this.scriptStack=t,' \
       'this.settings=e,this.preloadHints=[]}return t.prototype.insertPreloadHints=function(){var ' \
       't=this;this.scriptStack.forEach(function(e){if(a(e,t.settings.nonce)){var n=i(e),r=v()&&e.hasAttribute(' \
       '"integrity");if(n&&!r){var o=document.createElement("link");o.setAttribute("rel","preload"),o.setAttribute(' \
       '"as","script"),o.setAttribute("href",n),e.crossOrigin&&o.setAttribute("crossorigin",e.crossOrigin),' \
       'document.head.appendChild(o),t.preloadHints.push(o)}}})},t.prototype.removePreloadHints=function(){' \
       'this.preloadHints.forEach(function(t){return o(t)})},t.prototype.run=function(){for(var t=this,' \
       'e=this;this.scriptStack.hasItems;){var n=function(){var n=e.settings.docWriteSimulator,r=e.scriptStack.pop(' \
       ');n&&!r.async&&n.enable(r.placeholder);var o=e.activateScript(r);return ' \
       'o?r.external&&r.executable&&!r.async?(u(o,function(){t.finalizeActivation(r),t.run()}),{value:void 0}):void ' \
       'e.finalizeActivation(r):(n&&n.flushWrittenContentAndDisable(),"continue")}();if("object"==typeof n)return ' \
       'n.value}this.scriptStack.hasItems||this.settings.callback()},t.prototype.finalizeActivation=function(t){' \
       'this.settings.docWriteSimulator&&!t.async&&this.settings.docWriteSimulator.flushWrittenContentAndDisable(),' \
       'M.updateInlineHandlers(),o(t.placeholder)},t.prototype.activateScript=function(t){var n=t.script,' \
       'r=t.placeholder,o=t.external,i=t.async,a=r.parentNode;if(!document.contains(r))return e("Placeholder for ' \
       'script \n"+n.outerHTML+"\n was detached from document.","Script will not be executed."),' \
       'null;var c=this.settings.blocking&&o&&!i?d(n):p(n);return c?(a.insertBefore(c,r),c):(e("Failed to create ' \
       'activatable copy of script \n"+n.outerHTML+"\n","Script will not be executed."),null)},t}(),' \
       'R="data-cf-settings",T="|",B="data-cf-modified-",U=void 0;!function(){var t=document.currentScript;if(t){var ' \
       'n=b(t);n?(o(t),g(n),M.updateInlineHandlers(),n.bailout?w(n.nonce):(S(),x(n.nonce))):e("Activator script ' \
       'doesnt have settings. No scripts will be executed.")}else e("Cant obtain activator script. No scripts will be ' \
       'executed.")}()}(); '

result = js2py.eval_js(mpla.replace("document.write", "return "))

print(result)
