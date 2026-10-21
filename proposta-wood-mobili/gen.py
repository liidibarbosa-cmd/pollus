import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SUPERIOR, INFERIOR, H

E = html.escape
TAGS = {'ped': ('t-ped', 'Pedido anterior Wood Mobili'),
        'pe': ('t-pe', 'Acréscimo · pronta entrega'),
        'enc': ('t-enc', 'Acréscimo · encomenda a definir')}


def swatches(sw):
    if sw == H:
        return '<span class="sw hatch"></span>'
    return ''.join(f'<span class="sw" style="background-image:url(img/sw/{s}.jpg)"></span>' for s in sw)


def finish(f):
    bs = f['b'] if isinstance(f['b'], list) else [f['b']]
    fns = f['fn'] if isinstance(f['fn'], list) else [f['fn']]
    label = ' + '.join(f'<b>{E(b)}</b>' + (f' {E(fn)}' if fn else '') for b, fn in zip(bs, fns))
    if f['pend']:
        label += ' · <em class="pend">a definir</em>'
    pair = ' pair' if f['sw'] != H and len(f['sw']) > 1 else ''
    return f'<span class="fin{pair}"><span class="sws">{swatches(f["sw"])}</span><span class="fl">{label}</span></span>'


def item(it):
    cls, label = TAGS[it['tag']]
    if it['img']:
        thumb = f'<div class="thumb"><img src="img/prod/{it["img"]}.png" alt=""></div>'
    else:
        thumb = '<div class="thumb ph"><span>A definir</span></div>'
    qty = f' <span class="qty">{E(it["qty"])}</span>' if it['qty'] else ''
    out = [f'<div class="item">{thumb}<div class="body">',
           f'<h4 class="{"red" if it["red"] else ""}">{E(it["name"])}{qty}</h4>',
           f'<span class="tag {cls}">{label}</span>']
    if it['desc']:
        out.append(f'<p class="desc">{E(it["desc"])}</p>')
    if it['meas']:
        out.append(f'<p class="meas">{E(it["meas"])}</p>')
    if it['note']:
        out.append(f'<p class="note">{E(it["note"])}</p>')
    if it['fin']:
        out.append('<div class="fins">' + ''.join(finish(f) for f in it['fin']) + '</div>')
    if it['options']:
        out.append('<div class="opts">' + ''.join(
            f'<figure><div class="oimg"><img src="img/prod/{img}.png" alt=""></div><figcaption>{E(n)}</figcaption></figure>'
            for n, img in it['options']) + '</div>')
    out.append('</div></div>')
    return ''.join(out)


def amb(a):
    code = f'<span class="code">{E(a["code"])}</span>' if a['code'] else ''
    return (f'<section class="amb"><header>{code}<h3>{E(a["name"])}</h3><span class="count">{E(a["count"])}</span></header>'
            f'<p class="ref">Madeira de referência: <b>{E(a["ref"])}</b></p>'
            + ''.join(item(i) for i in a['items']) + '</section>')


LEGEND = ('<div class="legend"><span class="tag t-ped">Pedido anterior Wood Mobili</span><span class="lg">itens que a loja já pediu à Pollus</span>'
          '<span class="sep"></span><span class="tag t-pe">Acréscimo · pronta entrega</span><span class="tag t-enc">Acréscimo · encomenda a definir</span>'
          '<span class="lg">itens indicados nesta proposta</span></div>')

FOOT = '<footer class="pf"><span>Proposta de Mobiliário — Wood Mobili · Pollus Móveis · Lista por ambiente</span><span>Orçamento mediante aprovação do layout. · {n}/3</span></footer>'


def list_page(title, ambs, cols, n, closing=''):
    return (f'<div class="page list">'
            f'<div class="phead"><div><p class="kicker">Lista por ambiente</p><h2>{E(title)} <span class="sub">Modelo · quantidade · medidas · acabamentos · origem</span></h2></div>'
            f'<img class="mini" src="img/prod/logo.png" alt="Pollus Móveis"></div>'
            f'{LEGEND}<div class="cols c{cols}">' + ''.join(f'<div class="col">{amb(a)}</div>' for a in ambs) + '</div>'
            f'{closing}{FOOT.format(n=n)}</div>')


COVER = '''<div class="page cover">
<img class="logo" src="img/prod/logo.png" alt="Pollus Móveis">
<div class="ctitle"><p class="kicker">Proposta de layout para aprovação · Revisão</p>
<h1>Proposta de Mobiliário<br><span>— Wood Mobili</span></h1>
<p class="meta">Lista por ambiente <i>·</i> São Paulo <i>·</i> 16 de outubro de 2026</p></div>
<div class="toc"><div><h5>Pavimento superior</h5><p>Cozinha · AMB 1 · AMB 2 · AMB 3</p></div>
<div><h5>Pavimento inferior</h5><p>AMB 4 · AMB 5 · AMB 6</p></div>
<div><h5>Em cada item</h5><p>Pedido anterior Wood Mobili ou acréscimo indicado nesta proposta</p></div></div>
<footer class="pf"><span>Pollus Móveis</span><span>1/3</span></footer></div>'''

CLOSING = '''<div class="closing"><div><h3>Orçamento mediante aprovação do layout.</h3>
<p>Item do pedido anterior ainda sem posição nesta proposta: Banco Yago 1,60 m. Cores das amostras podem variar conforme tela e impressão.</p></div>
<p class="contact">Pollus Móveis · (17) 3426-1234 · www.pollusmoveis.com.br · @pollusmoveis</p></div>'''

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Proposta de Mobiliário — Wood Mobili · lista por ambiente</title>
<meta name="author" content="Pollus Móveis"><meta name="subject" content="Lista por ambiente para aprovação">
<link rel="stylesheet" href="fonts/fonts.css"><link rel="stylesheet" href="style.css"></head><body>
{COVER}
{list_page('Pavimento superior — lista por ambiente', SUPERIOR, 4, 2)}
{list_page('Pavimento inferior — lista por ambiente', INFERIOR, 3, 3, CLOSING)}
</body></html>'''

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'), 'w', encoding='utf-8').write(doc)
print('ok')
