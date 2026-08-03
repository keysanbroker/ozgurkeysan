"""
P-145 — Bağbaşı, Vatan Caddesi · Zemin + Bodrum Dükkan · Özgür Keysan
Çalıştır:  python3 P-145/build.py   (nereden çağrılırsa çağrılsın çalışır)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))   # kit kökü (build_lib burada)
os.chdir(HERE)                               # emsaller/ ve index.html buraya
import build_lib as B

# ------------------------------------------------------------------ görseller
SV    = B.img_uri("emsaller/streetview-vatan-cd.webp", width=1000)
DENEK = B.img_uri("emsaller/denek-120m2-4650000.png")
A243  = B.img_uri("emsaller/aktif-243m2-9750000.png")
A611  = B.img_uri("emsaller/aktif-611m2-22000000.png")
K150  = B.img_uri("emsaller/kalkan-150m2-4499000.png")
K45   = B.img_uri("emsaller/kalkan-45m2-1350000.png")
K30   = B.img_uri("emsaller/kalkan-30m2-1550000.png")
K27   = B.img_uri("emsaller/kalkan-27m2-1585000.png")

# ------------------------------------------------------------------ baş + topbar
head = B.head("Değerleme Raporu · Bağbaşı Vatan Caddesi · P-145 — Özgür Keysan")
top  = B.topbar("03.08.2026")

# ------------------------------------------------------------------ KAPAK
kapak = '''<header class="cover">
  <div class="wrap">
    <div class="eyebrow">Gayrimenkul Değerleme Raporu · 03 Ağustos 2026</div>
    <h1>Bağbaşı, Vatan Caddesi<br><span class="red">Zemin + Bodrum Dükkan · P-145</span></h1>
    <div class="id-line">120 m² zemin (cadde cepheli) · 120 m² bodrum · 15 m² işyeri önü · ana yola cepheli ticari</div>

    <div class="id-strip">
      <div class="id-cell"><div class="lbl">İl / İlçe</div><div class="val">Denizli</div></div>
      <div class="id-cell"><div class="lbl">Mahalle</div><div class="val">Bağbaşı</div></div>
      <div class="id-cell"><div class="lbl">Ada / Parsel</div><div class="val">137 / 18</div></div>
      <div class="id-cell"><div class="lbl">Kullanım Alanı</div><div class="val">240 m² kapalı<br>(120 zemin + 120 bodrum)</div></div>
    </div>

    <div class="parcel-cards">
      <div class="parcel-card">
        <div class="pc-lbl">Taşınmaz Niteliği</div>
        <div class="pc-num">Zemin + Bodrum Dükkan</div>
        <div class="pc-detail"><strong>120 m² zemin</strong> (cadde cepheli, geniş vitrin) · <strong>120 m² bodrum</strong> · 15 m² işyeri önü · Dükkan &amp; Mağaza (ticari)</div>
      </div>
      <div class="parcel-card">
        <div class="pc-lbl">Konum &amp; Cephe</div>
        <div class="pc-num">Vatan Caddesi</div>
        <div class="pc-detail"><strong>Bağbaşı eski yol · ana yola cepheli.</strong> Yaya ve araç trafiğinin yüksek olduğu ticari aks üzerinde, yüksek görünürlük.</div>
      </div>
    </div>

    <p class="salute">Sayın Ali Bey,</p>
    <p>Bu çalışma, Bağbaşı Vatan Caddesi üzerindeki zemin + bodrum dükkanınızın satış sürecini en doğru biçimde yürütebilmek amacıyla hazırlanmıştır. Aynı cadde üzerindeki ticari ilanlar tek tek incelendi ve taşınmazın kendi geçmiş ilan verisiyle birlikte değerlendirildi.</p>
    <p>Raporda; taşınmazın profilini, bölgedeki güncel ticari pazarı (aktif ve son bir yılda yayından kalkan emsaller), önerilen satış fiyatı aralığını ve satış sürecinin nasıl yönetileceğini bulabilirsiniz.</p>
    <p class="signoff">İyi okumalar dilerim.</p>

    <ol class="roadmap-list">
      <li>Taşınmaz Profili</li>
      <li>Pazar Analizi · Aktif ve Kalkan Emsaller</li>
      <li>Değer Analizi ve Fiyat Aralığı</li>
      <li>Riskler ve Maliyetler</li>
    </ol>
  </div>
</header>
'''

# ------------------------------------------------------------------ 01 PROFİL
profil = '''<section class="block">
  <div class="wrap">
    <div class="block-head">
      <div class="block-num">01</div>
      <h2>Taşınmaz Profili</h2>
      <p class="block-intro">Taşınmaz, Bağbaşı eski yol <strong>Vatan Caddesi</strong> üzerinde, ana yola cepheli konumdadır. Zemin kat cadde hizasında geniş vitrine sahip; 120 m² bodrum ek kullanım / depo alanı sağlar. Cadde, yaya ve araç trafiğinin yüksek olduğu ticari bir akstır.</p>
    </div>

    <div class="embed-wrap" style="border-radius:14px;overflow:hidden;border:1px solid var(--line);">
      <img src="__SV__" alt="Vatan Caddesi cephesi" class="lb-clickable" style="width:100%;height:auto;display:block;cursor:zoom-in;" />
    </div>
    <div class="embed-cap" style="margin-bottom:8px;">Vatan Caddesi cephesi · Google Street View (Haz 2024)</div>

    <div class="access-grid">
      <div class="access-cell"><div class="ac-loc">Zemin Kat</div><div class="ac-val">120<span class="unit">m²</span></div></div>
      <div class="access-cell"><div class="ac-loc">Bodrum</div><div class="ac-val">120<span class="unit">m²</span></div></div>
      <div class="access-cell"><div class="ac-loc">İşyeri Önü</div><div class="ac-val">15<span class="unit">m²</span></div></div>
    </div>

    <div class="topo-note">
      <div class="ct">Konum ve Cephe</div>
      <h4>Ana yola cepheli, yüksek görünürlük</h4>
      <p>Zemin kat, cadde hizasında <strong>geniş vitrinli</strong> bir ticari birimdir; ana yola cephesi taşınmazın en güçlü yönüdür. Altındaki <strong>120 m² bodrum</strong> depo veya ek işyeri kullanımı için değer katar; ancak bodrum katın birim değeri, ışık ve erişim nedeniyle zemin kattan belirgin biçimde düşüktür. 15 m² işyeri önü kullanımı cepheyi güçlendirir.</p>
    </div>
  </div>
</section>
'''.replace("__SV__", SV)

# ------------------------------------------------------------------ 02 PAZAR
stats = '''  <div class="stats">
    <div class="stat"><div class="lbl">İncelenen İlan</div><div class="val">7</div><div class="desc">Aynı cadde · tek tek incelendi</div></div>
    <div class="stat"><div class="lbl">Aktif İlan</div><div class="val">2</div><div class="desc">Büyük metrekare · henüz satılmadı</div></div>
    <div class="stat"><div class="lbl">1 Yılda Kalkan</div><div class="val">5</div><div class="desc">Kendi geçmiş ilanı dahil</div></div>
    <div class="stat accent"><div class="lbl">Gerçekleşen Teklif</div><div class="val">~3,0<span class="unit">M TL</span></div><div class="desc">Sahadan · en somut sinyal</div></div>
  </div>
'''

aktif = B.table("Şu Anda Yayında Olan İlanlar", 2, "Aynı cadde · büyük metrekare · henüz satılmadı",
    [
      B.lst_row("A1", A243, "243 m² · köşe parsel", "Anacadde üzeri köşe · geniş vitrin · <strong>prim taşır</strong>",
                "40.123 TL/m²", "9.750.000 TL", "26 gün"),
      B.lst_row("A2", A611, "611 m² · büyük işyeri", "Cadde üzeri büyük ticari alan",
                "36.007 TL/m²", "22.000.000 TL", "23 gün"),
    ], active=True)

saha = B.sahadan_bilgi(
    "Taşınmaz daha önce <strong>4.650.000 TL</strong> (38.750 TL/m²) istekle satışa çıkarılmış; "
    "<strong>90 gün</strong> yayında kalmış ve <strong>3.000.000 TL bandında teklifler</strong> aldıktan sonra "
    "yayından kaldırılmıştır. Bu, sahadan gelen en somut fiyat sinyalidir: 4M+ seviyesi bu taşınmaz için "
    "piyasada karşılık bulmamış, gerçek talep <strong>~3M seviyesinde</strong> oluşmuştur.")

kalkan = B.table("Son 1 Yılda Yayından Kalkan İlanlar", 5, "İstek fiyatları tavanı gösterir · aynı cadde",
    [
      B.lst_row("•", DENEK, "120 m² · bu taşınmaz", "Taşınmazın kendi geçmiş ilanı · <strong>~3M teklif aldı</strong>",
                "38.750 TL/m²", "4.650.000 TL", "90 gün", anchor=True),
      B.lst_row("K1", K150, "150 m² + alt depo", "En yakın büyük emsal · satılamadan kalktı",
                "29.993 TL/m²", "4.499.000 TL", "29 gün"),
      B.lst_row("K2", K45, "45 m² dükkan", "Bağbaşı eski yol cadde üzeri",
                "30.000 TL/m²", "1.350.000 TL", "9 gün"),
      B.lst_row("K3", K30, "30 m² · apart fiyatına", "Küçük dükkan · düşük mutlak fiyat (120 m² için referans dışı)",
                "51.667 TL/m²", "1.550.000 TL", "247 gün", outlier=True, long=True),
      B.lst_row("K4", K27, "27 m² · apart fiyatına", "Küçük dükkan · düşük mutlak fiyat (120 m² için referans dışı)",
                "58.704 TL/m²", "1.585.000 TL", "28 gün", outlier=True),
    ])

pazar_ozet = '''  <div class="market-summary">
    <h4>Pazar ne söylüyor?</h4>
    <p>Büyük metrekareli dükkanlar (120–243 m²) <strong>~30–40 bin TL/m²</strong> istek bandında fiyatlanıyor. Küçük dükkanlar (27–30 m²) düşük mutlak fiyat (~1,5M) nedeniyle 52–59 bin TL/m² gibi yüksek birim taşıyor; bu "apart fiyatına" etkisi olduğundan 120 m² için <strong>referans dışı</strong> bırakıldı.</p>
    <p><strong>Kritik gözlem:</strong> Hem taşınmazın kendi 4,65M ilanı, hem de 150 m²'lik en yakın büyük emsal (30 bin TL/m²) satılamadan yayından kalkmış; iki aktif büyük ilan da (243 m² köşe, 611 m²) hâlâ satılmamıştır. Yani büyük metrekarede istek fiyatları yüksek ama <strong>gerçekleşme zayıftır.</strong></p>
    <p>İstek fiyatları tavanı gösterir; gerçekleşen satış çoğu zaman bunun altındadır. Kalkan ilanların satılıp satılmadığı kesin bilinmediğinden, en güvenilir sinyal taşınmazın kendi aldığı <strong>~3M teklifidir.</strong></p>
  </div>
'''

pazar = ('<section class="block">\n  <div class="wrap">\n'
         '    <div class="block-head">\n      <div class="block-num">02</div>\n'
         '      <h2>Pazar Analizi</h2>\n'
         '      <p class="block-intro">Bölgede <strong>toplam 7 ticari ilan tek tek incelendi</strong>: '
         '2 aktif, son bir yılda yayından kalkan 4 emsal ve taşınmazın kendi geçmiş ilanı. '
         'Aktif ve kalkan ilanlar ayrı tablolarda gösterilmiştir.</p>\n    </div>\n\n'
         + stats + aktif + saha + kalkan + pazar_ozet +
         '  </div>\n</section>\n')

# ------------------------------------------------------------------ 03 DEĞER
deger_bilesen = '''  <div class="comp-total">
    <div class="ct-row"><span>Zemin kat · 120 m² × ~27.500 TL/m²</span><span>≈ 3.300.000 TL</span></div>
    <div class="ct-row"><span>Bodrum · 120 m² × ~11.500 TL/m² (zeminin ~%42'si)</span><span>≈ 1.380.000 TL</span></div>
    <div class="ct-row"><span>İşyeri önü + cephe primi</span><span>≈ 120.000 TL</span></div>
    <div class="ct-row ct-grand"><span>Teorik içsel değer</span><span>≈ 4.800.000 TL</span></div>
  </div>
  <div class="market-summary">
    <h4>İçsel değer ile piyasa gerçeği arasındaki gerilim</h4>
    <p>Bileşen toplamı, taşınmazın <strong>teorik içsel değerini ~4,8M TL</strong> olarak gösterir. Ancak piyasa bu seviyeyi onaylamamaktadır: taşınmazın kendi 4,65M denemesi 90 günde satılamamış, 150 m²'lik en yakın büyük emsal 30 bin TL/m² ile satılamamış, gerçek talep ise <strong>~3M teklifte</strong> oluşmuştur.</p>
    <p>Bu nedenle gerçekçi satış bandı <strong>3,1–3,9M TL</strong> olarak belirlenmiştir. Bodrumun 120 m²'lik tam alanı, bu bandın <strong>"ucuza satış olmadığını"</strong> güvence altına alır — Dengeli bandın <strong>3,5–3,7M</strong> orta seviyesi hem piyasada karşılık bulur hem de taşınmazın gerçek değerini korur.</p>
  </div>
'''

pyramid = '''  <div class="pyramid">
    <div class="title">Fiyat – Süre Piramidi · P-145</div>
    <svg viewBox="0 0 580 460" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="g145a" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFE2E2"/><stop offset="100%" stop-color="#FFC9C9"/></linearGradient>
        <linearGradient id="g145b" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFC9C9"/><stop offset="100%" stop-color="#E31C2A"/></linearGradient>
      </defs>
      <polygon points="220,30 280,100 160,100" fill="url(#g145a)" stroke="#BE1622" stroke-width="1.5"/>
      <polygon points="160,100 280,100 320,190 120,190" fill="url(#g145b)" stroke="#BE1622" stroke-width="1.5"/>
      <polygon points="120,190 320,190 360,285 80,285" fill="#F2F5FA" stroke="#3A1418" stroke-width="1"/>
      <polygon points="80,285 360,285 400,395 40,395" fill="#E8EBF2" stroke="#3A1418" stroke-width="1" opacity="0.6"/>
      <line x1="250" y1="65" x2="395" y2="65" stroke="#c8c8cc" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="300" y1="145" x2="395" y2="145" stroke="#c8c8cc" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="340" y1="237" x2="395" y2="237" stroke="#c8c8cc" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="380" y1="340" x2="395" y2="340" stroke="#c8c8cc" stroke-width="1.2" stroke-dasharray="3 3"/>
      <text x="400" y="62" font-family="Poppins, sans-serif" font-size="22" font-weight="600" fill="#BE1622">Sabırlı</text>
      <text x="400" y="88" font-family="Roboto, sans-serif" font-size="13" font-weight="400" fill="#555">3.900.000 – 4.300.000 TL</text>
      <text x="400" y="138" font-family="Poppins, sans-serif" font-size="26" font-weight="700" fill="#BE1622">Dengeli</text>
      <text x="400" y="160" font-family="Poppins, sans-serif" font-size="11" font-weight="700" fill="#BE1622" letter-spacing="2.5">ÖNERİLEN</text>
      <text x="400" y="184" font-family="Roboto, sans-serif" font-size="13" font-weight="500" fill="#222">3.500.000 – 3.900.000 TL</text>
      <text x="400" y="234" font-family="Poppins, sans-serif" font-size="22" font-weight="600" fill="#3A1418">Hızlı Satış</text>
      <text x="400" y="260" font-family="Roboto, sans-serif" font-size="13" font-weight="400" fill="#555">3.100.000 – 3.400.000 TL</text>
      <text x="400" y="337" font-family="Poppins, sans-serif" font-size="20" font-weight="500" fill="#6e6e73">Değer Kaybı</text>
      <text x="400" y="362" font-family="Roboto, sans-serif" font-size="13" font-weight="400" fill="#888">3.100.000 TL altı</text>
    </svg>
  </div>
'''

scenarios = '''  <div class="sc-list">
    <p class="sc-intro">Dört senaryo:</p>
    <div class="sc">
      <div class="sc-top"><span class="sc-lbl">Sabırlı / Üst</span><span class="sc-rate">~32.500 – 35.800 TL/m² (zemin)</span></div>
      <div class="sc-price">3.900.000 – 4.300.000 TL</div>
      <div class="sc-desc">240 m² toplam kullanımı hak eden doğru alıcı + sabır gerektirir. Geniş pazarlık payı bırakır, alıcı bulma süresi uzayabilir. Daha önce denenen 4,65M seviyesinin gerçekçi biçimde altında tutulmuştur.</div>
    </div>
    <div class="sc rec">
      <span class="rec-tag">ÖNERİLEN</span>
      <div class="sc-top"><span class="sc-lbl">Dengeli</span><span class="sc-rate">~29.200 – 32.500 TL/m² (zemin)</span></div>
      <div class="sc-price">3.500.000 – 3.900.000 TL</div>
      <div class="sc-desc">Taşınmazın tüm değerini (cephe, 120 m² bodrum) yansıtırken piyasada karşılık bulabilecek gerçekçi bant. Satışa çıkış bandın üstünden (3.900.000 TL) açılır, müzakereyle 3.500.000 – 3.700.000 TL'ye iner.</div>
    </div>
    <div class="sc">
      <div class="sc-top"><span class="sc-lbl">Hızlı Satış</span><span class="sc-rate">~25.800 – 28.300 TL/m² (zemin)</span></div>
      <div class="sc-price">3.100.000 – 3.400.000 TL</div>
      <div class="sc-desc">Alınan tekliflerin (~3M) hemen üstü. Daha hızlı kapanış isteyen satıcı için; 1–2 ay içinde sonuç olasılığı yüksek, pazarlık marjı daralır.</div>
    </div>
    <div class="sc">
      <div class="sc-top"><span class="sc-lbl">Değer Kaybı</span><span class="sc-rate">~25.800 TL/m² altı</span></div>
      <div class="sc-price">3.100.000 TL altı</div>
      <div class="sc-desc">Alınan tekliflerin seviyesinde veya altı; bodrumun değerini eksik fiyatlar. Yalnızca acil nakit ihtiyacında düşünülür — önerilmez.</div>
    </div>
  </div>
'''

final = '''    <div class="final-price">
      <div class="fp-title">Önerilen Satışa Çıkış Fiyatı</div>
      <div class="fp-rate-top">Dengeli bandın üstünden açılış · müzakereyle orta banda</div>
      <div class="fp-amount">3.900.000 TL</div>
      <div class="fp-rate">SATIŞA ÇIKIŞ (İLAN) FİYATI<span class="calc">Müzakere ile hedef gerçekleşme: 3.500.000 – 3.700.000 TL</span></div>
      <div class="fp-desc">Satışa çıkış, Dengeli bandın üst ucundan (3.900.000 TL) açılır; müzakereyle 3.500.000 – 3.700.000 TL'ye inmesi beklenir. Bu seviye, taşınmazın kendi 4,65M denemesinin (90 gün satılamadı) gerçekçi biçimde altında konumlanarak hem cephe ve 120 m² bodrum değerini korur, hem de piyasada karşılık bulma şansını yükseltir. Alınan ~3M tekliflerin belirgin üstünde, makul bir primle.</div>
    </div>
'''

deger = ('<section class="block">\n  <div class="wrap">\n'
         '    <div class="block-head">\n      <div class="block-num">03</div>\n'
         '      <h2>Değer Analizi ve Fiyat Aralığı</h2>\n'
         '      <p class="block-intro">Taşınmazın içsel bileşen değeri ile pazar analizini birlikte '
         'değerlendirerek dört satış senaryosu oluşturduk. Önerimiz, hem taşınmazın değerini yansıtan '
         'hem de piyasada karşılık bulabilecek <strong>Dengeli</strong> banttır.</p>\n    </div>\n\n'
         + deger_bilesen +
         '\n    <div class="price-grid">\n' + scenarios + pyramid + '    </div>\n\n'
         + final +
         '  </div>\n</section>\n')

# ------------------------------------------------------------------ 04 RİSKLER
maliyet = '''    <div class="tax">
      <h4>Maliyet Hesabı</h4>
      <div class="sub">Hedeflenen satış bedeli (Dengeli orta): <strong>3.700.000 TL</strong> · 500.000 TL üstü portföyler için %2 hizmet bedeli + %20 KDV uygulanır.</div>

      <div class="tax-row">
        <div class="tx-lbl">Hizmet Bedeli (%2)</div>
        <div class="tx-desc">3.700.000 × %2 = 74.000 TL</div>
        <div class="tx-amt">74.000 TL</div>
      </div>
      <div class="tax-row">
        <div class="tx-lbl">KDV (%20)</div>
        <div class="tx-desc">Hizmet bedeli üzerinden</div>
        <div class="tx-amt">14.800 TL</div>
      </div>

      <div class="tax-total">
        <div class="l">Toplam Kesinti</div>
        <div class="a">88.800 TL</div>
      </div>
      <div class="tax-total net">
        <div class="l">Net Elinize Geçen</div>
        <div class="a">≈ 3.611.200 TL</div>
      </div>

      <p class="tax-note"><strong>Not:</strong> Tapu harcı alıcı tarafından ödenir, satıcı maliyetine dahil değildir. Değer artış kazancı vergisi, taşınmazın edinim tarihine ve satış kazancına göre ayrıca değerlendirilmeli; ticari nitelik nedeniyle vergi durumu mali müşavirinizle teyit edilmelidir.</p>
    </div>

    <div class="risk-box">
      <h4>Dikkat Edilecek Hususlar</h4>
      <ul class="risk-list">
        <li><strong>Önceki 4,65M denemesi:</strong> Taşınmaz daha önce yüksek fiyattan çıkıp 90 gün satılamadığı için "uzun süredir satılık / pahalı" algısı oluşmuş olabilir. Yeni ve gerçekçi fiyatla, doğru kanallarda taze bir sunum bu algıyı kırar.</li>
        <li><strong>Bodrum kullanımı:</strong> 120 m² bodrumun kullanılabilirliği (nem, ışık, ayrı giriş, tavan yüksekliği) değeri doğrudan etkiler. Net bilgi ve mümkünse yerinde gösterim, fiyatı üst banda taşır.</li>
        <li><strong>Alıcı kitlesi:</strong> 27–30 m² küçük dükkanlar düşük mutlak fiyatla (~1,5M) hızlı alıcı çekiyor; 120 m² tek parça büyük dükkanın alıcı kitlesi daha dardır. Bu nedenle doğru alıcıya hedefli pazarlama ve sabır önemlidir.</li>
        <li><strong>Cephe avantajı:</strong> Ana yola cepheli konum ve geniş vitrin taşınmazın en güçlü yönüdür; sunumda ve görsellerde öne çıkarılmalıdır.</li>
      </ul>
    </div>
'''

riskler = ('<section class="block">\n  <div class="wrap">\n'
           '    <div class="block-head">\n      <div class="block-num">04</div>\n'
           '      <h2>Riskler ve Maliyetler</h2>\n'
           '      <p class="block-intro">Aşağıdaki tablo, satışın <strong>3.700.000 TL</strong> (Dengeli hedef orta) '
           'üzerinden gerçekleşmesi durumunda hizmet bedeli kesintisi sonrası elinize geçecek tahmini net tutarı '
           'göstermektedir.</p>\n    </div>\n\n'
           + maliyet +
           '  </div>\n</section>\n')

# ------------------------------------------------------------------ İMZA + birleştir
imza = B.signature()
lb   = B.lightbox()

html = head + top + kapak + profil + pazar + deger + riskler + imza + lb

OUT = os.path.join(HERE, "index.html")
B.write_and_check(OUT, html)
B.render(OUT, full=True)
