"""Content for justinhelmer.ca. Artist identity portal, not a second player."""

PUB = "ca-pub-0646320966060599"
AD = """<div class="ad-slot" aria-label="Advertisement">
  <div class="ad-label">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{pub}" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>""".format(pub=PUB)

AUTHOR = """<div class="author-box">
  <strong>Justin Helmer</strong> records as <a href="https://excavationpro.ca/">Excavationpro</a>.
  This is the name portal: bio, catalog, lyrics, press, and the doors to the free player.
</div>"""

PAGES = {}

# ---------------------------------------------------------------- music
PAGES["music.html"] = dict(
    title="Music — Justin Helmer / Excavationpro Catalog",
    desc="The Justin Helmer / Excavationpro catalog: how the records are made, where to listen free, store links, lyrics, live rooms, and the master/stream line.",
    path="/music.html",
    active="music",
    h1="The music: Justin Helmer / Excavationpro",
    lead="Records made at home, released independently, and streamed free. The catalog is the work; the player is the door.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["music", "catalog", "excavationpro"],
    body=f"""
<article class="card">
  <h2>One catalog, three names</h2>
  <p>Justin Helmer is the name on the door. The records go out as <strong>Excavationpro</strong>. Longer creative and mythic work sometimes uses <strong>Lightfather</strong>. The three names are not separate catalogs; they are layers of the same practice. If you came from a store badge, a lyric, or a live room, you are in the right place.</p>
  <p>The music is experimental hip-hop and electronic texture, recorded and mixed at home without a label deciding what a song is allowed to be. The catalog is large because the practice is daily, not because every track is a single. It includes songs, instrumentals, sketches, and full projects.</p>
  <h2>How a record gets made</h2>
  <p>A track usually starts with a drum pattern, a sample-free texture, or a phrase that will not leave. The writing and recording happen in the same room; the mix follows the arrangement rather than sanding it into a format. Some pieces are built to be songs, some are built to be listened to as texture. The distinction is intentional.</p>
  <p>Masters stay in the vault. The public stream is a compressed listening copy. That is the line: open listening, closed ownership. The <a href="https://asiancoastline.com/why-free-streams.html">streams vs masters guide</a> explains the model in full.</p>
</article>
{AD}
<article class="card">
  <h2>Where to listen</h2>
  <p>The canonical free player is <a href="https://asiancoastline.com/listen.html">asiancoastline.com/listen.html</a>. It carries the public catalog, search, queue, radio, favorites, and an installed-app shell. No account is required. This domain links to that player instead of running a second copy of the same 11,000-track catalog; one listening room is easier to maintain and easier to trust.</p>
  <p>If you want the catalog in the stores you already use, the two official smart links are <a href="https://ffm.to/justin-helmer">ffm.to/justin-helmer</a> for the name and <a href="https://ffm.to/eovnvo9">ffm.to/eovnvo9</a> for Excavationpro. Spotify, YouTube Music, and Audius are linked from the home page. The free player and the stores are different doors to the same work.</p>
  <h2>Lyrics and live rooms</h2>
  <p>The <a href="/lyrics/">lyric vault</a> holds the words with a search and a mini player for mapped streams. The live rooms on Kick, Rumble, and Twitch are treated as radio: a place to work, listen, and talk, not a hard sell. Links are on the home page and in the player&rsquo;s live tab.</p>
  <h2>What to start with</h2>
  <ul>
    <li><strong>If you want songs:</strong> open the player, search an album title, and let the queue run.</li>
    <li><strong>If you want words:</strong> start in the lyric vault and follow the mapped stream on a track.</li>
    <li><strong>If you want context:</strong> read <a href="https://excavationpro.ca/articles/why-i-give-the-music-away.html">why the music is free</a>.</li>
    <li><strong>If you want the whole map:</strong> use the <a href="https://bpmfinder.ca/tools.html">tools hub</a>.</li>
  </ul>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Is the music really free?</h3>
  <p>Yes. The public player is free to hear; no account is required. Optional support helps hosting.</p>
  <h3>Can I download the tracks?</h3>
  <p>The player is a listening room, not a download store. Store links are the legal purchase route where available.</p>
  <h3>Why three names?</h3>
  <p>Justin Helmer is the person, Excavationpro is the recording project, Lightfather is the longer-form creative layer. Same catalog family.</p>
  <h3>Where are the masters?</h3>
  <p>In the artist&rsquo;s vault. The public stream is a compressed copy; the master is the archival source.</p>
</article>
{AUTHOR}
""",
    faqs=[
        ("Is the music really free?", "The public player is free to hear; optional support helps hosting."),
        ("Can I download the tracks?", "The player is a listening room; store links are the purchase route where available."),
        ("Why three names?", "Justin Helmer is the person, Excavationpro the recording project, Lightfather the longer-form layer."),
        ("Where are the masters?", "In the artist vault; the public stream is a compressed copy."),
    ],
)

