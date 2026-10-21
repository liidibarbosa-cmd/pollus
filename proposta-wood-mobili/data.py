# Conteúdo da proposta — Wood Mobili · lista por ambiente (revisão 21/10/2026)
# tag: 'ped' = Pedido anterior Wood Mobili · 'pe' = Acréscimo · pronta entrega · 'enc' = Acréscimo · encomenda a definir
# fin: (amostras, nome em destaque, função, a_definir)
#   amostras = lista de arquivos em img/sw (1 ou 2 — 2 só para acabamentos "irmãos") ou 'hatch' (pendente / a definir)

H = 'hatch'

def F(sw, bold, fn='', pend=False):
    return {'sw': sw if sw == H else (sw if isinstance(sw, list) else [sw]), 'b': bold, 'fn': fn, 'pend': pend}

def I(name, tag, img=None, qty=None, meas=None, note=None, fin=(), desc=None, red=False, options=None):
    return dict(name=name, tag=tag, img=img, qty=qty, meas=meas, note=note, fin=list(fin), desc=desc, red=red, options=options)

SUPERIOR = [
  dict(code=None, name='Cozinha', count='1 do pedido', ref='Cacau + Louro Pardo', items=[
    I('Banqueta Lia LX', 'ped', 'banqueta-lia-lx', 'x6', 'altura 990', 'ao longo da ilha',
      [F('revestimento-caramelo', 'Revestimento Caramelo', 'assento'), F('cacau', 'Cacau', 'madeira')]),
  ]),
  dict(code='AMB 1', name='Jantar', count='1 do pedido', ref='Pinhão + Louro Pinhão', items=[
    I('Cadeira Repouso', 'ped', 'cadeira-repouso', 'x6', fin=[F('tecido-3.86.004', 'Tecido 3.86.004', 'estofado'), F('pinhao', 'Pinhão', 'madeira')]),
  ]),
  dict(code='AMB 2', name='Estar', count='4 do pedido', ref='Cacau + Louro Pardo', items=[
    I('Poltrona Tronco', 'ped', 'poltrona-tronco', 'x2', fin=[F('soleta-areia', 'Soleta Areia', 'couro'), F('laca-belga', 'Laca Belga', 'laca'), F('cacau', 'Cacau', 'madeira')]),
    I('Poltrona Copan', 'ped', 'poltrona-copan', 'x2', note='base do tapete',
      fin=[F('tecido-5.71.031', 'Tecido 5.71.031', 'estofado'), F('cacau', 'Cacau', 'madeira'), F('la-paz-pinhao', 'La Paz Pinhão', 'couro · acabamento')]),
    I('Banco Laos LX', 'ped', 'banco-laos-lx', meas='1,60 m · apenas com pesponto',
      fin=[F('revestimento-caramelo', 'Revestimento Caramelo', 'assento'), F('cacau', 'Cacau', 'madeira'), F('laca-champanhe', 'Metal laqueado Champanhe', 'metal')]),
    I('Banco Baru', 'ped', 'banco-baru', meas='2,00 m', note='atrás do sofá',
      fin=[F('tecido-4.69.033', 'Tecido 4.69.033', 'assento'), F('laca-champanhe', 'Laca Champanhe', 'metal'), F('cacau', 'Cacau', 'madeira')]),
  ]),
  dict(code='AMB 3', name='Jantar', count='2 do pedido', ref='Nogueira + Carvalho Castanho', items=[
    I('Mesa de jantar Fungi', 'ped', 'mesa-jantar-fungi', meas='2,50 × 1,20 m', fin=[F('nogueira', 'Nogueira', 'base e tampo')]),
    I('Buffet Tamboré', 'ped', 'buffet-tambore', meas='1,85 m', fin=[F('carvalho-castanho', 'Carvalho Castanho', 'lâmina'), F('laca-champanhe', 'Laca Champanhe', 'laca')]),
  ]),
]

INFERIOR = [
  dict(code='AMB 4', name='Estar', count='2 do pedido', ref='Cacau + Louro Pardo', items=[
    I('Home Volpi', 'ped', 'home-volpi', meas='2,50 m', fin=[F('louro-pardo', 'Louro Pardo', 'lâmina'), F('laca-taupe', 'Laca Taupe', 'laca')]),
    I('Sofá Planalto', 'ped', 'sofa-planalto', meas='ver layout · braço direito · bandeja esquerda',
      fin=[F('tecido-5.53.024', 'Tecido 5.53.024', 'estofado'), F(['castanho', 'carvalho-castanho'], ['Castanho', 'Carvalho Castanho'], ['madeira', 'lâmina'])]),
  ]),
  dict(code='AMB 5', name='Estar', count='4 do pedido', ref='Castanho + Carvalho Castanho', items=[
    I('Sofá Nimbus Slim composê', 'ped', 'sofa-nimbus', meas='2,76 m',
      fin=[F('revestimento-caramelo', 'Revestimento Caramelo', 'costas'), F('tecido-4.71.028', 'Tecido 4.71.028', 'corpo'), F('castanho', 'Castanho', 'base')]),
    I('Poltrona Ícaro', 'ped', 'poltrona-icaro', 'x2', fin=[F('tecido-5.71.026', 'Tecido 5.71.026', 'estofado'), F('castanho', 'Castanho', 'madeira')]),
    I('Buffet Tamboré', 'ped', 'buffet-tambore', meas='1,85 m', fin=[F('nogueira', 'Nogueira', 'lâmina'), F('laca-champanhe', 'Laca Champanhe', 'laca')]),
    I('Banco Yago', 'ped', 'banco-yago', meas='1,80 m',
      fin=[F('tecido-4.69.038', 'Tecido 4.69.038', 'assento'), F('revestimento-caramelo', 'Revestimento Caramelo', 'acabamento'),
           F('laca-champanhe', 'Laca Champanhe', 'metal'), F('castanho', 'Castanho', 'madeira')]),
  ]),
  dict(code='AMB 6', name='Jantar + apoio', count='3 do pedido', ref='Noce + Carvalho Noce', items=[
    I('Mesa de jantar Âmbar', 'ped', 'mesa-jantar-ambar', meas='1,60 × 1,20 m', fin=[F('castanho', 'Castanho', 'base e tampo')]),
    I('Cadeira Pitaia', 'ped', 'cadeira-pitaia', 'x8', fin=[F(H, 'Tecido', 'estofado', True), F(H, 'Madeira', '', True)]),
    I('Cadeira Angá com braço', 'ped', 'cadeira-anga', 'x6', fin=[F('tecido-3.10.001', 'Tecido 3.10.001', 'estofado'), F('castanho', 'Castanho', 'madeira')]),
  ]),
]