# ---------------------------------------------------------------- about
PAGES["about.html"] = dict(
    title="About Justin Helmer — Artist, Excavationpro, Lightfather",
    desc="Who Justin Helmer is, why the records go out as Excavationpro, how the independent catalog works, and what LYGO has to do with the music.",
    path="/about.html",
    active="about",
    h1="About Justin Helmer",
    lead="Canadian artist, independent catalog, three names, one practice. The short version: the music is the work, the portal is the door, and the masters stay mine.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["about", "artist", "bio"],
    body=f"""
<article class="card">
  <h2>Who I am</h2>
  <p>I am Justin Helmer. I write, record, and mix at home. Listeners know the records as <strong>Excavationpro</strong>; longer creative and mythic work uses <strong>Lightfather</strong>. I am Canadian, independent, and not interested in waiting for a label to decide whether a song is allowed to exist.</p>
  <p>The catalog is experimental hip-hop and electronic texture: songs, instrumentals, sketches, and full projects. It is large because the practice is daily. Not every track is a single; the catalog is a body of work, not a playlist optimized for a chart.</p>
  <h2>Why the music is free</h2>
  <p>The first encounter should be a listen, not a negotiation. The public player is free, the stores are there if you want them, and the masters stay offline. Free listening is not a license to re-upload or sell the files; it is a permission to hear the work and share the door.</p>
  <p>That model is explained in <a href="https://asiancoastline.com/why-free-streams.html">why free streams exist</a> and in the <a href="https://excavationpro.ca/articles/why-i-give-the-music-away.html">Excavationpro essay</a>. The short version: a preview behind a storefront is a sales pitch; a full stream is a relationship.</p>
</article>
{AD}
<article class="card">
  <h2>The names, plainly</h2>
  <ul>
    <li><strong>Justin Helmer</strong> &mdash; the person and the official artist name on stores.</li>
    <li><strong>Excavationpro</strong> &mdash; the recording project and the catalog most listeners know.</li>
    <li><strong>Lightfather</strong> &mdash; the longer-form creative and mythic layer.</li>
  </ul>
  <p>This domain is the name portal. <a href="https://excavationpro.ca/">excavationpro.ca</a> is the artist house and the essays. <a href="https://asiancoastline.com/">asiancoastline.com</a> is the free player. Keeping those jobs separate makes each one easier to maintain and easier to explain.</p>
  <h2>Live rooms</h2>
  <p>Kick, Rumble, and Twitch are treated as radio: a place to work, listen, and talk. They are not a hard sell. The live links are on the home page and inside the player&rsquo;s live tab. If a room is offline, the player and the catalog are still there.</p>
  <h2>The other half: LYGO</h2>
  <p>LYGO is the agent and tool stack I publish beside the music: the console, SkillHub, the games, the lattice docs. It is not a replacement for the catalog; it is the other half of the workshop. The <a href="https://bpmfinder.ca/tools.html">tools hub</a> is the map.</p>
  <h2>Press and contact</h2>
  <p>A short bio, a long bio, and reusable facts are on the <a href="/press.html">press page</a>. For interviews, permissions, or a direct message, use the <a href="/contact.html">contact page</a>.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Where are you based?</h3>
  <p>Canada. The catalog is recorded at home; the live rooms are online.</p>
  <h3>Do you play live?</h3>
  <p>The live rooms are the main live surface right now. They are radio-style sessions, not a tour schedule.</p>
  <h3>Is Excavationpro a band?</h3>
  <p>It is the recording project of Justin Helmer. The catalog is the work of one person with collaborators where credited.</p>
  <h3>Can I use a track in a project?</h3>
  <p>Ask first. Free listening is not a sync or commercial license. The <a href="/contact.html">contact page</a> is the route.</p>
</article>
{AUTHOR}
""",
    faqs=[
        ("Where are you based?", "Canada; the catalog is recorded at home and the live rooms are online."),
        ("Do you play live?", "The live rooms are the main live surface right now, radio-style rather than a tour."),
        ("Is Excavationpro a band?", "It is the recording project of Justin Helmer, with collaborators where credited."),
        ("Can I use a track in a project?", "Ask first; free listening is not a sync or commercial license."),
    ],
)

# ---------------------------------------------------------------- press
PAGES["press.html"] = dict(
    title="Press Kit — Justin Helmer / Excavationpro",
    desc="Short and long bios, reusable facts, interview topics, images, and press contact for Justin Helmer / Excavationpro.",
    path="/press.html",
    active="press",
    h1="Press kit: Justin Helmer / Excavationpro",
    lead="Reusable bios, the facts that do not change, interview angles, and the line between quoting the work and re-uploading it.",
    minutes="5 min read",
    updated="2026-10-20",
    tags=["press", "bio", "media"],
    body=f"""
<article class="card">
  <h2>Short bio (50 words)</h2>
  <p>Justin Helmer is a Canadian artist who records as Excavationpro. The catalog is independent experimental hip-hop and electronic texture, recorded at home and streamed free. Longer creative work uses the name Lightfather. The masters stay in the artist&rsquo;s vault; the public player stays open.</p>
  <h2>Medium bio (100 words)</h2>
  <p>Justin Helmer is a Canadian artist and independent publisher. He records as Excavationpro, a catalog of experimental hip-hop and electronic texture built at home without a label. Listeners know the free browser player at asiancoastline.com; the stores carry the same work under the names Justin Helmer and Excavationpro. Longer creative and mythic work uses Lightfather. Helmer also publishes LYGO, an open agent and tool stack. The through-line is ownership: the catalog is free to hear, the masters stay offline, and the artist keeps the door.</p>
  <h2>Long bio (200 words)</h2>
  <p>Justin Helmer is a Canadian artist, writer, and independent publisher. He records as Excavationpro, a large catalog of experimental hip-hop and electronic texture made at home without a label deciding what a song is allowed to be. The work ranges from songs and instrumentals to sketches and full projects; the through-line is a daily practice rather than a release cycle built for a chart.</p>
  <p>Listeners can hear the public catalog free at asiancoastline.com, with no account and no paywall. The same work is available through the official store links under Justin Helmer and Excavationpro. Longer creative and mythic work uses the name Lightfather. Helmer also publishes LYGO, an open agent and tool stack that includes a local console, SkillHub, browser games, and the BPMfinder tempo tool.</p>
  <p>His position on rights is straightforward: streams are listening copies, masters stay in the vault, and free listening is not a license to re-upload or sell the files. The essays at excavationpro.ca explain the model; the lyric vault at justinhelmer.ca holds the words. He lives in Canada and works online.</p>
</article>
{AD}
<article class="card">
  <h2>Facts that do not change</h2>
  <ul>
    <li><strong>Name:</strong> Justin Helmer</li>
    <li><strong>Recording name:</strong> Excavationpro</li>
    <li><strong>Long-form name:</strong> Lightfather</li>
    <li><strong>Based:</strong> Canada</li>
    <li><strong>Genres:</strong> experimental hip-hop, electronic, texture</li>
    <li><strong>Model:</strong> independent; free public streams; masters offline</li>
    <li><strong>Player:</strong> asiancoastline.com/listen.html</li>
    <li><strong>Artist house:</strong> excavationpro.ca</li>
    <li><strong>Lyrics:</strong> justinhelmer.ca/lyrics/</li>
  </ul>
  <h2>Interview angles</h2>
  <p>Independent catalog economics; why the player is free while the masters stay offline; the difference between a stream and a master; recording at home without a label; the three-name structure; and the LYGO tool stack as the other half of the practice.</p>
  <h2>Assets and usage</h2>
  <p>The share image is <a href="https://justinhelmer.ca/assets/og-home.jpg">justinhelmer.ca/assets/og-home.jpg</a>; the hero is <a href="https://justinhelmer.ca/assets/hero.jpg">/assets/hero.jpg</a>. You may use the bios and the images for editorial coverage with attribution. Do not re-upload the audio files, sell them, or present the catalog as your own. For a longer interview or a commercial use, use the contact page.</p>
  <p><strong>Press contact:</strong> <a href="mailto:excavationstation@gmail.com?subject=Justin%20Helmer%20press">excavationstation@gmail.com</a> with &ldquo;Press&rdquo; in the subject.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Can I quote the bio?</h3>
  <p>Yes, with attribution to Justin Helmer / Excavationpro.</p>
  <h3>Can I use a track in a podcast?</h3>
  <p>Ask first. That is a sync use, not the free listening permission.</p>
  <h3>Are the images licensed for press?</h3>
  <p>Yes for editorial coverage with attribution; ask for anything commercial.</p>
  <h3>Who handles press?</h3>
  <p>Justin directly. There is no outside publicist.</p>
</article>
{AUTHOR}
""",
    faqs=[
        ("Can I quote the bio?", "Yes, with attribution to Justin Helmer / Excavationpro."),
        ("Can I use a track in a podcast?", "Ask first; that is a sync use, not free listening."),
        ("Are the images licensed for press?", "Yes for editorial coverage with attribution; ask for commercial use."),
        ("Who handles press?", "Justin directly; there is no outside publicist."),
    ],
)

# ---------------------------------------------------------------- listening guide
PAGES["listen.html"] = dict(
    title="How to Listen — Justin Helmer / Excavationpro",
    desc="The free listening route for the Justin Helmer / Excavationpro catalog: the canonical player, no account, stores, lyrics, live rooms, and troubleshooting.",
    path="/listen.html",
    active="music",
    h1="How to listen to the catalog",
    lead="The canonical free player lives at asiancoastline.com. This page is the guide: what to open, what you can do, and where the stores and lyrics fit.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["listen", "player", "guide"],
    body=f"""
<article class="card">
  <h2>Open the canonical player</h2>
  <p>The full browser player is at <a href="https://asiancoastline.com/listen.html">asiancoastline.com/listen.html</a>. It carries the public catalog: search by title or ISRC, filter by album or Haven audio, queue tracks, shuffle, run radio, save local favorites, crossfade, set a sleep timer, and install the shell as an app.</p>
  <p>This domain does not run a second copy of the same 11,000-track catalog. One player is easier to maintain, faster to fix, and honest about where the listening room actually is. The name portal points to the room; the room does the playing.</p>
  <h2>No account, no upload</h2>
  <p>You do not need a signup. Favorites and queue are stored in your browser, not on an account. The player does not upload your files or build a listening profile. If you clear site data, the local favorites clear with it.</p>
</article>
<article class="card">
  <h2>What to do first</h2>
  <ol>
    <li>Open <a href="https://asiancoastline.com/listen.html">the player</a>.</li>
    <li>Search an album or track title rather than scrolling the whole catalog.</li>
    <li>Use the queue for three or four tracks; turn crossfade off to hear the transitions as recorded.</li>
    <li>Use radio when you want the player to keep going.</li>
    <li>Use the heart for a local favorites list and the share button for a link.</li>
  </ol>
  <h2>Stores and lyrics</h2>
  <p>If you want the catalog where you already listen, use the official smart links: <a href="https://ffm.to/justin-helmer">ffm.to/justin-helmer</a> for the name and <a href="https://ffm.to/eovnvo9">ffm.to/eovnvo9</a> for Excavationpro. The <a href="/lyrics/">lyric vault</a> holds the words with a mini player for mapped streams. The <a href="/music.html">music page</a> explains the catalog and the master/stream line.</p>
  <h2>Troubleshooting</h2>
  <ul>
    <li><strong>One track will not start.</strong> Try another track; if only one fails, the public file may be missing. The ledger in the player shows what the catalog expected.</li>
    <li><strong>Playback stops on mobile.</strong> Some browsers suspend background audio; keep the tab active or use the installed shell.</li>
    <li><strong>The list is empty.</strong> Clear the search and set the filter back to All.</li>
    <li><strong>No sound.</strong> Check the player volume, the system volume, and whether another tab owns the audio session.</li>
  </ul>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Why is the player on another domain?</h3>
  <p>asiancoastline.com is the listening room. justinhelmer.ca is the name portal. One canonical player avoids duplicate catalogs and duplicate maintenance.</p>
  <h3>Do I need an account?</h3>
  <p>No. Favorites and queue are local to your browser.</p>
  <h3>Can I download the tracks?</h3>
  <p>The player streams; it is not a download store. Store links are the purchase route where available.</p>
  <h3>Does it work on a phone?</h3>
  <p>Yes. The player is responsive and can be installed to the home screen.</p>
</article>
{AUTHOR}
""",
    faqs=[
        ("Why is the player on another domain?", "asiancoastline.com is the listening room; justinhelmer.ca is the name portal."),
        ("Do I need an account?", "No; favorites and queue are local to the browser."),
        ("Can I download the tracks?", "The player streams; store links are the purchase route."),
        ("Does it work on a phone?", "Yes; the player is responsive and installable."),
    ],
)

# ---------------------------------------------------------------- contact
PAGES["contact.html"] = dict(
    title="Contact Justin Helmer — Press, Booking, Permissions",
    desc="Contact Justin Helmer / Excavationpro for press, interviews, sync and permission requests, or a broken link.",
    path="/contact.html",
    active="contact",
    h1="Contact Justin Helmer",
    lead="Press, interviews, sync and permission requests, or a broken link. Email is the reliable route; the project is small and direct.",
    minutes="2 min read",
    updated="2026-10-20",
    tags=["contact"],
    body="""
<article class="card">
  <h2>Email</h2>
  <p><a href="mailto:excavationstation@gmail.com?subject=Justin%20Helmer">excavationstation@gmail.com</a></p>
  <p>Put <strong>&ldquo;Justin Helmer&rdquo;</strong> and the reason in the subject: press, booking, permission, or site issue. Allow a few business days for a reply.</p>
  <h2>What to include</h2>
  <ul>
    <li><strong>Press:</strong> outlet, angle, deadline, and whether you need an interview or a quote.</li>
    <li><strong>Permission:</strong> track title, intended use, platform, and whether money is involved.</li>
    <li><strong>Broken link:</strong> the page URL and what you expected to find.</li>
    <li><strong>Privacy:</strong> the email you used and what you want changed or removed.</li>
  </ul>
  <p>Do not send passwords, API keys, or private audio you do not want a stranger to hear.</p>
  <h2>Elsewhere</h2>
  <p>Stores: <a href="https://ffm.to/justin-helmer">Justin Helmer</a> · <a href="https://ffm.to/eovnvo9">Excavationpro</a>. Social: <a href="https://x.com/Excavationpro">X</a> · <a href="https://bsky.app/profile/excavationpro.bsky.social">Bluesky</a>.</p>
  <h2>Policies</h2>
  <p><a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a> · <a href="/press.html">Press kit</a></p>
</article>
""",
)

# ---------------------------------------------------------------- privacy
PAGES["privacy.html"] = dict(
    title="Privacy Policy — Justin Helmer",
    desc="How justinhelmer.ca handles logs, links to the player and stores, cookies, Google AdSense, consent, and privacy requests.",
    path="/privacy.html",
    active="privacy",
    h1="Privacy Policy — justinhelmer.ca",
    lead="This is a static artist portal with no account system. The short version: the site does not build a listener profile; the player and stores are separate services with their own policies.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["privacy"],
    body="""
<article class="card">
  <h2>This site</h2>
  <p>justinhelmer.ca is a static site hosted on GitHub Pages. The host may process standard technical logs such as IP address, user agent, requested URL, and timestamps for security and reliability. There is no account, no comment system, and no upload form on this domain.</p>
  <p>The lyric vault stores its search state in your browser. The cookie choice is stored locally. Clearing site data removes both.</p>
  <h2>Cookies and advertising</h2>
  <p>We may use cookies or similar storage for essential site function and to remember your cookie choice. When Google AdSense is active on editorial pages, Google and its partners may use cookies or device information to serve and measure ads, including ads based on visits to this site or other sites.</p>
  <p>The AdSense publisher ID is <code>ca-pub-0646320966060599</code>. You can review Google&rsquo;s advertising controls at <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a> and manage personalized ads at <a href="https://adssettings.google.com/">adssettings.google.com</a>. Blocking advertising cookies does not lock the site.</p>
  <h2>Consent</h2>
  <p>The site shows a cookie banner with Accept and Decline. Your choice is stored locally. If you decline, the banner will not keep asking on every page. Clear the site&rsquo;s local storage to change the choice.</p>
  <h2>Other services</h2>
  <ul>
    <li><strong>GitHub Pages</strong> &mdash; hosts this static site and may keep access logs.</li>
    <li><strong>asiancoastline.com</strong> &mdash; the canonical player; its privacy policy applies there.</li>
    <li><strong>Google AdSense</strong> &mdash; advertising on editorial pages when active.</li>
    <li><strong>Feature.fm, Spotify, YouTube, Audius</strong> &mdash; store links; their policies apply.</li>
    <li><strong>Kick, Rumble, Twitch</strong> &mdash; live rooms; their policies apply.</li>
    <li><strong>PayPal</strong> &mdash; optional support, under PayPal&rsquo;s policy.</li>
  </ul>
  <h2>Retention and children</h2>
  <p>This site does not maintain reader accounts or an uploaded-audio database. Email correspondence is kept only as long as needed to answer the request. It is a general music site; we do not knowingly collect personal information from children, and no account is required.</p>
  <h2>Changes and contact</h2>
  <p>If this policy changes, the update date will change. For privacy questions, email <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;Justin Helmer privacy&rdquo; in the subject. See also the <a href="/terms.html">terms</a>.</p>
</article>
""",
)

# ---------------------------------------------------------------- terms
PAGES["terms.html"] = dict(
    title="Terms of Use — Justin Helmer",
    desc="Terms for justinhelmer.ca: the listening license, acceptable use, intellectual property, and warranty and liability limits.",
    path="/terms.html",
    active="terms",
    h1="Terms of use — justinhelmer.ca",
    lead="These terms cover this artist portal and the links from it. By using the site, you agree to them. The short version: listen freely, do not re-upload or sell the files.",
    minutes="3 min read",
    updated="2026-10-20",
    tags=["terms", "license"],
    body="""
<article class="card">
  <h2>This site</h2>
  <p>justinhelmer.ca is an informational artist portal. The music player is a separate service at asiancoastline.com, and the stores are third-party services. Your use of those services is governed by their terms as well as these.</p>
  <h2>License to listen</h2>
  <p>You may stream the public catalog for personal listening, share links, and quote short passages from the guides or lyrics with attribution. You may not re-upload the audio files, sell them, include them in a paid product, or present them as your own. The stream is a listening copy, not a transfer of ownership.</p>
  <h2>Acceptable use</h2>
  <ul>
    <li>Do not use the site to break the law or infringe someone else&rsquo;s rights.</li>
    <li>Do not attempt to disrupt the site or bypass security controls.</li>
    <li>Do not use the catalog in a commercial video, game, or ad without permission.</li>
    <li>Do not feed the lyrics or audio into a commercial model for resale.</li>
  </ul>
  <h2>Intellectual property</h2>
  <p>The music, lyrics, guides, and site design are owned by Justin Helmer / Excavationpro unless otherwise stated. Short quotations from the guides are allowed with a link back to the page. Press use of the bios and images is covered on the <a href="/press.html">press page</a>.</p>
  <h2>No warranty</h2>
  <p>The site is provided as-is, without warranties of any kind, including fitness for a particular purpose and non-infringement. Links may break, a store may change, or a player may be unavailable. You are responsible for verifying anything you rely on.</p>
  <h2>Limitation of liability</h2>
  <p>To the maximum extent permitted by law, Justin Helmer / Excavationpro is not liable for indirect, incidental, special, or consequential damages arising from use of the site or the linked services.</p>
  <h2>Changes and contact</h2>
  <p>These terms may be updated; the date at the top will change. Questions: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;Justin Helmer terms&rdquo; in the subject. See also the <a href="/privacy.html">privacy policy</a>.</p>
</article>
""",
)
